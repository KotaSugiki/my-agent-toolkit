# エージェントのマーケットプレイス導入

このツールキットのエージェントは、Claude CodeまたはCodexのマーケットプレイスからプラグインとして導入します。マーケットプレイスは、プラグインの取得元をまとめた配布一覧です。このリポジトリの配布元名は `my-agent-toolkit`、実験支援プラグイン名は `experiments` です。

導入・更新・削除は、このガイドの2つの方法に統一します。利用者がエージェント定義や設定をコピーしたり、登録スクリプトを実行したりする手順は案内しません。スキル単独の導入は [Skillsの導入方法](skills-installation.md)で扱います。

## 前提条件と対応状況

Gitと、利用するClaude CodeまたはCodexを用意します。以下のコマンド例は、このリポジトリの配布名に合わせたものです。GitHubからの導入は、配布一覧とプラグインが `main` に取り込まれた後に使えます。利用者側でPythonを使って配布物を生成する必要はありません。

ローカル配布元を使った確認結果は次のとおりです。実際のモデルによる実験フローと、GitHubからの導入は未検証です。

| 利用先 | 確認した版 | 確認できた範囲 |
| --- | --- | --- |
| Claude Code | 2.1.291 | 導入、有効化、2スキルと4担当の認識 |
| Codex CLI | 0.160.1 | 導入、有効化、2スキルの認識。4担当の登録と全体進行は未確認 |

Codexの導入成功は、4担当がカスタムエージェントとして登録されることまで保証しません。現在の配布物にはCodex用の明示起動限定設定も未同梱です。実験支援全体を利用できるとする前に、両方を検証します。調査の根拠は [Codexの導入調査](codex-plugin-research.md)を参照してください。

## Claude Codeのマーケットプレイス

### 導入と確認

シェルで実行します。マーケットプレイスの追加は初回だけです。

```shell
claude --version
claude plugin marketplace add KotaSugiki/my-agent-toolkit
claude plugin install experiments@my-agent-toolkit --scope user
claude plugin list
claude plugin details experiments
```

`user` は自分の全プロジェクトが対象です。現在のプロジェクトで自分だけに使う場合は `--scope local` にします。一覧の有効状態を確認し、新しいセッションを開いて `/agents` で `experiments:experiment-` から始まる4担当を確認します。[Claude Code Install（公開日不明、2026/10確認）, Choose where plugins are enabled / Manage plugins from your shell](https://code.claude.com/docs/en/plugins/install)、[Claude Code Subagents（2026/10確認）, Manage subagents](https://code.claude.com/docs/en/sub-agents)

前提整理は `/experiments:setup-experiments`、全体進行は `/experiments:run-experiments` を使います。依頼例と成果物は [プラグインの使い方](../plugins/experiments/README.md)を参照してください。

### 更新と削除

更新する場合は次のコマンドを実行し、新しいセッションで読み込み直します。

```shell
claude plugin marketplace update my-agent-toolkit
claude plugin update experiments@my-agent-toolkit --scope user
```

削除する場合は、導入時と同じスコープを指定します。この配布元を使わなくなった場合だけ、最後の行でマーケットプレイスも削除します。

```shell
claude plugin uninstall experiments@my-agent-toolkit --scope user
claude plugin marketplace remove my-agent-toolkit
```

独自マーケットプレイスの自動更新は既定でオフです。必要なら `/plugin` のマーケットプレイス設定から有効にします。[Claude Code Install（2026/10確認）, Keep plugins updated / Manage marketplaces](https://code.claude.com/docs/en/plugins/install)

## Codexのマーケットプレイス

### 導入と確認

シェルで実行します。マーケットプレイスの追加は初回だけです。

```shell
codex --version
codex plugin marketplace add KotaSugiki/my-agent-toolkit --ref main
codex plugin add experiments@my-agent-toolkit
codex plugin list --json
```

一覧の `installed` に `experiments@my-agent-toolkit` があり、`enabled` が `true` であることを確認します。Codexは、GitHubリポジトリをマーケットプレイスとして登録できます。[OpenAI Commands（公開日不明、2026/10確認）, codex plugin / codex plugin marketplace](https://learn.chatgpt.com/docs/developer-commands#codex-plugin)

新しいセッションで `/skills` を開き、`experiments:setup-experiments` と `experiments:run-experiments` を確認します。Codexでは `$` とスキル名で明示的に呼び出します。全体進行用スキルが一覧にあることと、4担当への委任が動くことは別の確認です。[OpenAI Skills（公開日不明、2026/10確認）, How ChatGPT and Codex use skills](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)

### 更新と削除

更新する場合は、配布元の情報を更新してからプラグインを再導入します。一覧の版を確認し、新しいセッションで読み込み直します。

```shell
codex plugin marketplace upgrade my-agent-toolkit
codex plugin add experiments@my-agent-toolkit
codex plugin list --json
```

`marketplace upgrade` はGitから取得した配布元を更新します。`plugin add` はプラグインを導入します。手元の一時環境では、配布物の版を変更した後の `add` で新しい版になることを確認しました。[OpenAI Commands（2026/10確認）, codex plugin / codex plugin marketplace](https://learn.chatgpt.com/docs/developer-commands#codex-plugin)

削除する場合は次のコマンドを使います。この配布元を使わなくなった場合だけ、最後の行も実行します。

```shell
codex plugin remove experiments@my-agent-toolkit
codex plugin marketplace remove my-agent-toolkit
```

`plugin remove` はプラグインの登録とキャッシュを削除します。[OpenAI Commands（2026/10確認）, codex plugin](https://learn.chatgpt.com/docs/developer-commands#codex-plugin)

## 以前の個別導入からの移行

以前の4担当や単独スキルがある場合は、保存先と独自変更を確認して退避します。マーケットプレイスからの導入と認識を確認してから、旧版の4担当に限ってファイルと設定の参照を整理します。他のエージェント定義、設定、実験記録は保持します。単独スキルの削除は [Skillsの更新・削除](skills-installation.md#更新削除)を参照してください。

Codexでは4担当の登録が未確認なので、既存の動作する登録は、その代替を確認するまで保持します。

## 保守担当者向けの生成と公開

配布一覧は [marketplace.json](../.claude-plugin/marketplace.json)、プラグインの名前・版は [plugin.json](../plugins/experiments/.claude-plugin/plugin.json)で管理します。Claude形式のカタログはCodexでも互換形式として扱われ、今回の手元確認でも同じ配布物を使えました。[OpenAI Packaging（公開日不明、2026/10確認）, How local marketplaces work](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work)

指示本文の編集元は `agents/experiments/` と `skills/setup-experiments/` です。Python 3.11以上を用意し、リポジトリルートで配布物を生成・検証します。次のスクリプトは配布物の保守に使います。

```shell
python agents/experiments/scripts/register.py --agent claude-plugin --output plugins/experiments --force
python agents/experiments/scripts/register.py --agent claude-plugin --output plugins/experiments --check
python -B -m unittest discover -s agents/experiments/tests -v
claude plugin validate --strict ./plugins/experiments
claude plugin validate --strict .
```

`--agent claude-plugin` は現在の共通配布物を生成するモード名です。`--force` は4担当、2スキルと付属資料、ライセンスを更新します。マニフェストとREADMEは変更しません。`--check` は編集元との差異を確認するだけです。生成した `agents/` と `skills/` は直接編集しません。

公開前に次の順で確認します。

1. 配布物を再生成し、上の検証を通します。初回の版は `0.1.0`、以後は `plugin.json` の `version` を増やします。
2. 一時環境で、各マーケットプレイスの追加コマンドの取得元を手元のリポジトリの絶対パスに置き換え、導入・認識・更新・削除を確認します。利用者の設定は変更しません。
3. Claude Codeでは2スキルと4担当、Codexでは2スキルに加えて4担当の委任と明示起動の設定を検証します。前提の対話、Markdownの計画保存、HTMLレポートも利用確認します。
4. [リポジトリの規約](repository-rules.md)に従い、PRで `main` に取り込みます。GitHubから取得できたら、両方のリモート導入を確認します。

独自マーケットプレイスへの公開では、Anthropicのディレクトリへの提出は不要です。指示本文を更新した場合も版を増やします。[Claude Code Publish（公開日不明、2026/10確認）, 独自のマーケットプレイスを通じて公開する / ユーザーに更新を配布する](https://code.claude.com/docs/ja/plugins/publish)

## 参照資料

[Claude Code Install, 公開日不明（2026/10確認）] Anthropic. 「Install and manage plugins」. [導入と管理](https://code.claude.com/docs/en/plugins/install)

[Claude Code Subagents, 公開日不明（2026/10確認）] Anthropic. 「Create custom subagents」. [担当の確認](https://code.claude.com/docs/en/sub-agents)

[Claude Code Publish, 公開日不明（2026/10確認）] Anthropic. 「プラグインを公開・配布する」. [公開方法](https://code.claude.com/docs/ja/plugins/publish)

[OpenAI Commands, 公開日不明（2026/10確認）] OpenAI. 「Developer commands」. [CLIコマンド](https://learn.chatgpt.com/docs/developer-commands)

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Build skills」. [スキルの呼び出し](https://learn.chatgpt.com/docs/build-skills)

[OpenAI Packaging, 公開日不明（2026/10確認）] OpenAI. 「Package your plugin」. [配布構成](https://developers.openai.com/plugins/build/plugins)
