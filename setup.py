from setuptools import setup

# read the contents of markdown README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='grbpy',
    url='https://github.com/gamma-ray-burst/grbpy',
    author='Thomas Cannon',
    author_email='cannontw@g.cofc.edu',
    packages=['grbpy'],
    install_requires=['numpy>=1.17.0rc2'],
    version='0.1',
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=long_description,
    long_description_content_type='text/markdown',
)