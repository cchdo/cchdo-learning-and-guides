# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CCHDO Learn'
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
    "attrs_block",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Just include the notebooks as is
jupyter_execute_notebooks = "off"

# Automatically number any captioned figures, tables, and code blocks
numfig = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "logo": {
        "text": "CCHDO Documentation",
        "image_light": "_static/logo_cchdo.svg",
        "image_dark": "_static/logo_cchdo.svg",
    },
    "collapse_navigation": True,
    # Add Google Analytics
    "analytics": {
        "google_analytics_id": "G-89QCC25DF0",
    }
}


def setup(app):
    cloudflare = """(function(d) {
    script = d.createElement('script');
    script.type = 'text/javascript';
    script.defer = true;
    script.setAttribute("data-cf-beacon", '{"token": "de10da1edc5240c2a8b7948472ec5417"}')
    script.src = 'https://static.cloudflareinsights.com/beacon.min.js';
    d.getElementsByTagName('head')[0].appendChild(script);
}(document));
"""
    app.add_js_file(None, body=cloudflare)