import os
import sys
from typing import List

sys.path.insert(0, os.path.abspath('../src'))

from dataclass_dict.__version__ import __version__

project = 'dataclass_dict'
copyright = '2019, Leandro (Cerberus1746) Benedet Garcia'
author = 'Leandro (Cerberus1746) Benedet Garcia'
version = __version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx_autodoc_typehints'
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
master_doc = 'index'

intersphinx_mapping = {
    'python':  ('https://docs.python.org/3/', None),
}
