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

図の型と、図の共通ルールの取得元です。取得元の44種の型から、利用者の指示(2026-10-08)で次の12種に絞って取り込んでいます。`architecture`、`architecture-delta`、`flowchart`、`sequence`、`timeline`、`swimlane`、`quadrant`、`bar`、`line`、`gantt`、`scatter`、`process` です。

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
| 機械的な変換と文の削除 | `references/diagrams/type-*.md`(12)、`primitives-core.md`、`semantic-patterns.md` | 配色・書体・参照先の置き換えと、同梱しない機能への言及の削除。本文は英語のままです |
| 書き直し | `style-guide.md`、`layout-budget.md`、`output-spec.md` | 元のファイルを土台に、`html` の配色と文書への組み込みに合わせて日本語で書き直しました |
| 再構成 | `index.md` | 元の `SKILL.md` の §1(方針)・§3(選択)・§4(アンチパターン)・§6(部品)・§7(上限)・§9(点検)・§12(アクセシビリティ)を、日本語で再構成しました |

### 取り込まなかったもの

- 図の取り込み・書き出し・初期設定・プロファイル・環境診断に関する文書とスクリプト(`import-*`、`export*`、`onboarding`、`profiles`、`doctor`、`scripts/`)。図の作成とは別の機能で、スタイルは `html` が固定するためです
- アニメーション、吹き出し注釈、手描き風、ターミナル風、アイコンカタログに関する文書(`animation`、`primitive-annotation`、`primitive-sketchy`、`primitive-terminal`、`primitive-icons`)。静的で黒一色の線画という `html` の規則に合わないか、第三者のブランドロゴを含むためです
- `assets/` の例とテンプレート。元の配色で作られており、取り込むと元の配色が写るためです
- 次の32種の型の参照文書。利用者の指示で絞り込みました。`axonometric-plan`、`data-flow`、`db-schema`、`dependency`、`deployment`、`dp-integration`、`dp-security-matrix`、`er`、`exploded`、`fishbone`、`heatmap`、`high-level`、`it-state`、`journey`、`kanban`、`layers`、`loop`、`medallion`、`nested`、`org-chart`、`polar`、`pyramid`、`radar`、`sankey`、`state`、`story-map`、`tree`、`treemap`、`uml-class`、`venn`、`wardley`、`waterfall`
- `type-quadrant.md` の Consultant special(2×2 のシナリオマトリクス)。ドットの背景・赤い象限・11px の説明文が、`html` の規則に合わないためです
- 意味パターン9つのうち、主となる型が外れた6つ(ファンインの待ち行列、非構造の入力から構造化された成果物、ガバナンス・統制カタログ、補完し合うセキュリティ層、追跡可能なブロック分解、ライフサイクルの段階マップ)。残した3つは、段階フレームワーク(`process`)、対のポリシー評価トレース(`flowchart`)、セキュアな舗装路(`architecture`)です

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
- **系列数:** 折れ線の系列を5本から4本(focal 1とグレー3)に減らしました。白地で3:1を満たすグレーが3段階しかないためです
- **データ型チップ:** `process` のチップの色分けをやめ、すべて `ink` 塗りの2文字コードで区別します
- **型ごとの追記:** 9種の `type-*.md`(architecture-delta・sequence・swimlane・timeline・gantt・quadrant・line・scatter・process)の末尾に「html-explainer notes」を足しました。908 幅での寸法の例、`accent` を使えないときの形、日本語ラベルの扱いを書いてあり、本文と食い違う場合はこの節が先に効きます。`type-quadrant.md`・`type-line.md`・`type-scatter.md`・`type-swimlane.md`・`type-timeline.md`・`type-process.md` では、`accent` や5系列を前提にした本文も直しました
- **accent が使えないときの focal:** `style-guide.md` に、箱・線・領域・点・節目・系列ごとの形を足しました
- **矢印とラベル:** 矢印のマーカーに `markerUnits="userSpaceOnUse"` を付け、`ink` 用のマーカー `arrow-ink` を足しました。色付きゾーンの上のラベルのマスクは、そのゾーンの不透明な等価色にする規則と、その値の表を足しました。識別子(`POST /orders` など)は大文字化せず原文のまま書く規則を足しました
- **スクロール枠:** `.diagram-scroll` に `tabindex="0"`・`role="region"`・`aria-label` を付ける規則を `output-spec.md` に足しました
- **フォント:** `SKILL.md` のGoogle FontsのURLに、600のウェイトを足しました(元の `html` は 400・500・700 です)。図のノード名が 600 を指定するためです
- **文書への組み込み:** `viewBox` の幅を 908(`.mb-figure-frame` の内側幅に合わせた値)にし、狭い画面で図を横スクロールさせる規則を `output-spec.md` に書きました
- **削除した記述:** `scripts/*.py` の検証スクリプトの説明、`assets/` の例への参照、`Optional motion` と `Examples` の節、ADRへの言及、サイドカーレジストリの記述
- **節番号:** 参照文書の `SKILL.md §N` を、`index.md` の新しい節番号に振り替えました(§1→§1、§3→§2、§4→§3、§6→§4、§7→§5、§9→§6、§12→§7)。読み替えの一覧は `index.md` の §8 にあります
- **追加:** `SKILL.md`、`README.md`、`agents/openai.yaml`、この記録

## 確認状況

導入先の規約に沿って、確認できたことと、確認できていないことを分けて記録します。

### 確認できたこと

- **機械的な確認(2026-10-08):** `skills/html-explainer/` 配下のMarkdownの相対リンクがすべて解決すること。`references/diagrams/` と `SKILL.md` に、置き換え後の配色(`#111110` `#595959` `#767676` `#A5A5A5` `#DFDFDF` `#D63A2F` `#2990DA` `#FFFFFF` `#FAF9F6`)と、ゾーン上のマスク用に `ink` の薄い塗りを白に重ねた不透明な値(`#FAFAFA` `#F8F8F8` `#F5F5F5` `#F3F3F3` `#F1F1F1`)以外の16進値と `rgba` が無いこと。Geist・Instrument Serif・コーラルの語が残っていないこと。上のSHA-256が、無改変のファイルと一致すること
- **1回目の試作(2026-10-08):** スキルを読んだことのないエージェントに、`SKILL.md` の手順だけで試作文書(注文が確定するまでの仕組み)を作らせました。図は flowchart・architecture・bar の3種、コードブロックと数式を1つずつ含みます。幅1400pxの描画で、コネクタがすべて直角であること、ラベルのマスクと線の間に隙間があること、ラベルがはみ出していないこと、色が黒・灰・青と赤1箇所だけであることを、図の切り出し画像で私も目視しました
- **2回目の試作と使用例(2026-10-08):** 残る9種(sequence・timeline・swimlane・quadrant・line・gantt・scatter・process・architecture-delta)を、スキルを読んだことのないエージェント(1〜3図ずつ)に描かせました。9つの図は、`examples/html-explainer/` の1つの文書にまとめてあります。幅1400pxの描画で、9つの図すべてについて、重なり・はみ出し・斜めのコネクタが見当たらないことを、私が目視しました。赤が図4の focal 系列だけであること、HTMLの `id` が重複せず `aria-labelledby` と `url(#…)` がすべて解決することは、スクリプトで確認しました。幅390pxでは、冒頭から図1までの範囲で、本文が崩れず、図が枠の中で横スクロールになることを、私が画像で確認しました。これで、同梱する12種の型は、基本形をすべて一度は描画して確認したことになります

### 試作で見つかり、修正したこと

1回目の試作では、ページ骨格のクラス名と `head` の必須項目の追記、狭い画面の確認方法の追記、ノード寸法の表と最小値の矛盾の解消、`accent` を使えないときの見出し経路(太い `ink` 線とマーカー)の追加、矢印ラベルの配置の矛盾(縦の線分の脇)の解消、`flowchart` の寸法の追記、存在しない参照パスの修正を行いました。

2回目の試作では、9種の型の参照文書に、908 幅での寸法、`accent` を使えないときの形、日本語ラベルの扱いが書かれていないことが分かりました。多くの図で、各エージェントが同じ箇所を自分で判断していたため、その判断を規則として書き込みました(前述の「独自変更」)。修正後の指示で、使用例の図を描き直してはいません。使用例の図は修正前の指示で描いたもので、四象限図だけ、修正後の規則(軸の両端の「低」「高」)に合わせて手で追記しました。

### 確認できていないこと

- **型の変種:** 描画して確認したのは、各型の基本形です。line・scatter・bar の変種(スロープグラフ、リッジライン、ストリームグラフ、バンプ、バブル、ビースウォーム、ダンベル)は描画していません
- **修正後の指示での作り直し:** 2回目の試作で直した指示を使って、図を描き直した場合の結果は確認していません。細部(矢印のマーカーの大きさ、凡例の位置など)が変わる可能性があります
- **取り込んだCSSの挙動:** 幅390pxで、数式コピーのボタン(右端に絶対配置)が幅の広いディスプレイ数式に重なる現象が、1回目の試作で報告されました。使用例には数式がなく、私は再現していません。`design-system/` は無改変で取り込む方針のため、直していません
- 実機のスマートフォン、Safari・Firefox、印刷・PDF(`render-pdf.sh` はmacOS専用)、スクリーンリーダーの読み上げ、コントラスト比の測定(目視のみ)
