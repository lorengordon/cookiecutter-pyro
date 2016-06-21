{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
{%- set is_open_source = cookiecutter.open_source_license != 'Not Open Source' -%}
{%- if is_open_source -%}
[![License Status](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ project_slug }}.svg)](./LICENSE)
{%- endif %}
[![Documentation Status](https://readthedocs.org/projects/{{ project_slug }}/badge/?style=flat)](https://readthedocs.org/projects/{{ project_slug|replace('.', '') }})
{%- if cookiecutter.travis|lower == 'yes' %}
[![Travis-CI Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ project_slug }})
{%- endif %}
{%- if cookiecutter.appveyor|lower == 'yes' %}
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/{{ cookiecutter.github_username }}/{{ project_slug }}?branch=master&svg=true)](https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ project_slug }})
{%- endif %}
{%- if cookiecutter.requiresio|lower == 'yes' %}
[![Requirements Status](https://requires.io/github/{{ cookiecutter.github_username }}/{{ project_slug }}/requirements.svg?branch=master)](https://requires.io/github/{{ cookiecutter.github_username }}/{{ project_slug }}/requirements/?branch=master)
{%- endif %}
{%- if cookiecutter.coveralls|lower == 'yes' %}
[![Coveralls Status](https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ project_slug }}/badge.svg?branch=master&service=github)](https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ project_slug }})
{%- endif %}
{%- if cookiecutter.codecov|lower == 'yes' %}
[![Codecov Status](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ project_slug }})
{%- endif %}
{%- if cookiecutter.landscape|lower == 'yes' %}
[![Landscape Status](https://landscape.io/github/{{ cookiecutter.github_username }}/{{ project_slug }}/master/landscape.svg?style=flat)](https://landscape.io/github/{{ cookiecutter.github_username }}/{{ project_slug }}/master)
{%- endif %}
{%- if cookiecutter.codacy|lower == 'yes' %}
[![Codacy Status](https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat)](https://www.codacy.com/app/{{ cookiecutter.github_username }}/{{ project_slug }})
{%- endif %}
{%- if cookiecutter.codeclimate|lower == 'yes' %}
[![CodeClimate Status](https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ project_slug }}/badges/gpa.svg)](https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ project_slug }})
{%- endif %}
[![PyPI Package Latest Release](https://img.shields.io/pypi/v/{{ project_slug }}.svg?style=flat)](https://pypi.python.org/pypi/{{ project_slug }})
[![PyPI Package monthly downloads](https://img.shields.io/pypi/dm/{{ project_slug }}.svg?style=flat)](https://pypi.python.org/pypi/{{ project_slug }})
[![PyPI Wheel](https://img.shields.io/pypi/wheel/{{ project_slug }}.svg?style=flat)](https://pypi.python.org/pypi/{{ project_slug }})
[![PyPI Supported versions](https://img.shields.io/pypi/pyversions/{{ project_slug }}.svg?style=flat)](https://pypi.python.org/pypi/{{ project_slug }})
[![PyPI Supported implementations](https://img.shields.io/pypi/implementation/{{ project_slug }}.svg?style=flat)](https://pypi.python.org/pypi/{{ project_slug }})
{%- if cookiecutter.scrutinizer|lower == 'yes' %}
[![Scrutinizer Status](https://img.shields.io/scrutinizer/g/{{ cookiecutter.github_username }}/{{ project_slug }}/master.svg?style=flat)](https://scrutinizer-ci.com/g/{{ cookiecutter.github_username }}/{{ project_slug }}/)
{%- endif %}

# {{ cookiecutter.project_name }}

## Overview

{{ cookiecutter.project_short_description|wordwrap(79) }}

{%- if is_open_source %}

*   Free software: {{ cookiecutter.open_source_license }}
{%- endif %}

## Installation

```bash
pip install {{ project_slug }}
```

## Documentation

<https://{{ project_slug|replace('.', '') }}.readthedocs.io/>

## Development

To run the all tests run::

```bash
tox
```

Note, to combine the coverage data from all the tox environments run:

*   Windows

```bash
set PYTEST_ADDOPTS=--cov-append
tox
```

*   Other

```bash
PYTEST_ADDOPTS=--cov-append tox
```
