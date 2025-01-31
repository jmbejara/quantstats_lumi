"""Run or update the project. This file uses the `doit` Python package. It works
like a Makefile, but is Python-based

"""

#######################################
## Configuration and Helpers for PyDoit
#######################################
## Make sure the src folder is in the path
import sys

sys.path.insert(1, "./src/")

import shutil
from os import environ, getcwd, path
from pathlib import Path
# from settings import config

# BASE_DIR = config("BASE_DIR")
# DATA_DIR = config("DATA_DIR")
# OUTPUT_DIR = config("OUTPUT_DIR")

##################################
## Begin rest of PyDoit tasks here
##################################


# ###############################################################
# ## Sphinx documentation
# ###############################################################


def task_compile_sphinx_docs():
    """Compile Sphinx Docs"""

    return {
        "actions": [
            "sphinx-build -M html ./docs_src/ ./_docs/_build",
        ],  # Use docs as build destination
        # "actions": ["sphinx-build -M html ./docs/ ./docs/_build"], # Previous standard organization
        "targets": [
            "./_docs/_build/html/index.html",
        ],
        "file_dep": [
            "./docs_src/conf.py",
            "./docs_src/index.md",
            "./docs_src/myst_markdown_demos.md",
        ],
        "clean": True,
    }
