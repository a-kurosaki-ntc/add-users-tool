# 使い方（Linux）

Python の venv を作成します。

```
python -m venv .venv
```

venv を activate します。

```
source .venv/bin/activate
```

依存パッケージをインストールします。

```
pip install -r requirements.txt
```

.env.example の名前を.env に変更し、.env ファイルを編集して以下を設定しておきます。

- DB_USER: DB の操作権限のある Entra User のメールアドレス
- DB_HOST: DB のホスト
- DB_NAME: DB の名前

sample_users.txt を編集して、追加したいユーザーと管理者かどうか（1:管理者、0:一般ユーザー）を設定します。
最終行で改行を行うことを忘れないでください。

azure cli でログインを行います。

```
az login
```

シェルスクリプトを実行します。

```
sh register_default_users.sh sample_users.txt
```
