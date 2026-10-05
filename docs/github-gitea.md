# GitHub・GiteaでのIssue起票とPR作成

操作先の確認、認証・権限、重複確認、Issue・PRの記載事項と作成後の確認は、[共通ルール](../templates/AGENTS.md#issue起票とpr作成)に定めています。この文書は、CLI（コマンドで操作するツール）やAPIの操作例と参考資料を扱います。

配布用AGENTS.mdには必要な規約本文が含まれているため、この補足文書を導入先へコピーする必要はありません。

GitHub CLIの `gh` はIssue・PRの作成コマンドを提供します。Gitea公式CLIの `tea` はIssue・PRなどを操作するツールです。[GitHub CLI（公開日不明、2026/10確認）, 作成コマンド](https://cli.github.com/manual/gh_pr_create)、[Gitea Tea（公開日不明、2026/10確認）, What is Tea?](https://about.gitea.com/products/tea/)

## GitHubの操作

### 認証

`gh auth status` で認証状態を確認できます。初回の認証には `gh auth login` を使えます。[GitHub認証（公開日不明、2026/10確認）, auth status](https://cli.github.com/manual/gh_auth_status)、[auth login](https://cli.github.com/manual/gh_auth_login)

```powershell
gh auth status --hostname github.com
gh auth login --hostname github.com --web
```

認証不足の場合の対応は、[共通ルール](../templates/AGENTS.md#issue起票とpr作成)に従います。

### Issue・PRの作成

以下は本リポジトリ向けに作成したPowerShellの例です。`OWNER/REPO` は対象の所有者とリポジトリ名に置き換えます。`$issueBodyPath` と `$prBodyPath` には、事前に一時ディレクトリに作成したUTF-8の本文ファイルのパスを設定します。例のブランチ名は、実際の作業ブランチに置き換えます。

```powershell
gh issue create --repo OWNER/REPO --title "GitHub・Giteaの操作手順を整備する" --body-file $issueBodyPath
git push -u origin docs/github-gitea
gh pr create --repo OWNER/REPO --base main --head docs/github-gitea --title "docs(repo): GitHub・Giteaの操作手順を追加する" --body-file $prBodyPath
```

`--repo` で作成先を指定し、`--body-file` で本文をファイルから読み込めます。PRの `--base` は取り込み先、`--head` は変更元です。例の `origin` も、確認したpush先のリモート名に合わせます。[GitHub Issue作成（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_issue_create)、[GitHub PR作成（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_pr_create)

## Giteaの操作

### CLIの利用

`tea` では複数サーバーのログイン設定に名前を付けて管理できます。[Gitea Tea（公開日不明、2026/10確認）, See it in action / Why Tea?](https://about.gitea.com/products/tea/)

ログイン設定と操作コマンドのヘルプは、`tea --help` と `tea login add --help` で表示できます。作成時に確認する事項は、[共通ルール](../templates/AGENTS.md#issue起票とpr作成)を参照してください。

### Web画面・APIの利用

Web画面でPRを作成する場合は、対象リポジトリの「Pull Requests」から新規作成し、取り込み先と変更元を選択して、タイトル・本文を入力します。[Gitea PR作成（公開日不明、2026/10確認）, Creating a Pull Request](https://docs.gitea.com/usage/issues-prs/pull-request/)

APIは、プログラムからサービスを操作するためのインターフェースです。Giteaの作成APIは次のとおりです。`{owner}` と `{repo}` は、対象の所有者とリポジトリ名に置き換えます。

| 操作 | HTTPメソッドとパス | この手順で指定する本文項目 |
| --- | --- | --- |
| Issue起票 | `POST /api/v1/repos/{owner}/{repo}/issues` | `title`、`body` |
| PR作成 | `POST /api/v1/repos/{owner}/{repo}/pulls` | `title`、`body`、`base`、`head` |

PRの `base` には `main`、`head` には作業ブランチ名を指定します。接続先サーバーのURLと認証情報を使い、利用中のGiteaのバージョンに対応したAPI仕様を確認します。[Gitea Issue API（公開日不明、2026/10確認）, Request Body](https://docs.gitea.com/api/operations/issue-create-issue/)、[Gitea PR API（公開日不明、2026/10確認）, Request Body](https://docs.gitea.com/api/operations/repo-create-pull-request/)

## 参照資料

以下の公式資料は2026年10月に確認しました。公開日は不明です。

[GitHub CLI, 公開日不明] GitHub. 「gh issue create」「gh pr create」. GitHub CLI Manual. [Issue作成](https://cli.github.com/manual/gh_issue_create)、[PR作成](https://cli.github.com/manual/gh_pr_create)

[GitHub認証, 公開日不明] GitHub. 「gh auth status」「gh auth login」. GitHub CLI Manual. [認証状態](https://cli.github.com/manual/gh_auth_status)、[ログイン](https://cli.github.com/manual/gh_auth_login)

[Gitea Tea, 公開日不明] Gitea. 「Tea: a powerful CLI for interacting with Gitea」. Gitea. [Tea公式紹介](https://about.gitea.com/products/tea/)

[Gitea PR作成, 公開日不明] Gitea. 「Pull Request」. Gitea Documentation. [PRの操作手順](https://docs.gitea.com/usage/issues-prs/pull-request/)

[Gitea API, 公開日不明] Gitea. 「Create an issue」「Create a pull request」. Gitea Documentation. [Issue作成API](https://docs.gitea.com/api/operations/issue-create-issue/)、[PR作成API](https://docs.gitea.com/api/operations/repo-create-pull-request/)
