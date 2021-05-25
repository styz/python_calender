# generate year calender by Python

## Usage
```bash
python cal.py
```

## TODO
1. Display holidays. Now, I'm tentatively displaying a circle on Sunday, but I want to display a circle on a holiday.
2. Get holidays data from `https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv`.

## 実装ポイント
- ファイル出力
- ライブラリのクラス継承
- 画像操作
- 画像のトリム
- スクレイピング(最も簡単なWebからのcsvダウンロード)
- データ処理(csv)

## 実験
- Intel oneMKLでコンパイルしたnumpyなどのライブラリを自力インストールする。Anacondaを利用しない（商用利用が禁止された？）
- 速度実験（上記の環境とそれ以外、AMD CPUとIntel CPU）

