from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SudReg',
    version='1.0.1',
    url='https://github.com/0xe20x8d0xbc/sudreg',
    author='Your Name',
    author_email='0xe20x8d0xbc@gmail.com',
    description='A light weight Python library for the SudReg Web API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    keywords='Sudski Registar, Sudski Registar API'
)
