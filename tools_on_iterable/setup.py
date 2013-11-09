#!/usr/bin/python

from setuptools import setup
import os


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tools_on_iterable",
    version = "0.1",
    description = "Python module for handling some rare but inconvenient cases with iterables.",
    author = "Matyas Steiner",
    author_email = "steiner.matyas@gmail.com",
    url = "https://github.com/stma",
    license = "Apache license v2",
    long_description =read('README.md'),
    py_modules = ["tools_on_iterable"],
)
