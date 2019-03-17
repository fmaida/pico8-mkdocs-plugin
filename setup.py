from setuptools import setup

setup(
    name='Pico-8',
    version='1.0.0',
    packages=['pico8'],
    url='https://github.com/fmaida/pico8-mkdocs-plugin',
    license='MIT',
    author='Francesco Maida',
    author_email='fran@cesco.it',
    description='This plugin allows to embed a Pico-8 web player in a mkdocs generated page.',
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
