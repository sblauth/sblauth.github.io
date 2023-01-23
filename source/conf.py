# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("."))

project = 'sblauth.github.io'
copyright = '2023, Sebastian Blauth'
author = 'Sebastian Blauth'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


highlight_language = "python"

templates_path = ['_templates']

source_suffix = ".rst"
exclude_patterns = ["_build"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_title = "Sebastian Blauth"

html_theme_options = {
    "github_url": "https://github.com/sblauth/sblauth.github.io",
    "header_links_before_dropdown": 5,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": [],
    "show_nav_level": 2,
    "primary_sidebar_end": [
        "sidebar-ethical-ads",
    ],
    "logo": {"text": "Home"},
    "show_prev_next": False,
}



html_sidebars = {"**": ["search-field.html", "sidebar-nav-bs", "sidebar-ethical-ads"]}


pygments_style = "sphinx"

html_static_path = ['_static']
