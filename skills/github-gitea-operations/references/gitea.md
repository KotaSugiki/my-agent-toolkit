# Giteaの操作例

Giteaで操作する場合に参照します。接続先サーバーと、そこで利用できる認証・CLI・APIを使います。以下の手順とJSONは、このスキル向けに作成した例です。

## teaを使う場合

`tea` はGiteaのIssue・PRなどを操作する公式CLIです。複数サーバーのログイン設定には名前を付けて管理できます。[Gitea Tea（公開日不明、2026/10確認）, What is Tea? / See it in action](https://about.gitea.com/products/tea/)

```text
tea --help
tea login add --help
```

実行環境のヘルプで、次の操作と引数を確認します。バージョンによって確認する必要があるため、推測したコマンドでは作成しません。

- 接続先のログイン設定・アカウント・権限を確認します。既存の認証が使える場合は、その設定を使います。
- 対象リポジトリを指定し、既存Issue・PRを検索・取得します。
- 対象リポジトリの既存ラベルの一覧と、担当者に指定できるユーザーを確認します。
- 対象リポジトリ、タイトル、改行を維持した本文、担当者、ラベル、ブランチを明示してIssueを作成します。
- PRではpush済みの変更元と、導入先の規約・指定に従った取り込み先、担当者、ラベルを明示して作成します。
- 作成した番号やURLから本文・担当者・ラベル・ブランチなどを再取得して、依頼と照合します。

CLIが利用できない場合は、認証済み連携ツールやAPIを使えます。認証が不足している場合は、本文の準備まで進めて必要な対応を説明します。

## APIを使う場合

APIを使うときは、接続先のベースURLを確認します。例えば `https://example.com/gitea/owner/repo` なら、サブパス `/gitea` を維持してAPIのURLを組み立てます。所有者名とリポジトリ名はパス要素として適切にエンコードします。

接続先のAPI仕様は `/api/swagger`、OpenAPIの定義は `/swagger.v1.json` で確認できます。公開資料と接続先のバージョンが異なる場合は、接続先の仕様を使います。[Gitea API Usage（公開日不明、2026/10確認）, API Guide](https://docs.gitea.com/development/api-usage/#api-guide)

| 操作 | HTTPメソッドとパス | 本文の主要な項目 |
| --- | --- | --- |
| ラベル一覧 | `GET /api/v1/repos/{owner}/{repo}/labels` | (取得のみ。各ラベルの `id` と `name` を使う) |
| 認証アカウント | `GET /api/v1/user` | (取得のみ。`login` を使う) |
| Issue起票 | `POST /api/v1/repos/{owner}/{repo}/issues` | `title`、`body`、`assignees`、`labels`、`ref` |
| PR作成 | `POST /api/v1/repos/{owner}/{repo}/pulls` | `title`、`body`、`base`、`head`、`assignees`、`labels` |

Issue起票の項目は [Gitea Issue API（公開日不明、2026/10確認）, Request Body](https://docs.gitea.com/api/operations/issue-create-issue/)、PR作成の項目は [Gitea PR API（公開日不明、2026/10確認）, Request Body](https://docs.gitea.com/api/operations/repo-create-pull-request/)を参照してください。ラベル一覧は [Gitea ラベルAPI（公開日不明、2026/10確認）, Get all of a repository's labels](https://docs.gitea.com/api/operations/issue-list-labels/)、認証アカウントは [Gitea ユーザーAPI（公開日不明、2026/10確認）, Get the authenticated user](https://docs.gitea.com/api/operations/user-get-current/)を参照してください。

`assignees` はユーザー名の配列です。`labels` はラベル名ではなく、ラベルのIDの配列で、IDはラベル一覧から確認します。`ref` はIssueのブランチです。公開資料に値の形式の説明がないため、接続先の `/api/swagger` と、既存のIssueを取得した結果の `ref` で形式を確認します。これらの項目の型は、公開資料の記載です。値の選び方は、このスキルで採用する方針です。

Issue本文の例です。`USER_NAME`、`LABEL_ID`、`BRANCH_REF` は、確認した値に置き換えます。

```json
{
  "title": "課題のタイトル",
  "body": "目的\n\n背景\n\n完了条件",
  "assignees": ["USER_NAME"],
  "labels": [LABEL_ID],
  "ref": "BRANCH_REF"
}
```

PR本文の例です。実際のタイトル・本文・ブランチ名に置き換え、JSONのエスケープは利用するクライアントやシリアライザーに任せます。

```json
{
  "title": "変更のタイトル",
  "body": "変更内容\n\n確認結果",
  "base": "BASE_BRANCH",
  "head": "HEAD_BRANCH",
  "assignees": ["USER_NAME"],
  "labels": [LABEL_ID]
}
```

`base` は取り込み先、`head` は変更元です。[Gitea PR API（公開日不明、2026/10確認）, Request Body](https://docs.gitea.com/api/operations/repo-create-pull-request/)

APIトークンでの認証には `Authorization: token ...` ヘッダーを使用できます。[Gitea API Usage（公開日不明、2026/10確認）, Authentication / More on the Authorization header](https://docs.gitea.com/development/api-usage/#authentication)

認証情報はHTTPクライアントが既存の設定から直接読み込み、トークンの値を引数やログに出さない方法を使います。認証情報は確認した接続先だけへ送ります。作成結果が不明な場合は、一覧・取得APIで照合するまでPOSTを繰り返しません。これらは、このスキルで採用する操作方針です。

## Web画面を使う場合

Web画面でPRを作成する場合は、対象リポジトリの「Pull Requests」から新規作成し、取り込み先と変更元を選択してタイトル・本文を入力します。[Gitea PR作成（公開日不明、2026/10確認）, Creating a Pull Request](https://docs.gitea.com/usage/issues-prs/pull-request/)

Web画面でIssueやPRを作成した場合も、担当者・ラベル(Issueではブランチも)を決めて選択します。作成後の画面で、選択されているかを確認します。これは、このスキルで採用する方針です。

## 参照資料

以下の公式資料は2026年10月6日に確認しました(ラベル一覧、認証アカウント、Issue・PRの担当者・ラベル・ブランチの項目は10月12日)。公開日は不明です。

[Gitea Tea, 公開日不明] Gitea. 「What is Tea?」. Gitea. [公式CLIの紹介](https://about.gitea.com/products/tea/)

[Gitea API Usage, 公開日不明] Gitea. 「API Usage」. Gitea Documentation. [APIの認証と仕様](https://docs.gitea.com/development/api-usage/)

[Gitea Issue API, 公開日不明] Gitea. 「Create an issue」. Gitea Documentation. [Issue作成API](https://docs.gitea.com/api/operations/issue-create-issue/)

[Gitea PR API, 公開日不明] Gitea. 「Create a pull request」. Gitea Documentation. [PR作成API](https://docs.gitea.com/api/operations/repo-create-pull-request/)

[Gitea PR作成, 公開日不明] Gitea. 「Creating a Pull Request」. Gitea Documentation. [Web画面でのPR作成](https://docs.gitea.com/usage/issues-prs/pull-request/)

[Gitea ラベルAPI, 公開日不明] Gitea. 「Get all of a repository's labels」. Gitea Documentation. [ラベル一覧API](https://docs.gitea.com/api/operations/issue-list-labels/)

[Gitea ユーザーAPI, 公開日不明] Gitea. 「Get the authenticated user」. Gitea Documentation. [認証アカウントの取得API](https://docs.gitea.com/api/operations/user-get-current/)
