# weathertalkとは

Weathertalkは、天気予報をWebAPIを用いて取得し、音声で読み上げるプログラムです。
天気予報の取得には　Livedoor Weather APIを使用し、　音声合成は AI talkを使用しています。

#使用方法
AI-Talkのユーザー名／パスワードをaitalk.py中に設定します。

python weathertalk.py


#設定
対象地域は大阪とハードコーディングされてます。(weathertalk.py)

#その他内部的な話
livedoorAPIが吐き出す天気概況文字列には、空の改行コードと半角スペースが含まれるようです
これらはAItalkで受けられませんので、削除ています



