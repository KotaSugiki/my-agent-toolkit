# github-gitea-operations

GitHub・GiteaでIssueを起票し、プルリクエスト（PR）を作成するスキルです。作成先、認証、既存Issue・PRを確認し、導入先の規約に従って内容の準備から作成結果の確認まで進めます。

## 使い方

通常のチャットで「この課題をGitHubのIssueにしてください」「コミットからPR作成までお願いします」などと依頼します。Issue起票・PR作成に当てはまる依頼で自動呼出しの対象になります。コード修正だけや、既存Issueを読んで実装を再開するだけの依頼は対象にしません。

自動呼出しでは、エージェントがスキルの説明と依頼内容から使うスキルを選びます。必ず毎回実行される仕組みとして規約の適用を任せず、必須の規約は導入先のAGENTS.mdに残します。[OpenAI Skills（公開日不明、2026/10確認）, How ChatGPT and Codex use skills](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)

名前を指定して呼び出すこともできます。以下は使い方の例です。作成先や課題の内容は、実際の依頼に合わせて指定してください。

Codexの場合:

```text
$github-gitea-operations この課題をGitHubのIssueとして起票してください
$github-gitea-operations 変更をコミット・pushしてPRを作成してください
```

Claude Codeの場合:

```text
/github-gitea-operations この課題をGiteaのIssueとして起票してください
```

「PRの本文だけ用意してください」と依頼した場合は、本文の準備までを行います。Issue起票の依頼はPR作成を、PR作成の依頼はマージを許可するものとして扱いません。

## 利用に必要なもの

対象のリポジトリや作成先を特定できるURLと、そのサービスを操作できる接続手段が必要です。GitHubでは `gh`、Giteaでは `tea` を基本とし、認証済み連携ツールやAPIも使います。実際の作成には対象リポジトリへの権限が必要です。

作業先にAGENTS.mdと参照先の規約がある場合は、それに従います。取り込み先や言語・タイトル形式をこのツールキットのものに固定しません。他のスキルや、このツールキットのdocsファイルの導入は必要ありません。

エージェント向けの指示は [SKILL.md](SKILL.md)、詳しい操作例は [GitHub](references/github.md)と [Gitea](references/gitea.md)にまとめています。

## 参照資料

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Build skills」. ChatGPT Learn. [スキルの構成と呼出し](https://learn.chatgpt.com/docs/build-skills)
