# experiments

Claude Code・Codexのマーケットプレイスで配布する実験支援プラグインです。実験の前提を対話で確認し、計画、実行、評価、簡潔なHTMLレポート、人間のフィードバックを順番に扱います。

## 前提条件

Claude CodeまたはCodexと、対象分野のデータ・実行環境・評価方法を用意します。導入済みのプラグインを使うためにPythonやNode.jsを追加で用意する必要はありません。`html` スキルが利用できればレポート作成に活用し、未導入でもHTMLを作成します。

Codexでは2スキルの認識まで確認済みです。4担当の登録と全体進行は未確認です。対応状況は [共通の導入ガイド](https://github.com/KotaSugiki/my-agent-toolkit/blob/main/docs/agent-plugins.md#前提条件と対応状況)を参照してください。

## Claude Codeでの使い方

前提だけを整理する場合は、Claude Codeのセッションで次のように依頼します。この例はこのプラグイン向けに作成したものです。

```text
/experiments:setup-experiments
このプロジェクトの実験の前提を対話で整理してください。
目標は、処理結果の正しさを保ちながら実行時間を減らすことです。
```

全体進行は次のように依頼します。依頼の範囲を「計画だけ」などに限定することもできます。

```text
/experiments:run-experiments
保存済みの前提と目標値を使い、次の実験を進めてください。
初回・変更した目標値の確認と、レポート後のフィードバックは人間に求めてください。
```

個別の担当を使う場合は、`experiments:experiment-planner`、`experiments:experiment-runner`、`experiments:experiment-analyst`、`experiments:experiment-reporter` の名前と、実験ID・必要な入力の所在を伝えます。プラグインのスキルと担当名にはプラグイン名の接頭辞が付きます。[Claude Code Components（2026/10確認）, Skills / Agents](https://code.claude.com/docs/en/plugins/components)

導入だけでは前提文書を作成しません。計画はMarkdown、レポートは短い要約・グラフ・操作できる詳細を持つHTMLです。実験情報は利用先のプロジェクトへ保存します。

## Codexでの確認

Codexの新しいセッションで `/skills` を開き、`experiments:setup-experiments` と `experiments:run-experiments` の存在を確認します。明示的な呼び出しは `$experiments:setup-experiments` のように指定します。全体進行の動作確認はまだ完了していません。[OpenAI Skills（2026/10確認）, How ChatGPT and Codex use skills](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)

## 導入と保守

導入・更新・削除と公開の手順は、[このツールキットのプラグイン導入ガイド](https://github.com/KotaSugiki/my-agent-toolkit/blob/main/docs/agent-plugins.md)を参照してください。

このディレクトリの `agents/`、`skills/`、`LICENSE` は、ツールキットの共通本文から生成した配布用ファイルです。編集元は `agents/experiments/` と `skills/setup-experiments/` です。配布用ファイルを直接編集せず、生成スクリプトで更新します。マニフェストとこのREADMEは個別に保守します。

## 参照資料

[Claude Code Components, 公開日不明（2026/10確認）] Anthropic. 「Add components to a plugin」. [公式ドキュメント](https://code.claude.com/docs/en/plugins/components)

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Build skills」. [公式ドキュメント](https://learn.chatgpt.com/docs/build-skills)
