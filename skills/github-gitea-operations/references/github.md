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

## 担当者とラベルを決める

ラベルは、対象リポジトリの既存ラベルから選びます。次のコマンドで、ラベル名と説明の一覧を確認します。

```powershell
gh label list --repo HOST/OWNER/REPO --limit 100
```

`gh label list` はリポジトリのラベルを表示します。件数の既定は30なので、`--limit` で増やします。[GitHubラベル一覧（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_label_list)

Issue・PRの作成コマンドでは、`--assignee` で担当者を、`--label` でラベルを名前で指定します。担当者を認証アカウントにするときは `@me` を使い、ほかのユーザーはログイン名を指定します。ラベルは、確認した既存の名前だけを指定します。合うものがなければ `--label` を付けず、付けなかったことを報告します。[GitHub Issue作成（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_issue_create)

GitHubのIssueには、既存のブランチを選んで指定するオプションがありません。`gh issue develop` は、Issueに関連づけた新しいブランチを作るコマンドで、既存のブランチを関連づけるオプションはありません。依頼がない限り使いません。[GitHub Issue ブランチ（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_issue_develop)

## Issueを作成する

`$issueBodyPath` は、事前に準備したUTF-8の本文ファイルのパスです。タイトルと本文は作業先の規約・テンプレートに合わせます。`LABEL` は、確認した既存のラベル名です。

```powershell
gh issue create --repo HOST/OWNER/REPO --title "課題のタイトル" --body-file $issueBodyPath --assignee "@me" --label "LABEL"
```

`--repo` は作成先、`--body-file` は本文ファイル、`--assignee` は担当者、`--label` はラベルを指定します。[GitHub Issue作成（公開日不明、2026/10確認）, Options](https://cli.github.com/manual/gh_issue_create)

## PRを作成する

`REMOTE` は確認したpush先のリモート、`HEAD_BRANCH` は変更元、`BASE_BRANCH` は導入先の規約や指定に従って確認した取り込み先です。`$prBodyPath` は準備したUTF-8の本文ファイルのパスです。`LABEL` は、確認した既存のラベル名です。必要な変更をコミットした後に実行します。

```powershell
git push -u REMOTE HEAD_BRANCH
gh pr create --repo HOST/OWNER/REPO --base BASE_BRANCH --head HEAD_BRANCH --title "変更のタイトル" --body-file $prBodyPath --assignee "@me" --label "LABEL"
```

`--base` は取り込み先、`--head` は変更元、`--assignee` は担当者、`--label` はラベルです。フォークからの変更元は `OWNER:HEAD_BRANCH` の形も使えます。`--head` を明示すると、作成コマンドによる暗黙のpushやフォーク作成を避けられます。[GitHub PR作成（公開日不明、2026/10確認）, 本文 / Options](https://cli.github.com/manual/gh_pr_create)

同じCLIのヘルプで、作成後の取得コマンドと表示項目を確認します。作成した番号またはURLからタイトル・本文を再取得し、担当者・ラベルも照合します。PRでは取り込み先・変更元も照合します。次の例は、このスキル向けに作成したものです。`gh pr view` と `gh issue view` は、`--json` に `assignees` と `labels` を指定できます。

```powershell
gh pr view NUMBER --repo HOST/OWNER/REPO --json assignees,labels,baseRefName,headRefName
gh issue view NUMBER --repo HOST/OWNER/REPO --json assignees,labels
```

`gh pr create --dry-run` はGitの変更をpushする場合があります。外部への書込みをしない確認には、コマンドの組立てや隔離した模擬環境を使う方針とします。[GitHub PR作成（公開日不明、2026/10確認）, Options: dry-run](https://cli.github.com/manual/gh_pr_create)

## 参照資料

以下の公式資料は2026年10月6日に確認しました(ラベル一覧とIssueのブランチは10月12日)。公開日は不明です。コマンド例と確認手順はこのスキル向けに作成しています。

[GitHub認証, 公開日不明] GitHub. 「gh auth status」「gh auth login」. GitHub CLI Manual. [認証状態](https://cli.github.com/manual/gh_auth_status)、[ログイン](https://cli.github.com/manual/gh_auth_login)

[GitHub Issue作成, 公開日不明] GitHub. 「gh issue create」. GitHub CLI Manual. [Issue作成のオプション](https://cli.github.com/manual/gh_issue_create)

[GitHub PR作成, 公開日不明] GitHub. 「gh pr create」. GitHub CLI Manual. [PR作成のオプション](https://cli.github.com/manual/gh_pr_create)

[GitHubラベル一覧, 公開日不明] GitHub. 「gh label list」. GitHub CLI Manual. [ラベル一覧のオプション](https://cli.github.com/manual/gh_label_list)

[GitHub Issue ブランチ, 公開日不明] GitHub. 「gh issue develop」. GitHub CLI Manual. [Issueに関連づけるブランチのオプション](https://cli.github.com/manual/gh_issue_develop)
