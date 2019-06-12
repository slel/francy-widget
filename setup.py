# --*- encoding: utf-8 -*--
# from __future__ import print_function
from setuptools import setup
from codecs import open  # To open the README file with proper encoding


# Get information from separate files (README, VERSION)
def readfile(filename):
    with open(filename,  encoding='utf-8') as f:
        return f.read()


setup_args = {
    'name': 'francy-widget',
    'version': readfile("VERSION"),
    'description': 'Francy Widget for representing graphs',
    'long_description': readfile("README.rst"),
    'include_package_data': True,
    'data_files': [],
    'url': 'https://github.com/zerline/francy-widget',
    'author': 'Odile Bénassy',
    'author_email': 'odile.benassy@u-psud.fr',
    'license': 'GPLv3+',
    'classifiers': [
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'Topic :: Scientific/Engineering :: Mathematics',
      'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
      'Programming Language :: Python :: 2.7',
    ],  # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'keywords': ['jupyter', 'widget', 'graph', 'francy'],
    'packages': ['francy_widget'],
    'zip_safe': False,
    'install_requires': ['pip', 'ipywidgets>=7.0.0', 'networkx', 'jupyter-francy', 'Sphinx']
}

setup(**setup_args)
