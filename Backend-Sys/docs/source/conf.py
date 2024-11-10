import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import django

# Load environment variables from a .env file
load_dotenv()

# Add the base directory of your Django project to the system path
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Adjust this if necessary
sys.path.insert(0, str(BASE_DIR))  # Add the project root to the path

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'  # Adjust this as needed

# Import Django and set up the environment
django.setup()

# -- Project information -----------------------------------------------------
project = 'Datashield Solutions'
copyright = '2024, Susan Gicheru'
author = 'Susan Gicheru'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']