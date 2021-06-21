# Reusable ML engine code for JX_press

JX通信者のML・機械学習エンジニアのために、コードのテンプレートを作成しました。よければお使いください。
テンプレートを用いることで、機械学習エンジニアのコードの書き方の統一性を産み、可読性を上昇させることが狙いです。

[Pytorch lightning](https://www.pytorchlightning.ai/)をもとに作成しました

# How to use
## set up
poetryで実行環境を構築しています。

0. Poetry をインストールしていない場合、インストール
1. 以下のコマンドで実行環境を初期化

`poetry install`

## code tree
このレポジトリはwtfmlのフォルダを中心に以下のように構成されている

<pre>
wtfml
├── cross_validation # cross validationのためにデータを分割するためのフォルダ
│   └── fold_generator.py
│
├── data_loaders # DatasetとDataloaderを記述するフォルダ
│   ├── image
│   ├── nlp
│   └── tabular
│      
├── engine # AIアーキテクチャとPytorch lightning Moduleの形式を記述するフォルダ
│   ├── image
│   ├── nlp
│   └── tabular
│ 
├── pre_treatment # データの前処理を行うフォルダ
│   ├── image
│   ├── nlp
│   └── tabular
│ 
└── utils # 便利系コードを記述するフォルダ
    └── utils.py
</pre>

## わからないこと
なにかわからないことがあったら、ヨンテに連絡してください
まだ未実装な部分も多く、これから埋めて行ければと思います。
仕事で実装した方いらっしゃったらそこ埋めたいと思うので、ご連絡ください。

## ref : WTFML: Well That's Fantastic Machine Learning
pronounced as: w-t-f-m-l
このレポジトリは[WTFML](https://github.com/abhishekkrthakur/wtfml)をもとにYongtaePytorch lightningに書き換え作成した
