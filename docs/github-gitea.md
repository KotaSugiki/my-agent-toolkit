# GitHub・GiteaでのIssue起票とPR作成

Issueの起票とプルリクエスト（PR）の作成には、対象リポジトリを管理するGitHubまたはGiteaを操作します。この文書では、本リポジトリで採用する手順と、サービスごとの操作方法を説明します。

コミット、ブランチ、mainへの取り込みについては、[リポジトリの取り扱いルール](repository-rules.md)に従います。

## 操作先と操作手段

作業前に `git remote -v` で接続先を確認し、操作するサービス、リポジトリ所有者、リポジトリ名を特定します。複数のリモートがある場合は、依頼された作成先を使います。Giteaの接続先URLは利用環境に合わせて確認します。

基本の操作手段は次のとおりです。CLIは、コマンドを入力して操作するツールです。

| サービス | 基本の操作手段 | 代替手段 |
| --- | --- | --- |
| GitHub | GitHub CLIの `gh` | 接続済みの連携ツール、Web画面、API |
| Gitea | Gitea公式CLIの `tea` | 接続済みの連携ツール、Web画面、API |

`gh` はIssueやPRの作成コマンドを提供します。`tea` はGiteaのIssueやPRなどを操作する公式CLIです。[GitHub CLI（公開日不明、2026/10確認）, 作成コマンド](https://cli.github.com/manual/gh_pr_create)、[Gitea Tea（公開日不明、2026/10確認）, What is Tea?](https://about.gitea.com/products/tea/)

認証済みの操作手段が利用できる場合は、それを使います。認証先のホストとアカウントを確認し、起票・作成に必要な権限を持つ認証情報を使います。トークンやパスワードは、リポジトリ、Issue本文、PR本文、作業報告に記載しません。

## 共通の作業手順

1. 対象リポジトリの既存Issue・PRを確認し、同じ内容の起票や作成を重複させないようにします。
2. 課題や検討事項を記録する必要がある場合は、Issueを起票します。小さな修正は、Issueを作らずPRで説明できます。
3. 作業ブランチで変更し、必要な確認を済ませてコミットします。
4. 作業ブランチを対象のリモートにpushします。
5. 取り込み先を `main`、変更元を作業ブランチとしてPRを作成します。
6. 作成されたIssue・PRの番号、URL、本文を確認し、作業報告にURLを記載します。

Issueには、目的・背景・完了条件を記載します。不具合の場合は、再現手順、期待する動作、実際の動作も記載します。PRには、解決する問題、変更内容、確認結果を記載し、関連するIssueがあれば番号またはURLを添えます。タイトルと本文は日本語を基本とし、PRのタイトルは運用ルールで定めたコミットメッセージ形式にします。

AIエージェントも依頼された作業範囲に従って操作します。PRの作成とマージは別の操作として扱います。認証や権限が不足して作成できない場合は、用意したタイトル・本文と、実行できなかった操作を報告します。作成先で確認できたものだけを作成済みとして報告します。

## GitHubの操作

### 認証

`gh auth status` で認証状態を確認できます。初回の認証には `gh auth login` を使えます。[GitHub認証（公開日不明、2026/10確認）, auth status](https://cli.github.com/manual/gh_auth_status)、[auth login](https://cli.github.com/manual/gh_auth_login)

```powershell
gh auth status --hostname github.com
gh auth login --hostname github.com --web
```

ログインのコマンドは、認証が必要な場合に実行します。ブラウザーでのログインが必要な部分は、利用者が操作します。

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

`tea` を使う場合は、対象Giteaサーバーのログイン設定を用意し、接続先とアカウントを確認します。複数サーバーのログイン設定には名前を付けて管理できます。[Gitea Tea（公開日不明、2026/10確認）, See it in action / Why Tea?](https://about.gitea.com/products/tea/)

利用するバージョンの `tea --help` と `tea login add --help` で、ログイン設定と操作コマンドを確認します。Issue・PR作成時は、対象リポジトリ、タイトル、本文を指定し、PRの取り込み先を `main`、変更元をpush済みの作業ブランチにします。

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
