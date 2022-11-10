# -*- coding: utf-8 -*-

from setuptools import setup
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_requierements():
    with open( os.path.join( dir_path, "api", "requirements.pip") ) as f:
        return [ x.strip() for x in f.readlines()]

setup(
    name="offv",
    version="1.0.0",
    packages=[ "api" ], 
    include_package_data=True,
    install_requires=[
        get_requierements()
    ],
)

