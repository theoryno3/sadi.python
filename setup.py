from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "sadi",
    version = "0.1.5",
    packages = find_packages(exclude="example.py"),

    install_requires = ['rdflib>=3.0', 'surf', 'rdfextras', 'surf.rdflib'],

    # metadata for upload to PyPI
    author = "James McCusker",
    author_email = "mccusker@gmail.com",
    description = "SADI for python.",
    license = "New BSD License",
    keywords = "Webservices SemanticWeb, RDF, Python, REST",
    url = "http://code.google.com/p/sadi/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
