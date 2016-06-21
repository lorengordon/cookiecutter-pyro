{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will
  cause problems: the code will get executed twice:

  - When you run `python -m{{project_slug}}` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``{{project_slug}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``{{project_slug}}.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- elif cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- else %}
import sys
{%- endif %}


{% if cookiecutter.command_line_interface|lower == 'click' -%}
@click.command()
@click.argument('names', nargs=-1)
def main(names):
    """Main CLI entry point."""
    click.echo(repr(names))
{%- elif cookiecutter.command_line_interface|lower == 'argparse' -%}
parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None):
    """Main CLI entry point."""
    args = parser.parse_args(args=args)
    print(args.names)
{%- else -%}
def main(argv=sys.argv):
    """
    Main CLI entry point.

    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    print(argv)
    return 0
{%- endif %}
