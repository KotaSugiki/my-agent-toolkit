# my-agent-toolkit

ソフトウェア開発を効率化するために自作したツール、ハーネス、AIエージェント向けスキル、プロンプト、フック、自動化などを管理する個人用リポジトリです。よく使うスキルも保存します。

## ディレクトリ構成

| ディレクトリ | 役割 |
| --- | --- |
| `agents/` | Codex、Claude Codeなどで利用するサブエージェントやエージェント定義 |
| `harnesses/` | 開発フローやAIエージェントの実行を補助するハーネス |
| `skills/` | コードレビュー、文章校正、コード理解など、再利用可能なSkills |
| `prompts/` | 汎用的に再利用するプロンプト |
| `hooks/` | CodexやClaude Codeなどのイベントフック、実行前後処理 |
| `scripts/` | 開発作業を自動化する小規模なCLIやユーティリティスクリプト |
| `templates/` | リポジトリ、ドキュメント、設定ファイルなどのテンプレート |
| `docs/` | 各ツールの設計方針や利用方法などのドキュメント |
| `examples/` | 各ツールやSkillの使用例 |

各ツールやスキルは用途に合うディレクトリに配置し、必要になった時点でファイルやサブディレクトリを追加します。空ディレクトリには、Gitで管理するための `.gitkeep` を配置します。

## 保存しているスキル

- [deep-code-reading](skills/deep-code-reading/README.md): リポジトリ全体や指定箇所の構成と基本動作を、コードポインター付きで解説するスキルです。
- [ja-text-communication](skills/ja-text-communication/README.md): 日本語の応答やドキュメントを、一読で意味が伝わるように記述するためのスキルです。
- [resume-gitea-issue](skills/resume-gitea-issue/README.md): Orca CLIで作業場所を確認し、GiteaのIssue URLから現在のセッションで残りの作業を進めるスキルです。
- [wait-what](skills/wait-what/README.md): Matt Pocockさんのスキルを日本語化したものです。分かりにくい説明に背景を補い、平易な日本語で説明し直します。

## Skillsの導入

Skillsの導入には `npx skills` を使います。このスキルがリモートの `main` に取り込まれた後、利用先のプロジェクトで次のコマンドを実行します。

```shell
npx skills add KotaSugiki/my-agent-toolkit --skill ja-text-communication --agent codex
```

パッケージマネージャの準備、他のエージェントへの導入、更新・削除の方法は、[Skillsの導入方法](docs/skills-installation.md)を参照してください。

## 運用ルール

コミットメッセージ、ブランチの命名、mainブランチ保護、ドキュメントの階層については、[リポジトリの取り扱いルール](docs/repository-rules.md)を参照してください。

Issue起票やPR作成の操作方法については、[GitHub・GiteaでのIssue起票とPR作成](docs/github-gitea.md)を参照してください。
