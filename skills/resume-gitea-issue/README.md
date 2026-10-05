# resume-gitea-issue

Orca CLIで作業に使うワークツリーを選び、GiteaのIssue URLから作業を開始・再開するスキルです。独立した新しいワークツリー、現在のワークツリーの子ワークツリー、既存のワークツリーを選べます。Issueの本文・コメントと、選んだ作業場所のコード・未コミットの変更を照合して、現在のセッションで残りの作業を進めます。

## 使い方

Orcaが管理する対象リポジトリのワークツリーで、エージェントのチャット入力欄にIssueのURLを添えて呼び出します。以下は使い方を示す架空のURLです。

Codexの場合:

```text
$resume-gitea-issue https://gitea.example.com/owner/repo/issues/42
```

Claude Codeの場合:

```text
/resume-gitea-issue https://gitea.example.com/owner/repo/issues/42
```

URLの後に作業場所を指定できます。以下はCodexでの呼び出し例です。Claude Codeでは先頭の `$` を `/` に置き換えます。

```text
$resume-gitea-issue https://gitea.example.com/owner/repo/issues/42 独立した新しいワークツリーを作成してください
$resume-gitea-issue https://gitea.example.com/owner/repo/issues/42 現在のワークツリーの子ワークツリーを作成してください
$resume-gitea-issue https://gitea.example.com/owner/repo/issues/42 現在のワークツリーで再開してください
```

作業場所の指定がなければ、作業前に選択肢を確認します。会話ですでに指定していれば、同じ選択は再確認しません。同じIssueの既存の作業場所が見つかった場合は、再利用するか新しく作るかを確認します。

子ワークツリーはOrca上の親子関係を表します。Gitの分岐元は、リポジトリのルールと指定に従います。現在のブランチから分岐させたい場合は、その指示も添えてください。新しいワークツリーには未コミットの変更が自動では引き継がれないため、引き継ぐ変更があれば伝えてください。

必要なら「調査から始めてください」などの追加指示も添えます。作業場所を選んだ後は、別のエージェントを起動せず、現在のセッションで作業を進めます。

## 利用に必要なもの

Orca、エージェントから実行できるOrca CLI、Orcaが管理する対象リポジトリのワークツリーが必要です。CLIが使えない場合や作業場所を確認できない場合は、その問題を解消してから作業を進めます。

Issueを読み取れる接続手段も必要です。認証済みのGitea連携、`tea`、APIへのHTTPアクセスなどを使います。非公開Issueの場合は、対象サーバー向けの認証が必要です。

別のスキルや、スキル専用のプロジェクト文書は必要ありません。APIで読み取るための補助資料は、このスキル内に含めています。

エージェント向けの指示は [SKILL.md](SKILL.md)、APIの取得手順と参照資料は [references/gitea-api.md](references/gitea-api.md)に記載しています。
