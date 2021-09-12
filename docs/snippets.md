---
title: Snippets - Jean-Luc Tibaux
description: my personal collection of useful code snippets
---

# :octicons-code-24: Snippets

## Android SDK setup

**environment**: :simpleicons-linux: linux -> :simpleicons-gnubash: `bash`

!!! info ""
    Meant to be used for a quick setup of a :simpleicons-linux: `linux` dev environment for [TinyWeatherForecastGermany (TWFG)](/index.html#tinyweatherforecastgermany-twfg).

```java
sudo apt -y install openjdk-8-jdk-headless

wget "https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip"
mkdir -p Android/Sdk
unzip "commandlinetools-linux-7583922_latest.zip" -d Android/Sdk

export ANDROID_HOME=$(pwd)/Android/Sdk/cmdline-tools
export PATH="$ANDROID_HOME/bin:$ANDROID_HOME/lib:$ANDROID_HOME/emulator:$ANDROID_HOME/patcher:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$PATH"

sdkmanager --update --sdk_root=${ANDROID_HOME}
sdkmanager --list --sdk_root=${ANDROID_HOME} | grep "build-tools"
sdkmanager "build-tools;29.0.3" "platforms;android-29" "sources;android-29" --sdk_root=${ANDROID_HOME}
sdkmanager --licenses --sdk_root=${ANDROID_HOME}

sudo apt -y install gradle
```

## code search using [dezip.org](https://www.dezip.org/)

!!! info ""
    To search the contents of code repositories using :octicons-archive-16: archives.

### [update](https://www.dezip.org/https://codeberg.org/Starfish/TinyWeatherForecastGermany/archive/master.tar.gz) the cached tar archive

GET request: <https://www.dezip.org/https://codeberg.org/Starfish/TinyWeatherForecastGermany/archive/master.tar.gz>

!!! warning "warning"
    **Please use the `update` function responsible and if possible not more than once per day. This services operates on a fair use policy with limited bandwith. Please don't make the creator turning it into a paid service with captchas, geoblocking, etc. by wasting bandwith. Also [see here for more information](https://codeberg.org/Codeberg/Community/issues/379#issuecomment-237979) :octicons-link-external-16:.**

### [search](https://www.dezip.org/v1/9/https/codeberg.org/Starfish/TinyWeatherForecastGermany/archive/master.tar.gz/tinyweatherforecastgermany/) cached repository contents

Visit <https://www.dezip.org/v1/9/https/codeberg.org/Starfish/TinyWeatherForecastGermany/archive/master.tar.gz/tinyweatherforecastgermany/> using your browser of choice.

Type ++f++ to **search** and ++k++ or ++j++ to **change** between search results.


*[DWD]: Deutscher Wetterdienst, the German national weather agency similar to NOAA in the US
*[TWFG]: inofficial abbreviation for Tiny Weather Forecast Germany
