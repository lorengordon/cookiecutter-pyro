{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
{%- if cookiecutter.command_line_interface|lower == 'click' -%}
from click.testing import CliRunner

from {{ project_slug }}.cli import main
{%- elif cookiecutter.command_line_interface|lower in ['plain', 'argparse'] -%}
from {{ project_slug }}.cli import main
{%- endif %}
{%- if cookiecutter.test_matrix_configurator|lower == 'yes' and cookiecutter.test_matrix_configurator|lower == 'no' or
       cookiecutter.command_line_interface == 'no' %}
import {{ project_slug }}
{%- endif %}


def test_main():
{%- if cookiecutter.test_matrix_configurator|lower == 'yes' and cookiecutter.test_matrix_configurator|lower == 'no' %}
    assert 'site-packages' in {{ project_slug }}.__file__
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface|lower == 'argparse' %}
    main([])
{%- elif cookiecutter.command_line_interface|lower == 'plain' %}
    assert main([]) == 0
{%- else %}
    assert {{ project_slug }}  # use your library here
{%- endif %}
