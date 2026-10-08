# 取得元の記録

このスキルは、2つの外部スキルの素材を組み合わせたものです。どちらもMITライセンスで、全文を `licenses/` に保存しています。取得日は、どちらも2026-10-08です。

## html(mathbullet/skills)

文書のデザインシステムとコード・数式の規則の取得元です。

| 項目 | 記録 |
| --- | --- |
| 作者 | mathbullet |
| 取得元URL | <https://github.com/mathbullet/skills> |
| 元の配置 | `plugins/html/skills/html/` |
| 取得時点 | v1.0.0、コミット `5ab997fcb8a80da4938bacb0a86cbd568e1018a7`(2026-09-09) |
| 取得元の場所 | Claude Codeのプラグインキャッシュ(`.claude/plugins/cache/skills/html/1.0.0/`)と、同じコミットのマーケットプレイスの複製 |
| 元のライセンス | MIT、Copyright (c) 2026 mathbullet。全文を [licenses/html.txt](licenses/html.txt) に保存しています |
| ライセンスの原本 | 取得時点のリポジトリ直下の `LICENSE`。プラグインのディレクトリには `LICENSE` が含まれていません |

無改変で取り込んだファイルと、取得時のSHA-256です。SHA-256は、ファイルの内容を照合するための値です。Gitで改行形式が変換された場合は、ここに記載した値と異なることがあります。

| ファイル | SHA-256 |
| --- | --- |
| `design-system/component-samples.html` | `E653F6D3BEA377743B51C31EB804D73BEBBCEAFCB6D2B76F664E53081F912C55` |
| `design-system/document.css` | `64016A5EC8DE9792B18E1B221F52BB3294FE946E340F02D44DF76D055D58012D` |
| `design-system/math-copy.js` | `F4AD544FB29BA110F0BBA6C14BEF93FAB056DF778850BB39F0675ACE4118B472` |
| `render-pdf.sh` | `EC951BA8065A46583112CD2565A2F58B1F0E49B54AA94935C0CA22B99E789D6D` |

`SKILL.md` の「デザインシステム」「図」「コード」「数式」「印刷」の規則は、元の `SKILL.md` の規則を取り込んで再構成したものです。独自変更は後述します。

## diagram-design(cathrynlavery/diagram-design)

44種の図の型と、図の共通ルールの取得元です。

| 項目 | 記録 |
| --- | --- |
| 作者 | Cathryn Lavery |
| 取得元URL | <https://github.com/cathrynlavery/diagram-design> |
| 元の配置 | `skills/diagram-design/references/` と `skills/diagram-design/SKILL.md` |
| 取得時点 | v2.6.66、コミット `bd7001e0de50e08f8f13358ed084264ac17ba774`(2026-10-08) |
| 取得元の場所 | Claude Codeのプラグインキャッシュ(`.claude/plugins/cache/diagram-design/diagram-design/2.6.66/`) |
| 元のライセンス | MIT、Copyright (c) 2025 Cathryn Lavery。全文を [licenses/diagram-design.txt](licenses/diagram-design.txt) に保存しています |
| 第三者のライセンス | 取り込んだ範囲には含まれません。取得元の `THIRD_PARTY_LICENSES.md` の対象は、アイコン・ロゴ素材と、プラグインのロゴ用の書体の字形です。どれも同梱していません |

取り込んだファイルは、変換の程度で3種類に分かれます。

| 区分 | ファイル | 内容 |
| --- | --- | --- |
| 機械的な変換と文の削除 | `references/diagrams/type-*.md`(44)、`primitives-core.md`、`semantic-patterns.md` | 配色・書体・参照先の置き換えと、同梱しない機能への言及の削除。本文は英語のままです |
| 書き直し | `style-guide.md`、`layout-budget.md`、`output-spec.md` | 元のファイルを土台に、`html` の配色と文書への組み込みに合わせて日本語で書き直しました |
| 再構成 | `index.md` | 元の `SKILL.md` の §1(方針)・§3(選択)・§4(アンチパターン)・§6(部品)・§7(上限)・§9(点検)・§12(アクセシビリティ)を、日本語で再構成しました |

### 取り込まなかったもの

- 図の取り込み・書き出し・初期設定・プロファイル・環境診断に関する文書とスクリプト(`import-*`、`export*`、`onboarding`、`profiles`、`doctor`、`scripts/`)。図の作成とは別の機能で、スタイルは `html` が固定するためです
- アニメーション、吹き出し注釈、手描き風、ターミナル風、アイコンカタログに関する文書(`animation`、`primitive-annotation`、`primitive-sketchy`、`primitive-terminal`、`primitive-icons`)。静的で黒一色の線画という `html` の規則に合わないか、第三者のブランドロゴを含むためです
- `assets/` の例とテンプレート。元の配色で作られており、取り込むと元の配色が写るためです

## 独自変更

- **配色:** 元の16進値と `rgba` を、`html` の `document.css` の値へ置き換えました。主な対応は次のとおりです

  | 元の役割・値 | 置き換え後 |
  | --- | --- |
  | paper `#f5f5f5`、白 `#ffffff` | `#FFFFFF` |
  | paper-2 `#ececec` | `#FAF9F6` |
  | ink `#2d3142`、`#111111` | `#111110` |
  | muted `#4f5d75` | `#595959` |
  | soft `#7a8399` | `#767676` |
  | rule-solid `#bfc0c0` | `#A5A5A5` |
  | accent `#eb6c36`、`#f7591f`、`#f08a59` | `#D63A2F` |
  | link `#2e5aa8`、`#6a95d8` | `#2990DA` |
  | カテゴリ色(`#b85450`、`#7a8c47`、`#5a7d9a`、`#8c6d3f`、`#c9a23a`、`#4a7c59`) | `#111110`、`#595959`、`#767676`、`#A5A5A5`、`#DFDFDF` のグレー |
  | シリーズ色(`#7c8f6f`、`#5e7a9b`、`#b8915a`、`#9c6b50`、`#6e6479`) | グレーと線種(`style-guide.md` の「シリーズ」) |
  | ダーク用・ターミナル用の値 | 近いグレーまたは `html` の値。ダークは使いません |

- **書体:** Geist を Ubuntu Sans(日本語は Noto Sans JP)、Geist Mono を Ubuntu Mono に置き換えました。Instrument Serif と、韓国語・中国語・キリル文字の節は取り除き、日本語ラベルの節に置き換えました
- **accentの予算:** 「1図に1〜2箇所」を、`html` の「1ページ1箇所」に合わせて文書全体で1箇所にしました。「コーラル」の語は「accent」に置き換えました
- **系列数:** 折れ線・レーダーの系列を5本から4本(focal 1とグレー3)に減らしました。白地で3:1を満たすグレーが3段階しかないためです
- **データ型チップ:** `data-flow`・`process` のチップの色分けをやめ、すべて `ink` 塗りの2文字コードで区別します
- **アイコン:** カタログを同梱しないため、`dp-integration`・`high-level`・`it-state` の `icon` フィールドを取り除き、アイコンなしで描く注記を各型の冒頭に足しました
- **文書への組み込み:** `viewBox` の幅を 908(`.mb-figure-frame` の内側幅に合わせた値)にし、狭い画面で図を横スクロールさせる規則を `output-spec.md` に書きました
- **削除した記述:** `scripts/*.py` の検証スクリプトの説明、`assets/` の例への参照、`Optional motion` と `Examples` の節、ADRへの言及、サイドカーレジストリの記述
- **節番号:** 参照文書の `SKILL.md §N` を、`index.md` の新しい節番号に振り替えました(§1→§1、§3→§2、§4→§3、§6→§4、§7→§5、§9→§6、§12→§7)。読み替えの一覧は `index.md` の §8 にあります
- **追加:** `SKILL.md`、`README.md`、`agents/openai.yaml`、この記録

## 確認状況

導入先の規約に沿って、確認できたことと、確認できていないことを分けて記録します。

### 確認できたこと

- **機械的な確認(2026-10-08):** `skills/html-explainer/` 配下のMarkdownの相対リンクがすべて解決すること。`references/diagrams/` と `SKILL.md` に、置き換え後の配色(`#111110` `#595959` `#767676` `#A5A5A5` `#DFDFDF` `#D63A2F` `#2990DA` `#FFFFFF` `#FAF9F6`)以外の16進値と `rgba` が無いこと。Geist・Instrument Serif・コーラルの語が残っていないこと。上のSHA-256が、無改変のファイルと一致すること
- **試作文書での確認(2026-10-08):** スキルを読んだことのないエージェントに、`SKILL.md` の手順だけで試作文書(注文が確定するまでの仕組み)を作らせました。図は flowchart・architecture・bar の3種、コードブロックと数式を1つずつ含みます。幅1400pxの描画で、コネクタがすべて直角であること、ラベルのマスクと線の間に隙間があること、ラベルがはみ出していないこと、色が黒・灰・青と赤1箇所だけであることは、3つの図の切り出し画像で私も目視しました。幅390pxの結果(本文・表・コードが崩れず、図が枠の中で横スクロールになること)は、試作エージェントの報告で、私は画像を確認していません

### 試作で見つかり、修正したこと

試作で見つかった、指示の矛盾・欠落を修正しました。主なものは、ページ骨格のクラス名と `head` の必須項目の追記、狭い画面の確認方法の追記、ノード寸法の表と最小値の矛盾の解消、`accent` を使えないときの見出し経路(太い `ink` 線とマーカー)の追加、矢印ラベルの配置の矛盾(縦の線分の脇)の解消、`flowchart` の寸法の追記、存在しない参照パスの修正です。修正後の指示で試作をやり直してはいません。

### 確認できていないこと

- **描画して確認した型は、44種のうち flowchart・architecture・bar の3種だけです。** 残りの41種は、配色・書体・参照先の機械的な置き換えと、上の機械的な確認までです。型ごとの座標の式(1000×500 や 960 幅で書かれたもの)を 908 幅へ計算し直す手順は、`index.md` の §8 に方針だけを書いてあり、型ごとには試していません
- **色で意味を分けていた型の読みやすさ:** radar・heatmap・treemap・sankey・venn などで、有彩色をグレーに置き換えたあとに読み取れるかは、描画して確認していません
- **取り込んだCSSの挙動:** 幅390pxで、数式コピーのボタン(右端に絶対配置)が幅の広いディスプレイ数式に重なる現象が、試作で報告されました。`design-system/` は無改変で取り込む方針のため、直していません
- 実機のスマートフォン、Safari・Firefox、印刷・PDF(`render-pdf.sh` はmacOS専用)、スクリーンリーダーの読み上げ、コントラスト比の測定(目視のみ)
