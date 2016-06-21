{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
"""
Entrypoint module, in case you use `python -m{{project_slug}}`.

Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
{%- if cookiecutter.command_line_interface|lower == 'plain' %}
import sys
{% endif %}
from {{project_slug}}.cli import main

if __name__ == "__main__":
{%- if cookiecutter.command_line_interface|lower == 'plain' %}
    sys.exit(main())
{%- else %}
    main()
{%- endif %}
