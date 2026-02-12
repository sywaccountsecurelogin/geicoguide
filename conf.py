# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'GEICO Contact Guide'
copyright = '2025, GEICO'
author = 'GEICO Contact Guide'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "GEICO Contact Guide – Customer Service, Claims & Billing Help"

# Optional short title (e.g., for nav bar)
html_short_title = "GEICO Contact Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (you can change it)
html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'navigation_depth': 2,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'show_relbars': True,
}

# Paths to templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

# Add custom CSS for GEICO-style colors
html_css_files = [
    'custom.css',
]

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
