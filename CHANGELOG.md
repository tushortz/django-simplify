# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.1.5] - 2021-04-14
### Added
- added doc strings for `TimeBasedModel`, `TimeBasedModel` and `AlphaNumericFilterAdmin`

### Fixes
- fixed generated `urls.py` adding url paths on newline
- - fixed `include` being imported multiple times for every app

## [0.1.4] - 2021-04-14
### Removed
- removed unnecessary user import statement in stub

### Fixes
- fixed `include` not being imported in `urls.py`
- fixed extra unnecessary new line in `urls.py` creation


## [0.1.3] - 2021-04-14
### Fixes
- fixed error caused due to extra format parameter added in 0.1.2
- replaced `User` model instead to use `_MY_MODEL_HERE_` placeholder

## [0.1.0 - 0.1.2] - 2021-04-13
### Added
- added create view functionality
- updated create_app so user can specify optional view to create
- added create_view command so user can create standalone view
- fixed error caused when inheriting from `AlphaNumericFilterAdmin` without specifying `alphanumeric_filter` fields.  

## [0.0.6 - 0.0.9] - 2021-04-12
### Added
- added create model functionality
- added ability to auto generate admin model
- added `AlphaNumericFilterAdmin` to model helper

### Fixes
- bug fixes


## [0.0.2 - 0.0.5] - 2021-04-12
### Added 
- added auto import of modules
- added ability to add created app to settings.INSTALLED_APPS
- added create_app command


## [0.0.1] - 2021-04-11
### Added
- Initial creation
- added `TimeBasedModel` and `NamedTimeBased` model
