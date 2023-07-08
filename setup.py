from setuptools import setup, find_packages

setup(
    name='SudReg',
    version='1.0.0',
    url='https://github.com/0xe20x8d0xbc/sudreg',
    author='Your Name',
    author_email='0xe20x8d0xbc@gmail.com',
    description='A light weight Python library for the SudReg Web API',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
)
