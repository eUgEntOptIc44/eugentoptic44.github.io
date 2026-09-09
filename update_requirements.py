#!/usr/bin/env python3.11
"""
Helper script to fetch and update all packages in requirements.txt to their latest versions.
Uses PyPI JSON API to get latest version information.
"""

import regex
import requests
from pathlib import Path
from typing import Optional, Tuple

# Enhanced regex patterns for parsing requirements
# Supports: package==1.0, package>=1.0, package[extra]==1.0, package @ URL, etc.

# Full requirement line pattern with version specifier
REQUIREMENT_PATTERN = regex.compile(
    r"""
    ^\s*
    (?P<name>[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)   # package name
    (?:\[(?P<extras>[A-Za-z0-9,._-]+)\])?                   # optional extras [extra1,extra2]
    \s*
    (?P<operator>==|>=|<=|~=|!=|>|<|===)                    # version operator
    \s*
    (?P<version>[^;\#\s]+)                                  # version string
    (?:;\s*(?P<markers>[^\#]+?))?                           # optional environment markers
    \s*
    (?:\#\s*(?P<comment>.*))?                               # optional inline comment
    \s*$
    """,
    regex.VERBOSE | regex.IGNORECASE
)

# Package without version specifier
PACKAGE_ONLY_PATTERN = regex.compile(
    r"""
    ^\s*
    (?P<name>[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)   # package name
    (?:\[(?P<extras>[A-Za-z0-9,._-]+)\])?                   # optional extras
    \s*
    (?:;\s*(?P<markers>[^\#]+?))?                           # optional environment markers
    \s*
    (?:\#\s*(?P<comment>.*))?                               # optional inline comment
    \s*$
    """,
    regex.VERBOSE | regex.IGNORECASE
)

# URL-based requirement (package @ URL)
URL_REQUIREMENT_PATTERN = regex.compile(
    r"""
    ^\s*
    (?P<name>[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)   # package name
    (?:\[(?P<extras>[A-Za-z0-9,._-]+)\])?                   # optional extras
    \s*@\s*
    (?P<url>\S+)                                            # URL
    (?:;\s*(?P<markers>[^\#]+?))?                           # optional environment markers
    \s*
    (?:\#\s*(?P<comment>.*))?                               # optional inline comment
    \s*$
    """,
    regex.VERBOSE | regex.IGNORECASE
)


def get_latest_version(package_name: str) -> Optional[str] | None:
    """
    Fetch the latest version of a package from PyPI.
    
    Args:
        package_name (str): The name of the package to check.

    Returns:
        latest_version (str | None): The latest version string if found, else None.
    
    """
    # Normalize package name (PyPI uses lowercase and hyphens)
    normalized_name = package_name.lower().replace("_", "-")
    url = f"https://pypi.org/pypi/{normalized_name}/json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except requests.RequestException as e:
        print(f"  Warning: Could not fetch version for {package_name}: {e}")
        return None


def parse_requirement_line(line: str) -> Optional[Tuple[str, str, str, str, str, str]]:
    """
    Parse a requirement line and return parsed components.
    Returns None for comments, empty lines, or un-parseable lines.

    Args:
        line (str): A line from requirements.txt.

    Returns:
        line (Tuple[str, str, str] | None): A tuple of (package_name, operator, version) or None.
    """
    line = line.strip()
    
    # Skip empty lines and pure comments
    if not line or line.startswith("#"):
        return None
    
    # Skip -r, -e, --index-url and other options
    if line.startswith(("-", "--")):
        return None
    
    # Try URL-based requirement first (package @ URL)
    match = URL_REQUIREMENT_PATTERN.match(line)
    if match:
        # For URL requirements, we can't update versions automatically
        return None
    
    # Try standard requirement with version specifier
    match = REQUIREMENT_PATTERN.match(line)
    if match:
        return (
            match.group("name"),
            match.group("extras") or "",
            match.group("operator"),
            match.group("version"),
            match.group("markers") or "",
            match.group("comment") or "",
        )
    
    # Try package without version
    match = PACKAGE_ONLY_PATTERN.match(line)
    if match:
        return (
            match.group("name"),
            match.group("extras") or "",
            "",
            "",
            match.group("markers") or "",
            match.group("comment") or "",
        )
    
    return None


def update_requirements(requirements_path: Path, dry_run: bool = False) -> bool:
    """
    Update all packages in requirements.txt to their latest versions.
    
    Args:
        requirements_path (Path): Path to the requirements.txt file.
        dry_run (bool): If True, do not write changes, just show what would be updated.

    Returns:
        status (bool): `True` if updates were made, `False` otherwise.
    """
    if not requirements_path.exists():
        print(f"Error: {requirements_path} not found")
        return False
    
    content = requirements_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    updated_lines = []
    updates = []
    
    print(f"Processing {requirements_path}...\n")
    
    for line in lines:
        parsed = parse_requirement_line(line)
        
        if parsed is None:
            # Keep comments, empty lines, options, and URL requirements as-is
            updated_lines.append(line)
            continue
        
        package_name, extras, operator, current_version, markers, comment = parsed
        extras_str = f"[{extras}]" if extras else ""
        display_name = f"{package_name}{extras_str}"
        print(f"Checking {display_name}...", end=" ")
        
        latest_version = get_latest_version(package_name)
        
        if latest_version is None:
            # Keep original line if we couldn't fetch version
            updated_lines.append(line)
            print("(keeping original)")
            continue
        
        if current_version == latest_version:
            updated_lines.append(line)
            print(f"up to date ({current_version})")
        else:
            # Use == for pinned versions
            new_operator = "==" if operator in ("==", "") else operator
            # Reconstruct the line preserving extras, markers, and comments
            new_line = f"{package_name}{extras_str}{new_operator}{latest_version}"
            if markers:
                new_line += f" ; {markers.strip()}"
            if comment:
                new_line += f"  # {comment}"
            updated_lines.append(new_line)
            updates.append((display_name, current_version or "none", latest_version))
            print(f"{current_version or 'none'} -> {latest_version}")
    
    print("\n" + "=" * 50)
    
    if not updates:
        print("All packages are already at their latest versions!")
        return False
    
    print(f"\nFound {len(updates)} package(s) to update:")
    for pkg, old, new in updates:
        print(f"  {pkg}: {old} -> {new}")
    
    if dry_run:
        print("\n[Dry run] No changes written.")
        print("\nUpdated content would be:")
        print("-" * 40)
        print("\n".join(updated_lines))
        return False
    else:
        requirements_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
        print(f"\n✓ Updated {requirements_path}")

    return True

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Update requirements.txt to latest package versions"
    )
    parser.add_argument(
        "requirements_file",
        nargs="?",
        default="requirements.txt",
        help="Path to requirements.txt (default: requirements.txt)",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be updated without making changes",
    )
    
    args = parser.parse_args()
    requirements_path = Path(args.requirements_file)
    
    update_requirements(requirements_path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
