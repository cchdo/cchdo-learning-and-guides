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
html_show_sourcelink = False

html_theme_options = {
    "logo": {
        "text": "CCHDO Documentation",
        "image_light": "_static/logo_cchdo.svg",
        "image_dark": "_static/logo_cchdo.svg",
    },
    "collapse_navigation": True,
    "external_links": [
        {"name": "Main CCHDO Site", "url": "https://cchdo.ucsd.edu"}  # Add this external link for the main site
    ],
    # Add Google Analytics
    "analytics": {
        "google_analytics_id": "G-89QCC25DF0",
    }
}

html_css_files = [
    'custom.css',
]

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

    posthog = """!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('phc_P0sqR6YbfFxHaBQ9RWdAxJbXHdSn7P4OhZj28migeQ0',{api_host:'https://us.i.posthog.com', person_profiles: 'identified_only' // or 'always' to create profiles for anonymous users as well
        })"""
    app.add_js_file(None, body=posthog)
