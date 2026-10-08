# my-agent-toolkit

ソフトウェア開発を効率化するために自作したツール、ハーネス、AIエージェント向けスキル、プロンプト、フック、自動化などを管理する個人用リポジトリです。よく使うスキルも保存します。

## ディレクトリ構成

| ディレクトリ | 役割 |
| --- | --- |
| `agents/` | Codex、Claude Codeなどで利用するサブエージェントやエージェント定義 |
| `plugins/` | 共通の編集元から生成したClaude Code・Codex向けプラグインの配布ファイル |
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
- [github-gitea-operations](skills/github-gitea-operations/README.md): 導入先の規約と接続先を確認し、GitHub・GiteaのIssue起票とPR作成を進めるスキルです。
- [html-explainer](skills/html-explainer/README.md): 概念や仕組みを、12種の型で描いた図解入りのHTML説明文書として作成・編集するスキルです。文書と図は同じ配色・書体で統一します。
- [ja-text-communication](skills/ja-text-communication/README.md): 日本語の応答やドキュメントを、一読で意味が伝わるように記述するためのスキルです。
- [resume-gitea-issue](skills/resume-gitea-issue/README.md): Orca CLIで作業場所を確認し、GiteaのIssue URLから現在のセッションで残りの作業を進めるスキルです。
- [setup-experiments](skills/setup-experiments/README.md): 実験プロジェクトの目標、データ、実行・評価方法、制約、記録先を対話で確認し、保存するスキルです。
- [wait-what](skills/wait-what/README.md): Matt Pocockさんのスキルを日本語化したものです。分かりにくい説明に背景を補い、平易な日本語で説明し直します。

## 実験支援エージェント

[実験支援エージェント](agents/experiments/README.md)には、実験計画、実験実行、評価・分析、レポート作成の4担当をまとめています。計画はMarkdownファイル、レポートは短い要約と視覚表示・操作できる詳細を持つHTMLとして保存します。保存情報と人間のフィードバックを次の実験へ引き継ぎます。

エージェントの導入は、Claude CodeまたはCodexのマーケットプレイスから [experimentsプラグイン](plugins/experiments/README.md)を追加する方法に統一します。[導入・更新・削除の共通ガイド](docs/agent-plugins.md)を参照してください。Codexでは2スキルの認識まで確認済みで、4担当の登録と全体進行は未確認です。

## 共通ルールの導入

[配布用AGENTS.md](templates/AGENTS.md)には、コミット・ブランチ・PR・Issueの規約と、ドキュメントの配置・記述などの共通ルールをまとめています。単体で利用できるよう、必要な指示を本文に含めています。

導入は手動で行います。AGENTS.mdがないリポジトリにはコピーし、既にある場合はプロジェクト固有の指示を残して共通ルールを組み込みます。新規導入、既存リポジトリへの導入、更新は、[AGENTS.mdの手動導入](docs/agents-installation.md)を参照してください。

## Skillsの導入

Skillsの導入には `npx skills` を使います。このスキルがリモートの `main` に取り込まれた後、利用先のプロジェクトで次のコマンドを実行します。

```shell
npx skills add KotaSugiki/my-agent-toolkit --skill ja-text-communication --agent codex
```

パッケージマネージャの準備、他のエージェントへの導入、更新・削除の方法は、[Skillsの導入方法](docs/skills-installation.md)を参照してください。

## 運用ルール

共通の規約本文は、[配布用AGENTS.md](templates/AGENTS.md)を参照してください。このツールキット固有の配置・導入方針やGitHub側の設定方針は、[リポジトリの取り扱いルール](docs/repository-rules.md)を参照してください。

Issue起票やPR作成の操作手順は [github-gitea-operations](skills/github-gitea-operations/README.md)にまとめています。規約との役割分担と利用案内は、[GitHub・GiteaでのIssue起票とPR作成](docs/github-gitea.md)を参照してください。
