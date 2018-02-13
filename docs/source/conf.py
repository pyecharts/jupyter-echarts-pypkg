# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Echarts pypi packages for jupyter and python' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'jupyter-echarts-pypkg'
copyright = u'2018 C.W.'
version = '0.0.6'
release = '0.0.6'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'jupyter-echarts-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'jupyter-echarts-pypkg.tex',
     'jupyter-echarts-pypkg Documentation',
     'C.W.', 'manual'),
]
man_pages = [
    ('index', 'jupyter-echarts-pypkg',
     'jupyter-echarts-pypkg Documentation',
     [u'C.W.'], 1)
]
texinfo_documents = [
    ('index', 'jupyter-echarts-pypkg',
     'jupyter-echarts-pypkg Documentation',
     'C.W.', 'jupyter-echarts-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
