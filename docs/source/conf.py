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

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxarg.ext",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "myst_parser",
]

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_keyword = True
napoleon_use_rtype = True

autodoc_default_options = {
    "members": True,
    "member-order": "groupwise",
    "undoc-members": False,
    "inherited-members": "ConfigParser",
    "show-inheritance": True,
}
autodoc_member_order = "alphabetical"
autodoc_mock_imports = [
    "fenics",
    "numpy",
    "petsc4py",
    "ufl",
    "meshio",
    "dolfin",
    "configparser",
    "h5py",
]
autodoc_typehints = "description"
autoclass_content = "both"

highlight_language = "python"

templates_path = ['_templates']

source_suffix = ".rst"
exclude_patterns = ["_build"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/sblauth/sblauth.github.io",
    "header_links_before_dropdown": 5,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": [],
    "show_nav_level": 2,
    "primary_sidebar_end": [
        "sidebar-ethical-ads",
    ],
    "logo": {"text": "Home"}
}

html_sidebars = {"**": ["search-field.html", "sidebar-nav-bs", "sidebar-ethical-ads"]}
pygments_style = "sphinx"

autosummary_generate = True
autosummary_imported_members = True

myst_enable_extensions = ["dollarmath", "colon_fence"]
html_static_path = ['_static']
