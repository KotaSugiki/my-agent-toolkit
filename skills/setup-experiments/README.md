# setup-experiments

実験プロジェクトの目標と、繰り返し使うデータ・環境・実行方法・制約を、対話で確認して保存するスキルです。既存リポジトリの初回整理、新規プロジェクトの準備、前提の更新に使います。導入しただけでは前提文書の作成を始めません。

## 前提条件

導入先のファイルを読み書きできるClaude CodeまたはCodexを使います。分野の知識、実行方法、評価方法は、コード・設定・ドキュメントまたは利用者から与えます。実験支援エージェントは必須ではありません。

## 使い方

Codexでは `$setup-experiments`、Claude Codeでは `/setup-experiments` を指定し、目的を伝えます。次はこのツールキット用に作成した依頼例です。

```text
setup-experimentsを使って、このリポジトリの実験の前提を整理してください。
コードとドキュメントを先に調べ、調査結果を提示して対話で前提を確認してください。
目標は、処理結果の正しさを保ちながら実行時間を減らすことです。
```

明示的に呼び出した後、既存ファイルを調べ、目的・範囲と保存先について質問します。回答が届くまで前提文書を作成・更新しません。調査済みの情報は候補として示すため、同じ情報を入力し直す必要はありません。

既定の保存先は `docs/experiment-project.md` です。目的・範囲と保存先への回答後は、確認した内容を順次保存しながら、残る項目を少数ずつ確認します。途中の文書は「対話中」とし、全項目の内容または未準備・該当なしの理由を確認できたら「確認済み」にします。未準備のデータや環境も、その状態と必要な作業を記録できます。実験を実行できるかは別に判定します。

このスキルは「何を実現したいか」を保存します。評価指標・目標値は実験計画で決め、`docs/experiment-targets.md` へ分けて保存します。条件や仮説だけを変える次の実験では、保存情報を引き継ぎます。

更新時は「データと実行環境が変わったので、保存済みの前提を更新してください」のように変更理由を伝えます。既存の実験記録と目標値は保持します。

項目は [記録形式](references/records.md)、4担当と親の使い方は [実験支援エージェント](../../agents/experiments/README.md)を参照してください。導入手順は [Skillsの導入方法](../../docs/skills-installation.md)にまとめています。

エージェントとまとめて導入する場合は、Claude CodeまたはCodexのマーケットプレイスから [experimentsプラグイン](../../plugins/experiments/README.md)を追加します。手順と対応状況は [エージェントの導入方法](../../docs/agent-plugins.md)を参照してください。プラグインからの呼び出し名は、Claude Codeが `/experiments:setup-experiments`、Codexが `$experiments:setup-experiments` です。

## 呼び出し形式の出典

Codexは `$` とスキル名で明示的に呼び出せます。[OpenAI Skills（2026/10確認）, How ChatGPT and Codex use skills](https://developers.openai.com/codex/skills)

Claude Codeは `/` とスキル名で呼び出せます。[Claude Code Skills（2026/10確認）, Create your first skill](https://code.claude.com/docs/en/skills)

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Agent Skills」. [公式ドキュメント](https://developers.openai.com/codex/skills)

[Claude Code Skills, 公開日不明（2026/10確認）] Anthropic. 「Extend Claude with skills」. [公式ドキュメント](https://code.claude.com/docs/en/skills)
