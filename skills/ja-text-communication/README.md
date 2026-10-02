# ja-text-communication

日本語の応答やドキュメントを、一読で意味が伝わるように記述するためのスキルです。用語の説明、文の構成、根拠の示し方、作業報告などの指針を含みます。

## 前提条件と導入

スキルに対応したAIエージェントと、導入用のNode.js・npm・Gitを用意します。パッケージマネージャの準備、導入先、更新・削除の方法は、リポジトリ内の[Skillsの導入方法](https://github.com/KotaSugiki/my-agent-toolkit/blob/main/docs/skills-installation.md)を参照してください。共通ガイドは、スキルを導入した後も参照できるよう、リポジトリのURLで案内します。

このスキルがリモートの `main` に取り込まれた後、利用先のプロジェクトで次のコマンドを実行します。

```shell
npx skills add KotaSugiki/my-agent-toolkit --skill ja-text-communication --agent codex
```

Claude Codeに導入する場合は、`--agent claude-code` を指定します。ユーザー全体で使う場合は、`--global` を追加します。

## 使い方

導入先のエージェントに、日本語の文章を扱う際にこのスキルを使うよう依頼します。例えば、「ja-text-communicationを使って、変更内容を日本語で説明してください」と指定します。適用条件と指示の本文は [SKILL.md](SKILL.md) に記載しています。

取得元と独自変更の有無は、[取得元の記録](provenance.md)を参照してください。
