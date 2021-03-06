{%- set project_slug = cookiecutter.project_slug|lower|replace(' ','_')|replace('-','_') -%}
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
{% if cookiecutter.c_extension_support|lower == 'yes' -%}
import os
{% endif -%}
import re

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
{% if cookiecutter.c_extension_support|lower == 'yes' -%}
from os.path import relpath
{% endif -%}
from os.path import splitext
{% if cookiecutter.c_extension_support|lower == 'yes' -%}
from setuptools import Extension
{% endif -%}
from setuptools import find_packages
from setuptools import setup
{%- if cookiecutter.c_extension_support|lower == 'yes' -%}
{%- if cookiecutter.c_extension_optional|lower == 'yes' %}
from setuptools.command.build_ext import build_ext
{%- endif %}
{%- if cookiecutter.c_extension_cython|lower == 'yes' %}

try:
    # Allow installing package without any Cython available. This
    # assumes you are going to include the .c files in your sdist.
    import Cython
except ImportError:
    Cython = None
{%- endif %}
{%- endif %}


{% if cookiecutter.c_extension_support|lower == 'yes' -%}
# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
    os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']

{% if cookiecutter.c_extension_optional|lower == 'yes' %}
class optional_build_ext(build_ext):
    """Allow the building of C extensions to fail."""
    def run(self):
        try:
            build_ext.run(self)
        except Exception as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def _unavailable(self, e):
        print('*' * 80)
        print('''WARNING:

    An optional code optimization (C extension) could not be compiled.

    Optimizations for this package will not be available!
        ''')

        print('CAUSE:')
        print('')
        print('    ' + repr(e))
        print('*' * 80)

{% endif -%}
{% endif -%}

def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def find_version(*file_paths):
    # Read the version number from a source file.
    # Why read it, and not import?
    # see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
    version_file = read(*file_paths, encoding='latin1')

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

try:
    import pypandoc
    # Strip Markdown image tags from README.md and convert to rst
    long_description = '%s\n%s' % (
        re.compile('^\[!\[.*$', re.M).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.md'))
    )
    long_description = pypandoc.convert(
        long_description.lstrip('\n'),
        'rst',
        format='md')
    long_description = long_description.replace('\r\n', '\n')
except (ImportError, OSError):
    # pandoc is not installed, fallback to using raw contents
    print("WARNING: Pandoc not found. Long_description conversion failure. "
          "Do not upload this package to pypi.")
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

{%- if cookiecutter.c_extension_support|lower == 'yes' and cookiecutter.c_extension_cython|lower == 'yes' %}
setup_requires.extend(['cython'] if Cython else [])
{%- endif %}

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License'
} %}

setup(
    name='{{ project_slug }}',
    version=find_version('src', '{{ cookiecutter.project_slug }}', '__init__.py'),
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description=long_description,
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub') }},
    author_email={{ '{0!r}'.format(cookiecutter.email).lstrip('ub') }},
    url='https://github.com/{{ cookiecutter.github_username }}/{{ project_slug }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
{%- if cookiecutter.command_line_interface|lower == 'click' %}
        'click>=6.0',
{%- else %}
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
{%- endif %}
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- if cookiecutter.command_line_interface|lower != 'no' %}
    entry_points={
        'console_scripts': [
            '{{ project_slug }} = {{ project_slug }}.cli:main',
        ]
    },
{%- endif %}
{%- if cookiecutter.c_extension_support|lower == 'yes' -%}
{%- if cookiecutter.c_extension_optional|lower == 'yes' %}
    cmdclass={'build_ext': optional_build_ext},
{%- endif %}
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
            include_dirs=[dirname(path)]
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root,
{%- if cookiecutter.c_extension_cython|lower == 'yes' %} '*.pyx' if Cython else '*.c'
{%- else %} '*.c'{% endif %}))
    ],
{%- endif %}
)
