# GitHubの操作例

GitHubをCLIで操作する場合に参照します。以下はこのスキル向けに作成したPowerShellの例です。CLIの詳細やAPIによる代替操作は、必要なときに公式資料と実行環境のヘルプで確認します。

## 接続先・認証・既存の作成物を確認する

`HOST`、`OWNER`、`REPO` は、確認したGitHubのホスト名、所有者、リポジトリ名に置き換えます。ホスト名はGitリモートや依頼のURLから確認し、GitHub Enterpriseを含め、操作するホストを明示します。

```powershell
gh auth status --hostname HOST
gh repo view HOST/OWNER/REPO --json nameWithOwner,url,defaultBranchRef,viewerPermission
gh issue list --repo HOST/OWNER/REPO --state all
gh pr list --repo HOST/OWNER/REPO --state all
```

`gh auth status` は認証状態の確認、`gh auth login` はログインに使えます。既存の認証が使える場合は再ログインを求めません。利用者による認証が必要な場合にだけ、次の例を案内します。[GitHub認証（公開日不明、2026/10確認）, auth status / auth login](https://cli.github.com/manual/gh_auth_status)、[ログインの公式説明](https://cli.github.com/manual/gh_auth_login)

```powershell
gh auth login --hostname HOST --web
```

一覧に対象が見つからない場合は、目的に合う検索やページの確認を行います。表示された最初の一覧だけで、重複がないと断定しません。これらは、このスキルで採用する確認手順です。

## Issueを作成する

`$issueBodyPath` は、事前に準備したUTF-8の本文ファイルのパスです。タイトルと本文は作業先の規約・テンプレートに合わせます。

```powershell
gh issue create --repo HOST/OWNER/REPO --title "課題のタイトル" --body-file $issueBodyPath
```

`--repo` は作成先、`--body-file` は本文ファイルを指定します。[GitHub Issue作成（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_issue_create)

## PRを作成する

`REMOTE` は確認したpush先のリモート、`HEAD_BRANCH` は変更元、`BASE_BRANCH` は導入先の規約や指定に従って確認した取り込み先です。`$prBodyPath` は準備したUTF-8の本文ファイルのパスです。必要な変更をコミットした後に実行します。

```powershell
git push -u REMOTE HEAD_BRANCH
gh pr create --repo HOST/OWNER/REPO --base BASE_BRANCH --head HEAD_BRANCH --title "変更のタイトル" --body-file $prBodyPath
```

`--base` は取り込み先、`--head` は変更元です。フォークからの変更元は `OWNER:HEAD_BRANCH` の形も使えます。`--head` を明示すると、作成コマンドによる暗黙のpushやフォーク作成を避けられます。[GitHub PR作成（公開日不明、2026/10確認）, 本文 / Options](https://cli.github.com/manual/gh_pr_create)

同じCLIのヘルプで、作成後の取得コマンドと表示項目を確認します。作成した番号またはURLからタイトル・本文を再取得し、PRでは取り込み先・変更元も照合します。

`gh pr create --dry-run` はGitの変更をpushする場合があります。外部への書込みをしない確認には、コマンドの組立てや隔離した模擬環境を使う方針とします。[GitHub PR作成（公開日不明、2026/10確認）, Options: dry-run](https://cli.github.com/manual/gh_pr_create)

## 参照資料

以下の公式資料は2026年10月6日に確認しました。公開日は不明です。コマンド例と確認手順はこのスキル向けに作成しています。

[GitHub認証, 公開日不明] GitHub. 「gh auth status」「gh auth login」. GitHub CLI Manual. [認証状態](https://cli.github.com/manual/gh_auth_status)、[ログイン](https://cli.github.com/manual/gh_auth_login)

[GitHub Issue作成, 公開日不明] GitHub. 「gh issue create」. GitHub CLI Manual. [Issue作成のオプション](https://cli.github.com/manual/gh_issue_create)

[GitHub PR作成, 公開日不明] GitHub. 「gh pr create」. GitHub CLI Manual. [PR作成のオプション](https://cli.github.com/manual/gh_pr_create)
