"""
This file provides standard information to
help with debugging.

This file is named:   about.py
This module is named: about

It uses a built-in attribute representing the file name:

    print(get_header(__file__))

To learn more, search:

    builtin attributes python

"""

# imports (all of these are from the standard library)

import datetime
from inspect import iscode
import os
import platform
import sys

# declare program constants
# sometimes, data is kept in a folder named 'data'
# in this repo, data is in the same directory as the source code

data_folder = ""
divider = "=============================================================="

# define helper functions


def get_source_directory_path():
    """Returns the absolute path to this source directory."""
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def get_data_directory_path():
    """Returns the absolute path to the data directory."""
    datapath = os.sep.join([os.getcwd(), data_folder])
    return datapath


def get_data_file_path(fn):
    """Return the absolute path to a data file given the file name (fn)."""
    dir = get_data_directory_path()
    fullPath = os.sep.join([dir, fn])
    return fullPath


def get_header(fn):
    """This function prints helpful information about a file."""
    return f"""

{divider}
{divider}

 Welcome!

 It's (January 24 2023) at (20.00 hours)

 This file is running on:    () (Microsoft)
 
 The Python version is:     (VScode.python_version 3.10.9)
 
 The Python interpreter is at: 
 

 The active environment should be either conda OR pip (one should be None):

     Active conda env is: (os.environ.get('CONDA_DEFAULT_ENV'))
     Active pip env is:   (os.environ.get('PIP_DEFAULT_ENV')
 
 The path to the active virtual environment is:

 (conda 23.1.0)
 
 The Current Working Directory (CWD) where this command was launched is:

 {sys.VScode}
 
 The absolute path to the data directory is:

 (https://github.com/anythonyschomer/datafun-01-getting-started)
 
 The absolute path to this source directory is:

 (https://github.com/denisecase/datafun-01-getting-started)
 
 The absolute path to this file is:

 (https://github.com/denisecase/datafun-01-getting-started)
 
{divider}
{divider}

"""


# -------------------------------------------------------------
# Call some functions and execute code!

# Call our print_header() function on this file to test it
# Python provides a built-in attribute representing the file name
# two underscores on each side of the word 'file'
print(get_header(__file__))

print_to_file = True

if print_to_file:
    # print to a file named about.txt
    fn = "about.txt"
    with open(fn, "w") as f:
        f.write(get_header(__file__))
