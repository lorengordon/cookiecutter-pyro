{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
# Installation

At the command line::

```bash
pip install {{ project_slug }}
```
