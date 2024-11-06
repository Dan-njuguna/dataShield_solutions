# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Add the base directory of your Django project to the system path
BASE_DIR = Path(__file__).resolve().parent.parent  # Adjust this if necessary
sys.path.insert(0, str(BASE_DIR))

# If your Django settings module is not in the default location, set it here
# os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings' 

# Import Django and set up the environment
import django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Datashield Solutions'
copyright = '2024, Susan Gicheru'
author = 'Susan Gicheru'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',           # Automatically document from docstrings
    'sphinx.ext.viewcode',          # Include links to the source code
    'sphinx_autodoc_typehints',     # Automatically include type hints in documentation
]

templates_path = ['_templates']      # Path to templates
exclude_patterns = []                  # Patterns to exclude from the build

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'              # Choose your HTML theme
html_static_path = ['_static']         # Path for static files