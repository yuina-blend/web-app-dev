# web-app-dev
webアプリ開発実験

# webアプリ開発

## 第一回

## テーマ案

### 1. 掲示板

投稿機能、複数人が書き込み可能

### 2. 二進→十進変換のやつ

これ↓

https://hogehoge.tk/tool/number.html

### 3. 画像処理

1.アップロードした画像を反転、縮小とか文字入れたりする。

→画像をアップロードして、オプション選択（反転・縮小率など）→画像生成

2.文字画像ジェネレーターとか

→テキストBOXに生成する文字、フォントとかを選べるといいかも→画像生成

↓

OpenCVにまんまその機能がるから、バックがPython(OpenCV)で動けばできそう(Flask+OpenCV？)


現状3の画像処理がテーマとしていいんじゃないかという話になってる

あとは技術的なことを考慮してテーマ決定したい

## 第二回

文字画像ジェネレータをつくる

## 役割分担

フロントとバックで分ける

フロント : 野口、武井

バック : 南(Flaskでフロントと連携)、弘中(画像生成機能)

## 機能詳細等

### 欲しい情報

- つくる文字（テキストボックス）
- フォント（選択式）
- 色（選択式）
- サイズ（文字）
- サイズ（画像全体）

### Webの見た目の概形

