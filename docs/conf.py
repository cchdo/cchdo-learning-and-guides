# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CCHDO Learn'
copyright = '2024, CCHDO Staff'
author = 'CCHDO Staff'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #"myst_parser", // myst_nb includes this automatically
    "sphinx_design",
    "myst_nb",
]

myst_enable_extensions = [
    "fieldlist",
    "dollarmath",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Just include the notebooks as is
jupyter_execute_notebooks = "off"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "logo": {
        "text": "CCHDO Learning Center",
        "image_light": "_static/logo_cchdo.svg",
        "image_dark": "_static/logo_cchdo.svg",
    },
    "collapse_navigation": True
}
