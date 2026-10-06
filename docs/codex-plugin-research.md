# Codexの独自マーケットプレイス導入調査

確認日: 2026-10-06。対象: Codex CLIと、このリポジトリの実験支援プラグイン。

**Codexでも独自マーケットプレイスから導入できます。** GitHubリポジトリを登録し、プラグインを追加するCLIが公式に案内されています。[OpenAI Commands（公開日不明、2026/10確認）, codex plugin / marketplace](https://learn.chatgpt.com/docs/developer-commands#codex-plugin)

ただし、マーケットプレイスの互換性と、Claudeの4役割エージェントをそのまま使えることは別に確認する必要があります。公開ポータル向けの公式移植手順では、Claudeの `agents/` をスキルに変換するよう案内されています。[OpenAI Conversion（公開日不明、2026/10確認）, Review what OpenAI supports](https://developers.openai.com/plugins/guides/submit-claude-plugin#review-what-openai-supports)

## 確認できた範囲

| 項目 | 結果 | 根拠 |
| --- | --- | --- |
| 独自GitHubマーケットプレイス | 対応。`owner/repo`、Git URL、ローカルのルートディレクトリを登録できます | [OpenAI Commands（2026/10確認）, marketplace](https://learn.chatgpt.com/docs/developer-commands#codex-plugin-marketplace) |
| 既存のClaudeカタログ | `.claude-plugin/marketplace.json` の互換対応が記載されています。手元CLIでも既存カタログを変更せず導入できました | [OpenAI Packaging（2026/10確認）, How local marketplaces work](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work)・下記の手元確認 |
| スキルの一括配布 | プラグインの `skills/<名前>/SKILL.md` と付属資料を配布できます | [OpenAI Packaging（2026/10確認）, Plugin structure](https://developers.openai.com/plugins/build/plugins#plugin-structure) |
| Claudeの `agents/*.md` | CLIで役割として認識されるかは未確認。公開ポータル向けにはスキルへの変換が案内されています | [OpenAI Conversion（2026/10確認）, Review what OpenAI supports](https://developers.openai.com/plugins/guides/submit-claude-plugin#review-what-openai-supports) |
| Codexの独自エージェント | 個人用 `~/.codex/agents/` またはプロジェクト用 `.codex/agents/` のTOMLが公式の配置方法です。プラグイン内TOMLの自動登録は未確認です | [OpenAI Subagents（2026/10確認）, Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents) |

## 採用した導入方法

この調査後、エージェントの導入方法をClaude CodeとCodexのマーケットプレイスに統一しました。最新の導入・更新・削除の手順と確認済みの範囲は [共通の導入ガイド](agent-plugins.md)を参照してください。

## 手元の確認と次の対応

手元のCodex CLI 0.160.1で一時環境を使い、既存のClaudeカタログとプラグインを変更せずに登録・導入しました。`plugin list --json` で `experiments@my-agent-toolkit` の導入済み・有効化を確認し、app-serverの `skills/list` で `experiments:setup-experiments` と `experiments:run-experiments` が有効なスキルとして認識されました。実際の利用者設定は変更していません。モデルを呼び出す実験フローと4役割の認識は未確認です。

既存のマーケットプレイスと配布物を再利用する方針を採用しました。Codexの4担当は、マーケットプレイスからの導入で動作する構成を検証する必要があります。現在の配布物には、元スキルの [Codex用起動設定](../skills/setup-experiments/agents/openai.yaml) が含まれていないため、明示起動限定の設定を同梱し、意図せずsetupが始まらないことも検証します。これらは実装上の残りの確認事項です。今回更新したのは導入案内であり、Codex向けの動作変更は行っていません。

Codexでは、スキル内の `agents/openai.yaml` に `policy.allow_implicit_invocation: false` を指定すると、暗黙の起動を無効にできます。[OpenAI Skills（公開日不明、2026/10確認）, Optional metadata](https://learn.chatgpt.com/docs/build-skills#optional-metadata)

## 参照資料

[OpenAI Commands, 公開日不明（2026/10確認）] OpenAI. 「Developer commands」. ChatGPT Learn. [CLIコマンド](https://learn.chatgpt.com/docs/developer-commands).

[OpenAI Packaging, 公開日不明（2026/10確認）] OpenAI. 「Package your plugin」. OpenAI Developers. [構成とマーケットプレイス](https://developers.openai.com/plugins/build/plugins).

[OpenAI Conversion, 公開日不明（2026/10確認）] OpenAI. 「Submit your Claude Code plugin to OpenAI」. OpenAI Developers. [Claudeプラグインの移植](https://developers.openai.com/plugins/guides/submit-claude-plugin).

[OpenAI Subagents, 公開日不明（2026/10確認）] OpenAI. 「Subagents」. ChatGPT Learn. [独自エージェント](https://learn.chatgpt.com/docs/agent-configuration/subagents).

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Build skills」. ChatGPT Learn. [スキルの起動設定](https://learn.chatgpt.com/docs/build-skills#optional-metadata).
