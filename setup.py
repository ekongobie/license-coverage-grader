# SPDX-License-Identifer: Apache-2.0


from setuptools import setup


def readme():
    """Opens and reads the readme file"""
    with open('README.md') as f:
        return f.read()


setup(
    name="License Coverage Grader", # Package name
    long_description=readme(), # Package description and documentation
    version='0.1', # Package version
    py_modules=['cmds'], # Python modules installed
    author='Nuvadga Christian Tete', # Source code author
    author_email='tetechris20@gmail.com', # Source code email author
    description='SPDX Utility to grade License information', # Brief description of package
    install_requires=[
        'Click',
        'xmlbuilder',
        'Fabric',
        'lxml',
        'colorama',
        'python-Levenshtein'
    ], # Required python packages for the utility to run smoothly
    entry_points={
        'console_scripts': ['scan=cmds:scan',
                            'analyse=cmds:analyse',
                            'check=cmds:check',
                            'grade=cmds:grade'],
    } # Commands shipped with this utility
)
