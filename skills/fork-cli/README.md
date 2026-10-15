# fork-cli

メインセッションの会話から、実装または文書作成の1件に必要な範囲だけを分け、選んだ CLI を同じ作業ディレクトリで起動するスキルです。1件の区切りはファイル数ではありません。関連するファイルは複数になってよいです。実装と文書作成の両方が必要なら、呼び出しを分けます。

引き継ぎ先の CLI は、メインセッションが非対話で起動します。完了は、引き継ぎ先が書いた結果ファイルの末尾が `状態: 完了` であることです。プロセスが終了しただけでは完了になりません。

## 前提条件

引き継ぎ先の CLI が導入済みで、ログインなどその CLI の実行に必要な認証が済んでいること。メインセッションと引き継ぎ先が、同じ作業ディレクトリを読めること。サブエージェント機能が無い CLI でも、結果ファイルのパスをメインセッションへ戻して完了を確認できます。

## 使い方

`fork-cli` を指定し、実装か文書作成かと、引き継ぎ先の CLI 名を伝えます。種類か CLI 名が無いときは、ファイルを作る前に質問されます。作業ディレクトリの指定がなければ、カレントディレクトリを使います。

依頼例:

```text
fork-cli を使ってください。
種類は実装です。引き継ぎ先は Gemini CLI です。
この会話で決めたログイン画面のエラー表示だけを実装してください。
```

```text
fork-cli を使ってください。
種類は文書作成です。引き継ぎ先は Claude Code です。
この会話で決めた手順を、利用者向けの Markdown にしてください。
```

実行ごとの記録は、作業ディレクトリの `.fork-cli/<実行ID>/` に残ります。このディレクトリは、利用者がコミットを頼んだとき以外、コミット対象にしません。

エージェント向けの手順は [SKILL.md](SKILL.md)、記録項目は [references/fork.md](references/fork.md)、起動形は [references/clis.md](references/clis.md) にあります。導入手順は [Skillsの導入方法](../../docs/skills-installation.md) にまとめています。

## 呼び出し形式の出典

Codexは `$` とスキル名で明示的に呼び出せます。[OpenAI Skills（2026/10確認）, How ChatGPT and Codex use skills](https://developers.openai.com/codex/skills)

Claude Codeは `/` とスキル名で呼び出せます。[Claude Code Skills（2026/10確認）, Create your first skill](https://code.claude.com/docs/en/skills)

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Agent Skills」. [公式ドキュメント](https://developers.openai.com/codex/skills)

[Claude Code Skills, 公開日不明（2026/10確認）] Anthropic. 「Extend Claude with skills」. [公式ドキュメント](https://code.claude.com/docs/en/skills)
