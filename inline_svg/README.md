# mkdocs-inline-svg

> Reads SVG images referenced from Markdown and replaces them with the SVG
> file content

> Since the SVG is included as part of the plain-text input to MkDocs, this means
> the default MkDocs search supports searching SVG text, and hyperlinks are also
> fully functional.

In addition to this, optimizes SVF file content for HTML.

## Usage

Install the package with pip:

`pip install mkdocs-inline-svg`

Enable the plugin in your mkdocs.yml:

```
plugins:
    - inline-svg
```

## Credits
I have borrowed inspiration from:

* https://gitlab.com/craig0990/mkdocs-plugin-inline-svg
