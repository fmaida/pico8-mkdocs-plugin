from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pico8-mkdocs-plugin',
    version='1.0.0',
    packages=['pico8'],
    url='https://github.com/fmaida/pico8-mkdocs-plugin',
    license='MIT',
    author='Francesco Maida',
    author_email='francesco.maida@gmail.com',
    description='This plugin allows to embed a Pico-8 web player in a mkdocs generated page.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'pico-8 = pico8:Pico8',
        ]
    },
)
