# 取得元の記録

Matt Pocockさんの `wait-what` を日本語向けに翻訳・調整したものです。取得時の原文とライセンスは、以下の固定コミットへのリンクから確認できます。

| 項目 | 記録 |
| --- | --- |
| 作者 | Matt Pocock |
| 取得元 | [mattpocock/skills](https://github.com/mattpocock/skills) |
| 元の配置 | `skills/productivity/wait-what/` |
| 取得日 | 2026-10-02 |
| 取得時のコミット | `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |
| 原文 | [SKILL.md](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/wait-what/SKILL.md) |
| 元のCodex用設定 | [agents/openai.yaml](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/wait-what/agents/openai.yaml) |
| 元のライセンス | MIT。[取得時のLICENSE](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/LICENSE)の全文と著作権表示を、同梱の[LICENSE](LICENSE)に保存しています |

## 独自変更

- `SKILL.md` の説明と本文を日本語化しました。原文のASD-STE100 Simplified Technical Englishで説明する指示を、平易な日本語で説明する指示に置き換えました。一文では一つの内容を扱い、専門用語は初出で説明する指示を追加しました。
- 単独で使える構成にするため、原文にあった `GLOSSARY.md` と `GLOSSARY-MAP.md` への参照を削除しました。会話で使われている言葉と、その意味に合わせて説明する指示に置き換えました。
- スキル名 `wait-what` と、ユーザーが呼び出す方式を維持しました。`disable-model-invocation: true` と `allow_implicit_invocation: false` は変更していません。
- `agents/openai.yaml` の表示名と短い説明を日本語化しました。
- 利用者向けの `README.md` と、この取得元の記録を追加しました。

導入先での変更の扱いは、[リポジトリの取り扱いルール](https://github.com/KotaSugiki/my-agent-toolkit/blob/main/docs/repository-rules.md)に従います。
