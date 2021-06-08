# TODO

## markdown embedded SVG to inline SVG plugin
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

## setting for proxy/remote env
### proxy
`~/.docker/config`

### ssh
- server
  - sshd
    https://www.robata.org/docs/ad/network/config_sshd-01.html
    `C:\windows\system32\OpenSSH\sshd_default_config`から`${env:ProgramData}/ssh/sshd_config`を作成。
    公開鍵認証on、パスワード認証off、チャレンジレスポンス認証off、ファイル末の数行管理者用公開鍵の設定をコメントアウト。
  - ssh-keygen
    https://hackers-high.com/linux/easy-ssh-publickey-authentication/
- client
  - ssh-agent
  - ssh-add
    秘密鍵登録

### remote docker host
https://qiita.com/74th/items/2ccfc07bd279aba610b1
- docker contextの登録・切り替え
    ```
    docker context create <context_name> --docker 'host=ssh://<user>@<host>:<port>'
    docker context use <context_name>
    ```

- VSCode上の設定
  DockerおよびRemote-Containers extentionsで利用するDocker接続先設定。
    setting.json
    ```json
    {
        "docker.context": "<context_name>",
        "docker.host": "ssh://<user>@<host>:<port>",
    }
    ```


## Docker in Docker(dind)

## Docker outside of Docker(DooD)
https://www.nullpo.io/2020/05/27/docker-dood-volume/
- Docker CLIインストール
- docker.sockマウント
    非rootの場合は権限付与

## mkdocs 1.2 にlivereloadが動かないバグ
https://github.com/mkdocs/mkdocs/issues/2448