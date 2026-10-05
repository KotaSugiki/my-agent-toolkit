# resume-gitea-issue

Orca CLIで現在のワークツリーを確認し、GiteaのIssue URLから作業を開始・再開するスキルです。Issueの本文・コメントと、手元のコード・未コミットの変更を照合して、現在のセッションで残りの作業を進めます。

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

必要なら、URLの後に「調査から始めてください」「既存の修正を引き継いでください」などの追加指示を添えます。

最初にOrca CLIの `worktree current --json` を実行し、作業場所を確認します。そのワークツリーでIssueの要求と現在の変更を照合し、作業を進めます。

## 利用に必要なもの

Orca、エージェントから実行できるOrca CLI、Orcaが管理する対象リポジトリのワークツリーが必要です。CLIが使えない場合や作業場所を確認できない場合は、その問題を解消してから作業を進めます。

Issueを読み取れる接続手段も必要です。認証済みのGitea連携、`tea`、APIへのHTTPアクセスなどを使います。非公開Issueの場合は、対象サーバー向けの認証が必要です。

別のスキルや、スキル専用のプロジェクト文書は必要ありません。APIで読み取るための補助資料は、このスキル内に含めています。

エージェント向けの指示は [SKILL.md](SKILL.md)、APIの取得手順と参照資料は [references/gitea-api.md](references/gitea-api.md)に記載しています。
