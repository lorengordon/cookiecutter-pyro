{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
# {{ project_slug }}

## Testing

```python
import {{ project_slug }}
```

## Modules
