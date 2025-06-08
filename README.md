<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=plastic">
  <img src="https://img.shields.io/badge/-Html5-E34F26.svg?logo=html5&style=plastic">
  <img src="https://img.shields.io/badge/-Css3-1572B6.svg?logo=css3&style=plastic">
  <img src="https://img.shields.io/badge/-Javascript-F7DF1E.svg?logo=javascript&style=plastic">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [スクリーンショット](#スクリーンショット)
3. [主な機能](#主な機能)
4. [環境](#環境)
5. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [Django コマンド一覧](#Django コマンド一覧)

<!-- READMEの作成方法のドキュメントのリンク -->
<br />
<div align="right">
    <a href="READMEの作成方法のリンク"><strong>READMEの作成方法 »</strong></a>
</div>
<br />
<!-- Dockerfileのドキュメントのリンク -->
<div align="right">
    <a href="Dockerfileの詳細リンク"><strong>Dockerfileの詳細 »</strong></a>
</div>
<br />
<!-- プロジェクト名を記載 -->

## プロジェクト名
### Standup-Timer

<!-- プロジェクトについて -->
## プロジェクトについて

このアプリは、**座りすぎを防止する作業用ポモドーロタイマー**と、**作業記録管理機能**を備えたWebアプリです。

ポモドーロタイマーとは、**25分間の作業と5分間の休憩**を繰り返すことで集中力を高める時間管理術です。  
本アプリでは、5分間の休憩時間に「立ち上がるよう促す通知」を表示することで、長時間の座りすぎを防ぎます。

作業ごとに以下の情報を記録できます：
- カテゴリ
- タイトル
- メモ

記録した作業は、**日別の作業量**や**カテゴリ別の時間配分**としてグラフで可視化できます。  
学習や仕事の振り返り・習慣化に活用できるツールです。


## 主な機能

### 1. 認証機能
- ユーザー登録（ユーザーID・パスワード）
- ログイン / ログアウト（認証済みユーザーのみが利用可能）

---

### 2. タイマー機能
- 学習カテゴリ・タイトルを選択し、作業タイマーを開始
- 作業時間を自由に設定可能
- 25分以上作業が続いた場合、5分休憩と立ち上がり促進のアラートを表示（ポモドーロ風）

---

### 3. 作業記録機能
- 記録される内容：
  - カテゴリ
  - タイトル
  - メモ
  - 開始時刻
  - 作業時間
  - 詳細表示（個別ページ）

- 作業記録の編集・削除が可能：
  - タイトル・メモを編集
  - 不要な作業記録を削除

---

### 4. 📊 統計・グラフ機能
- 日ごとの作業時間を棒グラフで表示
- カテゴリ別の学習時間の割合を円グラフで表示

---

### 5. 🗂 カテゴリ・タイトル管理
- カテゴリの追加・削除
- タイトルの追加・削除

ユーザーごとに自由に学習項目をカスタマイズ可能


## スクリーンショット
- タイマー画面
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/360859b4-3f3c-4743-bb8c-a2505cdd14cf" />

- 作業記録画面
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/46770450-8782-47f3-9237-ea4a0d480d0f" />

- 統計画面
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/90d8047a-4fcf-4895-b85e-71f7a9ecc7a6" />

- カテゴリ・タイトル管理画面
<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/9359bd7a-491f-494a-be8f-37f8e3b84f8e" />


## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.13.0     |
| Django                | 5.1.4      |

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

<!-- Treeコマンドを使ってディレクトリ構成を記載 -->

tree -a -I "node_modules|.next|.git|.pytest_cache|static" -L 2
.
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── staticfiles
│   ├── admin
│   └── timer
├── templates
│   ├── base.html
│   └── registration
├── timer
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── plugin_plotly.py
│   ├── static
│   ├── templates
│   ├── templatetags
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── timerproject
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

### 仮想環境の作成

以下のコマンドで仮想環境を作成

python3 -m venv venv

以下のコマンドで仮想環境を立ち上げる

source venv/bin/activate

### 動作確認

以下のコマンドでプロジェクトに移動

cd timerproject

以下のコマンドでサーバーを起動

python3 manage.py runserver

http://127.0.0.1:8000/ にアクセスできるか確認
アクセスできたら成功

### サーバーの停止

以下のコマンドでサーバーを停止することができます

ctrl + c


## Django コマンド一覧

###プロジェクト・アプリ作成

| コマンド | 説明 |
|----------|------|
| `django-admin startproject プロジェクト名` | 新しいDjangoプロジェクトを作成 |
| `python manage.py startapp アプリ名` | 新しいアプリを作成 |

---

###サーバー実行・確認

| コマンド | 説明 |
|----------|------|
| `python manage.py runserver` | 開発サーバーを起動（http://127.0.0.1:8000） |
| `python manage.py runserver 0.0.0.0:8000` | 外部アクセス可能なサーバーを起動 |

---

###データベース関連

| コマンド | 説明 |
|----------|------|
| `python manage.py makemigrations` | モデルの変更をマイグレーションファイルに変換 |
| `python manage.py migrate` | マイグレーションファイルをデータベースに適用 |

---

###ユーザーと管理画面

| コマンド | 説明 |
|----------|------|
| `python manage.py createsuperuser` | 管理画面用のスーパーユーザーを作成 |

---

###その他便利なコマンド

| コマンド | 説明 |
|----------|------|
| `python manage.py test` | 単体テストを実行 |
| `python manage.py collectstatic` | 静的ファイルをまとめる（本番用） |
| `python manage.py check` | 設定ファイルの問題をチェック |
| `python manage.py help` | 使用可能なコマンド一覧を表示 |

---

<p align="right">(<a href="#top">トップへ</a>)</p>
