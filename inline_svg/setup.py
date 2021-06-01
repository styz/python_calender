# setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='mkdocs-inline-svg',
    version='0.0.1',
    description='A MkDocs plugin that inlines SVG images into the output.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='mkdocs inline svg',
    url='',
    author='Yuji Sato',
    author_email='styzjade@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
        'scour'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'inline-svg = inlinesvg.plugin:InlineSvgPlugin',
        ],
        'console_scripts': [
            'inlinesvg = inlinesvg:main',
        ],
    }
)
