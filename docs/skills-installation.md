# Skillsの導入方法

このリポジトリのSkillsは、`npx skills` で利用先のエージェント環境へ導入します。導入先の変更を編集元へ反映するかどうかは、[リポジトリの取り扱いルール](repository-rules.md)に従います。

このガイドはSkillsの導入手順を扱います。`harnesses/` や `hooks/` などの導入方法は、[種類ごとの導入方法](repository-rules.md#種類ごとの導入方法)を参照してください。

## 前提条件とパッケージマネージャ

Node.jsはJavaScriptを実行する環境、npmはそのパッケージマネージャです。まずNode.jsとnpmを導入します。導入方法は[npm公式のNode.js・npm導入ガイド（公開日不明、2026/10確認）](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm/)を参照してください。

`npx` はnpmパッケージのコマンドを実行する仕組みです。必要なパッケージがローカルにない場合は、取得してnpmのキャッシュから実行します。[npm npx（公開日不明、2026/10確認）, Description](https://docs.npmjs.com/cli/v11/commands/npx/)

`skills` は、AIエージェント向けスキルを導入・管理するCLIです。次のコマンドで前提条件と、利用するCLIの情報を確認します。Gitリポジトリを取得するためのGitと、導入先のエージェント環境も用意します。

```shell
node --version
npm --version
npx --version
git --version
npm view skills version engines
npx skills --help
```

`npm view` はパッケージ情報を表示します。`engines` に示されるNode.jsの条件を満たす環境を使います。[npm view（公開日不明、2026/10確認）, Description](https://docs.npmjs.com/cli/v11/commands/npm-view/)

CLIは `npx skills` で実行できます。初回にnpmパッケージ取得の確認が表示された場合は、取得するパッケージ名を確認して進めます。[Skills CLI（公開日不明、2026/10確認）, Installation](https://www.skills.sh/docs/cli)、[npm npx（公開日不明、2026/10確認）, Description](https://docs.npmjs.com/cli/v11/commands/npx/)

WindowsのPowerShellで `npm.ps1` や `npx.ps1` の実行が制限される場合は、以下の例の `npm` を `npm.cmd`、`npx` を `npx.cmd` に置き換えます。

## 導入

以下は、このリポジトリ向けに作成したコマンド例です。プロジェクト単位で導入する場合は、利用先のプロジェクトのディレクトリで実行します。

```shell
# 導入可能なスキルを確認します
npx skills add KotaSugiki/my-agent-toolkit --list

# Codexへ導入します
npx skills add KotaSugiki/my-agent-toolkit --skill ja-text-communication --agent codex

# Claude Codeへ導入します
npx skills add KotaSugiki/my-agent-toolkit --skill ja-text-communication --agent claude-code
```

`--list` は導入候補の一覧、`--skill` はスキル名、`--agent` は導入先エージェントを指定します。ユーザー全体で使う場合は、導入コマンドに `--global` を追加します。[Skills README（公開日不明、2026/10確認）, Options / Installation Scope](https://github.com/vercel-labs/skills#options)

リモートからの導入は、対象スキルの変更をpushし、PRを `main` に取り込んでから行います。手元の変更を使う場合は、利用先のプロジェクトで、取得元にローカルの `skills/` のパスを指定します。

```shell
npx skills add /path/to/my-agent-toolkit/skills --skill ja-text-communication --agent codex
```

`/path/to/my-agent-toolkit/skills` は、編集元を置いている実際のパスに置き換えます。Windowsの例は `"C:/Users/your-name/orca/my-agent-toolkit/skills"` です。Giteaを取得元にする場合は、`KotaSugiki/my-agent-toolkit` の代わりに対象リポジトリのGit URLを指定します。ローカルパスとGit URLはCLIの取得元として利用できます。[Skills README（公開日不明、2026/10確認）, Source Formats](https://github.com/vercel-labs/skills#source-formats)

## 導入先と確認

プロジェクト単位では、Codex向けは `.agents/skills/`、Claude Code向けは `.claude/skills/` に配置されます。`--global` を付けた場合は、それぞれユーザーのホームディレクトリ内の `.codex/skills/`、`.claude/skills/` が対象です。[Skills README（公開日不明、2026/10確認）, Supported Agents](https://github.com/vercel-labs/skills#supported-agents)

導入後は一覧と、対象エージェントからスキルが認識されることを確認します。

```shell
# 導入済みスキルを確認します
npx skills list --agent codex

# ユーザー全体への導入を確認します
npx skills list --global --agent codex
```

`skills list` は導入済みスキルを表示します。[Skills README（公開日不明、2026/10確認）, skills list](https://github.com/vercel-labs/skills#skills-list)

## 更新・削除

リモートから導入したスキルを更新する場合は、更新内容を確認してから次のコマンドを使います。導入先で独自に修正している場合は、その内容を確認・退避してから更新します。

```shell
# プロジェクト単位のスキルを更新します
npx skills update ja-text-communication -p

# ユーザー全体に導入したスキルを更新します
npx skills update ja-text-communication --global

# プロジェクト単位のCodex向けスキルを削除します
npx skills remove ja-text-communication --agent codex

# ユーザー全体のCodex向けスキルを削除します
npx skills remove ja-text-communication --agent codex --global
```

`update` は導入済みスキルの更新、`remove` は導入先からの削除です。ローカルの変更を導入し直す場合は、ローカルパスを指定した `add` を使います。更新・再導入で、導入先の変更を編集元に採用したことにはしません。[Skills README（公開日不明、2026/10確認）, skills update / skills remove](https://github.com/vercel-labs/skills#skills-update)

## 参照資料

以下の公式資料は2026年10月に確認しました。公開日は不明です。

[npm導入, 公開日不明] npm. 「Downloading and installing Node.js and npm」. npm Docs. [Node.js・npm導入ガイド](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm/)

[npm npx, 公開日不明] npm. 「npx」. npm Docs. [npxの説明](https://docs.npmjs.com/cli/v11/commands/npx/)

[npm view, 公開日不明] npm. 「npm view」. npm Docs. [パッケージ情報の確認](https://docs.npmjs.com/cli/v11/commands/npm-view/)

[Skills CLI, 公開日不明] Vercel. 「CLI Reference」. Skills Documentation. [CLIガイド](https://www.skills.sh/docs/cli)

[Skills README, 公開日不明] Vercel Labs. 「skills」. GitHub. [コマンド・取得元・導入先の説明](https://github.com/vercel-labs/skills)
