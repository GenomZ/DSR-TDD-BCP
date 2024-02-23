import os
import sys

project = "test"
copyright = "me"
author = "also me"
release = "v0.0.1"

sys.path.insert(0, os.path.abspath('../src'))

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
]

autosummary_generate = True

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ['_static']
