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

extensions = [
    "sphinx_copybutton",
    "sphinx_design",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_title = "Sebastian Blauth"


html_theme_options = {
    "header_links_before_dropdown": 5,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": [],
    "navbar_align": "content",
    "show_nav_level": 2,
    "logo": {"text": "Home"},
    "show_prev_next": False,
    "secondary_sidebar_items": [],
    "footer_items": ["copyright"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sblauth",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "ORCiD",
            "url": "https://orcid.org/0000-0001-9173-0866",
            "icon": "fa-brands fa-orcid",
            "type": "fontawesome",
        },
        {
            "name": "email",
            "url": "mailto:sebastian.blauth@itwm.fraunhofer.de",
            "icon": "fa-regular fa-envelope",
            "type": "fontawesome",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=M-SEAnwAAAAJ&hl=en&oi=ao",
            "icon": "fa-brands fa-google",
            "type": "fontawesome",
        },
        {
            "name": "ResearchGate",
            "url": "https://www.researchgate.net/profile/Sebastian-Blauth",
            "icon": "fa-brands fa-researchgate",
            "type": "fontawesome",
        },
    ]
}

html_sidebars = {"**": []}


pygments_style = "sphinx"

html_static_path = ['_static']
html_css_files = ["custom.css"]
