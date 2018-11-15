End to End Testing
=======

Feature files are living documentation. They hold functionality of the code described in a DSL understandeable as plain english. This DSL is then parsed by programming-language-specific libraries, and translated into end-to-end tests.
Please refer to cucumber/behave documentation to get started regarding the gherkin syntax, what are step definitions etc.

Framework
----
The Gherkin syntax is used to describe features/scenarios.
Behave is used to run our tests, with selenium on Firefox.

Tags
----
The @skip tag may be used to skip scenarios or entire features if needed.

Directory Structure
----
- `features/` has feature files, in the Given, When, Then Gherkin syntax
- Inside the `features/` directory, the `.feature` files are categorized into streams and a `common` directory, which holds features that are common to all streams or do not belong to any stream
- `steps/` has step definitions

Requirements
---
- Xvfb _To be able to run selenium in headless mode_
- python-paramiko _installing this through pip requires build tools and gcc setup_

Installation
----
```
git clone
cd spicegate
pip install behave
pip install selenium
pip install pyyaml
pip install paramiko
pip install xvfbwrapper # Only if you want to run browser in headless mode

Alternatively, you can run "pip install -r requirements.text" from the root of the source tree to install the requisite Python packages.
```

Configuration Settings
----
`config/settings.yml` provides configuration options for all environments.
The default environment is 'development', but can be specified as `development` environment variable.

For example: To use the Google URL from the development environment:
1. Enter value for any uri in settings.yml, development: section



'config/settings.yml' is loaded to context.data variable in order for it to be used globally across behave scripts. Please add your config structure to `config/settings.yml` first and the you can retrieve it from context.data.


Run Tests
----
From the project root,

`behave # for python`

You can open the image created by screenshot at /tmp/ directory using 'gnome-open' command in a linux system

Headless mode
----
For running on systems without a display (such as jenkins), we need to use headless mode.

- Install Xvfb. `xorg-X11-server-Xvfb` on fedora/RHEL
- For python, install xvfbwrapper: `pip install xvfbwrapper`

# stylelabs

Restapi.py
---

This file contains script for test automation assessment - 2. For running the restapi.py file, simply do a:
# python3 restapi.py
or
# pytest restapi.py
