# Python Development Environment on **devcontainer**

VSCode workspace settings and Container Image for Python.
- Includes markdown builder/viewer and graph drawing tools.
- Includes major `pip` modules(numpy, pandas, matplotlib...etc)

[Anaconda](https://www.anaconda.com/) is not free for commercial use since 2020-4-30[^1].
I want to build and install pip modules, like Anaconda environment.

[^1]: https://www.anaconda.com/blog/sustaining-our-stewardship-of-the-open-source-data-science-community

## Features
1.  Python Environment

    devcontainer.json and Dockerfile for building Python Container Image.

2.  Documentation Environment

    Setting up MkDocs for Markdown writing and building.

3.  Drawing Environment

    Setting up drawing tools(Draw.io, Mermaid.js, PlantUML, Graphviz).
    A graph images created by these tools can be embedded in Markdown as **inline SVG**.
    **inline SVG**'s elements can be seached on the browser.

## Recommended system requirements
- Windows10: Version 20H2
  - VSCode: VSCode v1.56.2
    - Remote-Container extention: Extention ID is `ms-vscode-remote.remote-containers`
- Docker: Docker Desktop 3.3.3, Docker Engine v20.10.6

## Usage
1. Clone or copy this repository.
2. Open VSCode.
3. Press keys ++ctrl+shift+p++ and select `Remote-Containers: Open Workspace in Container`.
4. Select workspace file `devenv.code-workspace`.
5. VSCode build and attach container. You develop `docs/` or `src/` in this container.
6. Press keys ++f5++, documents are built and opened in Chrome[^2].
7. Press keys ++shift+f5++, close PWA Chrome.

[^2]: Debugging on Progressive Web Apps(PWA) Chrome that auto reload documents.

## Note
none.

## Author
* Author: Yuji Sato
* E-mail: styzjade@gmail.com

## License
MIT License.

# Version
{% include "version.md" %}