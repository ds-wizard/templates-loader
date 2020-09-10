from setuptools import setup

setup(
    name='dsw_template_loader',
    version='0.1',
    description='A simple tool for uploading DSW templates',
    author='Marek Suchánek',
    author_email='marek.suchanek@fit.cvut.cz',
    license='Apache License 2.0',
    url='https://github.com/ds-wizard/templates-loader',
    py_modules=['templates_loader'],
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'dsw_template_loader = templates_loader:cli',
        ],
    },
)
