---
title: Projects - Jean-Luc Tibaux
description: Projects that I contribute/d to: TinyWeatherForecastGermany, Hypatia, Currencies
---

# :octicons-project-24: Projects

An unordered list of open source :material-open-source-initiative: projects that I contribute/d to:

!!! help "shortcuts"
    Type ++s++ or ++f++ to :octicons-search-16: **search** this site.
    Type ++p++ or ++comma++ to go the :material-skip-previous: **previous** page.
    Type ++n++ or ++period++ to go the **next** :material-skip-next: page.

## [Tiny Weather Forecast Germany (TWFG)](https://tinyweatherforecastgermanygroup.gitlab.io/index/index.html)

!!! info "about"
    An android open source weather forecast app written in `java` focused on Germany using open data provided by Deutscher Wetterdienst (DWD).

**Maintainer**: Pawel Dube ([@Starfish](https://codeberg.org/Starfish)) :octicons-star-16: :material-fish:

[:simpleicons-codeberg: code repository](https://codeberg.org/Starfish/TinyWeatherForecastGermany/){ .md-button }

[:simpleicons-fdroid: F-Droid page](https://f-droid.org/packages/de.kaffeemitkoffein.tinyweatherforecastgermany){ .md-button }

[:material-home-search: searchable table of all locations -> *"areas"*](https://tinyweatherforecastgermanygroup.gitlab.io/index/areas.html)

[:material-home-search: searchable table of all **stations**](https://tinyweatherforecastgermanygroup.gitlab.io/index/stations.html)

[:material-map-plus: OpenStreetMap based **map** visualizing all data sources used by TWFG](https://tinyweatherforecastgermanygroup.gitlab.io/index/map.html)

[:material-frequently-asked-questions: list of Frequently asked questions (**FAQ**)](https://tinyweatherforecastgermanygroup.gitlab.io/index/index.html#faq)

[:octicons-code-24: :material-help: javadoc **code documentation**](https://tinyweatherforecastgermanygroup.gitlab.io/twfg-javadoc/index.html)

??? info "note"
    The **javadoc** docs and **map** are both automatically updated **once daily**.

    The docs also contain :fontawesome-solid-project-diagram: **UML** diagrams generated using [graphviz](https://gitlab.com/graphviz/graphviz) via [PlantUML](https://plantuml.com/) integrated in the [uml-java-doclet](https://github.com/gboersma/uml-java-doclet) by Gerald Boersma ([@gboersma](https://github.com/gboersma)).

### :octicons-mirror-24: Mirrors

!!! info "note"
    The following git repositories are updated **once daily** at 5am UTC.

    Target: increased SEO-Scores, leading interested members of the public to the 'main' project at [:simpleicons-codeberg: codeberg.org](https://codeberg.org/Starfish/TinyWeatherForecastGermany/) the home of the user and developer communities of TinyWeatherForecastGermany

[:material-gitlab: **GitLab** Mirror](https://gitlab.com/tinyweatherforecastgermanygroup/TinyWeatherForecastGermany)[^1]

[:material-github: **GitHub** Mirror](https://github.com/tinyweatherforecastgermanygroup/TinyWeatherForecastGermany)[^1]

[:material-git: **framagit** Mirror](https://framagit.org/tinyweatherforecastgermanygroup/tinyweatherforecastgermanymirror)[^1]

[:simpleicons-gitea: **Gitea** Mirror](https://gitea.com/tinyweatherforecastgermanygroup/TinyWeatherForecastGermanyMirror)[^1]

If you'd like to add a **new** mirror repository on a hosted GitLab, GitHub Enterprise, Gitea, Gogs instance or any other :fontawesome-brands-git: server please get in touch with me ([@eUgEntOptIc44](https://codeberg.org/eUgEntOptIc44)) :material-email:. 

### :material-translate: Translations

Translations of **TinyWeatherForecastGermany** are managed on the :simpleicons-weblate: **weblate**[^2] instance maintained by Marcus Hoffmann ([@Bubu](https://bubu1.eu/)).

[![weblate translation status](https://weblate.bubu1.eu/widgets/tiny-weather-forecast-germany/-/multi-blue.svg "weblate translation status of TinyWeatherForecastGermany")](https://weblate.bubu1.eu/engage/tiny-weather-forecast-germany/){ loading=lazy title="weblate translation status" }

[^1]: maintained by myself using a scheduled GitLab CI/CD job :octicons-rocket-16:
[^2]: an open source SaaS for community translations of apps and websites.

## [Hypatia](https://gitlab.com/divested-mobile/hypatia)

!!! info "about"
    An open source android `java` virus scanner app using hash signatures from several open sources.

Maintainer: Tad ([@IratePorcupine](https://gitlab.com/IratePorcupine))

[:material-gitlab: code repository](https://gitlab.com/divested-mobile/hypatia){ .md-button }

[:simpleicons-fdroid: F-Droid page](https://f-droid.org/packages/us.spotco.malwarescanner/){ .md-button }

### :material-translate: Translations

* French[^3]
* German
* Italian
* Portuguese
* Spanish
* Russian

[^3]: My contribution :fontawesome-regular-grin:

## [Currencies](https://github.com/sal0max/currencies)

!!! info "about"
    An open source android `kotlin` currency converter app.

Maintainer: [@sal0max](https://github.com/sal0max)

[:material-github: code repository](https://github.com/sal0max/currencies){ .md-button }

[:simpleicons-googleplay: play store page](https://play.google.com/store/apps/details?id=de.salomax.currencies){ .md-button }

[:simpleicons-fdroid: F-Droid page](https://f-droid.org/packages/de.salomax.currencies){ .md-button }

### :material-translate: Translations

Translations of :material-currency-eur::material-currency-gbp::material-currency-usd::material-currency-jpy: **Currencies** are managed on the :simpleicons-weblate: weblate[^2] instance maintained by Marcus Hoffmann ([@Bubu](https://bubu1.eu/)).

[![weblate translation status](https://weblate.bubu1.eu/widgets/currencies/-/multi-blue.svg "weblate translation status of currencies")](https://weblate.bubu1.eu/engage/currencies){ loading=lazy title="weblate translation status" }


### :octicons-database-16: Data sources

* [exchangerate.host :octicons-link-external-16:](https://exchangerate.host/#/#faq) providing over 160 currencies
* [frankfurter.app :octicons-link-external-16:](https://www.frankfurter.app/docs/) providing over 30 currencies -> data provided by the European Central Bank (ECB)
* [fer.ee :material-github:](https://github.com/narorolib/fer): an alternative service that behaves just like [frankfurter.app](https://www.frankfurter.app/docs/)

All sources rely (partialy) on the ECB see [here for more information](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) on their terms and conditions concerning data usage, privacy, etc.

*[DWD]: Deutscher Wetterdienst, the German national weather agency similar to NOAA in the US
*[ECB]: European Central Bank
*[TWFG]: inofficial abbreviation for Tiny Weather Forecast Germany
*[SaaS]: Software as a Service
*[FAQ]: Frequently asked questions
