{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
# Usage

To use {{ cookiecutter.project_name }} in a project::

```python
import {{ project_slug }}
```
