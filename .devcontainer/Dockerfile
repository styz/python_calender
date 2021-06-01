# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.177.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ARG HTTP_PROXY=""
ARG HTTPS_PROXY=""
ENV http_proxy "${HTTP_PROXY}"
ENV https_proxy "${HTTPS_PROXY}"

# [Option] Install Node.js
ARG INSTALL_NODE="true"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
COPY inline_svg/ /tmp/pip-tmp/inline_svg/
RUN /usr/local/bin/python -m pip install --upgrade pip \
    && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && cd /tmp/pip-tmp/inline_svg/ && /usr/local/bin/python setup.py bdist_wheel \
    && pip3 install dist/mkdocs_inline_svg-0.0.1-py3-none-any.whl \
    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends fonts-vlgothic locales default-jre \
    && sed -i -E 's/# (ja_JP.UTF-8)/\1/' /etc/locale.gen \
    && locale-gen

# install wkhtmltox
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb \
    && apt -y install ./wkhtmltox_0.12.6-1.buster_amd64.deb \
    && rm -f ./wkhtmltox_0.12.6-1.buster_amd64.deb

# install PlantUml
COPY bin/plantuml /usr/local/bin/plantuml
RUN mkdir /opt/plantuml \
    && wget http://sourceforge.net/projects/plantuml/files/plantuml.1.2021.7.jar/download -O /opt/plantuml/plantuml.jar \
    && chmod 755 /opt/plantuml/plantuml.jar \
    && chmod 755 /usr/local/bin/plantuml

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1