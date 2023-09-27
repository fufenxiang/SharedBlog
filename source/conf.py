# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import datetime

current_year = datetime.datetime.now().year

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SharedBlog'
copyright = u'2023 - {}, Flora'.format(current_year)
author = 'Flora'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # markdown 格式文档支持
    'recommonmark',
    # markdown 表格支持
    'sphinx_markdown_tables',
    # 多版本文档支持
    "sphinx_multiversion",
]

templates_path = ['_templates']
html_sidebars = {
    '**': [
        'version.html',
    ],
}
# html_static_path = ["_static"]
# html_css_files = [
#     'css/custom.css',
# ]
# html_style = 'css/custom.css'
# html_logo = '_static/imgs/logo.PNG'

exclude_patterns = []


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'classic'
html_theme = 'agogo'
# html_theme = 'bizstyle'
# html_theme = 'sphinx_rtd_theme'
