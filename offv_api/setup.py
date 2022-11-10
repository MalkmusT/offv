from setuptools import find_packages, setup

setup(
    name='offv_api',
    version='1.0.0',
    packages= ["offv_api"], 
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

