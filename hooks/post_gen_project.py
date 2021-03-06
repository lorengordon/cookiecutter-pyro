{% set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') %}
from __future__ import print_function

import datetime
import os
import shutil
import subprocess
import sys
from os.path import join

try:
    from click.termui import secho
except ImportError:
    warn = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)


{% if cookiecutter.test_matrix_configurator|lower == "yes" %}
    print("""
################################################################################

    For your convenience, the test environments are getting configured for the
    first time, as you have selected "yes" for `test_matrix_configurator` ...
""")
    try:
        subprocess.check_call(['tox'])
    except Exception:
        try:
            subprocess.check_call([sys.executable, '-mtox'])
        except Exception:
            subprocess.check_call([sys.executable, join('ci', 'bootstrap.py')])
{% endif %}

{%- if cookiecutter.command_line_interface|lower == 'no' %}
    os.unlink(join('src', '{{ project_slug }}', '__main__.py'))
    os.unlink(join('src', '{{ project_slug }}', 'cli.py'))
{% endif %}

{%- if cookiecutter.test_matrix_configurator|lower == 'no' %}
    os.unlink(join('ci', 'templates', 'tox.ini'))
{% endif %}

{%- if cookiecutter.appveyor|lower == 'no' %}
    os.unlink(join('ci', 'appveyor-bootstrap.py'))
    os.unlink(join('ci', 'appveyor-download.py'))
    os.unlink(join('ci', 'appveyor-with-compiler.cmd'))
    os.unlink('appveyor.yml')
    if os.path.exists(join('ci', 'templates', 'appveyor.yml')):
        os.unlink(join('ci', 'templates', 'appveyor.yml'))
{% endif %}

{%- if cookiecutter.travis|lower == 'no' %}
    os.unlink('.travis.yml')
    if os.path.exists(join('ci', 'templates', '.travis.yml')):
        os.unlink(join('ci', 'templates', '.travis.yml'))
{% endif %}

    print("""
################################################################################
################################################################################

    You have succesfully created `{{ project_slug }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

################################################################################

    To get started run these:

        cd {{ project_slug }}
{%- if cookiecutter.pypi_deploy_with_travis|lower == "yes" %}
        python ci/travis_pypi_setup.py
{%- endif %}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ project_slug }}.git
        git push -u origin master

{% if cookiecutter.test_matrix_configurator|lower == "yes" %}
    To reconfigure your test/CI settings run:

        tox -e bootstrap

    You can also run:

        ci/bootstrap.py
{% else %}
    The project doesn't use the test matrix configurator, but in case
    you change your mind just edit `setup.cfg` and run `ci/bootstrap.py`.
{% endif %}
""")

    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ project_slug }}':
            warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      WARNING:                                                              !!
!!                                                                            !!
!!          Your result package is broken. Your bin script named              !!
!!          {0} !!
!!                                                                            !!
!!          Python automatically adds the location of scripts to              !!
!!          `sys.path`. Because of that, the bin script will fail             !!
!!          to import your package because it has the same name               !!
!!          (it will try to import itself as a module).                       !!
!!                                                                            !!
!!          To avoid this problem you have two options:                       !!
!!                                                                            !!
!!          * Remove the ".py" suffix from the `command_line_interface_bin_name`.                    !!
!!                                                                            !!
!!          * Use a different `project_slug` {1} !!
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""".format(
                '"{{ cookiecutter.command_line_interface_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(command_line_interface_bin_name).ljust(32)))
        break
