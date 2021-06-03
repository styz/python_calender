# TODO

## embedded SVG to inline SVG plugin
<!-- inline SVG refs. -->
https://qiita.com/propella/items/803923b2ff02482242cd
https://github.com/scour-project/scour/blob/master/scour/scour.py
https://gitlab.com/craig0990/mkdocs-plugin-inline-svg
https://vecta.io/blog/best-way-to-embed-svg#comparison
<!-- publish plugin -->
https://qiita.com/shinichi-takii/items/e90dcf7550ef13b047b5


```bash
# build & install
cd inline_svg
python setup.py clean --all
python setup.py bdist_wheel
pip uninstall mkdocs-inline-svg
pip install dist/mkdocs_inline_svg-0.0.1-py3-none-any.whl

# 開発用のローカルbuild and install
# pip install -e .
```

## 環境
### proxy
`~/.docker/config`

### ssh
`~/.ssh/config`
`${env:ProgramData}/ssh/sshd_config`

### remote docker host
docker contextの登録・切り替え
