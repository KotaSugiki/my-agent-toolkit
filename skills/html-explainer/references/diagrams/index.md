# 図の選び方と共通ルール

`SKILL.md` から参照されます。図の要否・型の選択・共通のルール・点検をまとめます。`type-*.md` と `primitives-core.md` からは、この文書の節番号(§1〜§7)で参照されます。

**この文書の読み順:** §2 で型を選ぶ → 選んだ `type-*.md` を読む → §4 と §3 を守って描く → §6 で点検する。参照文書の古い記述の読み替えは §8 に集めてあります。

## §1 方針

**最も質の高い手は、たいてい削除である。**

- ノードは、それぞれ別の考えを表す。いつも一緒に動く2つのノードは、1つにする
- 接続線は、情報を運ぶ。配置から関係が明らかなら、線を消す
- `accent` は編集上の強調で、警告の旗ではない。文書全体で1箇所に絞る
- 図が完成するのは、足すものがなくなったときではなく、**削れるものがなくなったとき**である

**密度の目安は 10 点中 4。** 技術的に完結していて、案内がなくても読める密度にする。ノードが 9 を超えるなら、たいてい2つの図である。

## §2 図の選び方

### 描くかどうか

描く前に確認する。**この図から読み手が学ぶものは、よく書いた段落より多いか。** 多くなければ描かない。

- 3列の表で同じことが伝わるなら、表にする
- 項目の羅列は、表か箇条書きにする
- 属性だけの前後比較は表にする。構造の変化だけが図になる(アーキテクチャ差分)
- 1つの図形だけの図は、一文で書く
- 単なる直列の手順は、番号付きの説明にする(html の規則)

### 意味パターン → 型

挙動・状態・強制・リスクが意味を担うときは、先に `semantic-patterns.md` を読み、主となるパターンを1つ選ぶ。次に、近い型をレイアウトとして選ぶ。パターンが合わなければ、型を直接選ぶ。

| きっかけ | 意味パターン → 近い型 |
|---|---|
| ファンイン、待ち行列、有限の容量、ボトルネック | ファンインの待ち行列 / ボトルネック → data-flow |
| 段階をまたいで繰り返す 問い・入力・統制・出力 の枠 | 意味の枠を持つ段階フレームワーク → process |
| 会話や雑多な入力が、構造化された永続的な成果物になる | 非構造の入力 → 構造化された成果物 → data-flow |
| 2つのルールの評価に 合格/不合格/スキップ/未到達 と最初の分岐点が要る | 対のポリシー評価トレース → flowchart |
| 信頼境界と、許可・禁止された流入・配備経路 | セキュアな舗装路 → architecture |
| 統制を、強制される場所ごとに整理する | ガバナンス / 統制カタログ → layers |
| 防御が前段の隙を補い、残余リスクが伝わっていく | 補完し合うセキュリティ層 → layers |
| ID で指せる階層分解。ブロックごとの入出力・制約・コードへのリンクが要る | 追跡可能なブロック分解 → tree |
| 1つの対象が、段階・待ち・再試行・取消・終端結果を経て進む | ライフサイクルの段階マップ → state |

パターンはその意味の部品と、より厳しい上限を持つ。型はレイアウトの文法を持つ。

### 型の一覧(44種)

選んだ型の参照文書は、**描く前に必ず読む。**

| 見せたいもの | 型 | 参照 |
|---|---|---|
| ある時点のシステムの部品と接続 | architecture | [type-architecture.md](type-architecture.md) |
| 同期した Before / After の構造変化と変更台帳 | architecture-delta | [type-architecture-delta.md](type-architecture-delta.md) |
| 段階・部門別の旧来のIT構成。移行前の状態 | it-state | [type-it-state.md](type-it-state.md) |
| 分岐のある判断ロジック | flowchart | [type-flowchart.md](type-flowchart.md) |
| 時間順のアクター間メッセージ | sequence | [type-sequence.md](type-sequence.md) |
| 状態・遷移・ガード | state | [type-state.md](type-state.md) |
| エンティティ・項目・関係 | er | [type-er.md](type-er.md) |
| 時間軸上のできごと | timeline | [type-timeline.md](type-timeline.md) |
| 引き継ぎのある部門横断の工程 | swimlane | [type-swimlane.md](type-swimlane.md) |
| 2軸での配置・優先順位付け | quadrant | [type-quadrant.md](type-quadrant.md) |
| 3〜5の定量基準での複数対象の採点 | radar | [type-radar.md](type-radar.md) |
| 周期的なカテゴリ上の1系列(角度=カテゴリ、半径=大きさ) | polar | [type-polar.md](type-polar.md) |
| 最後の段階が最初に戻り、ハブに状態が蓄積する強化サイクル | loop | [type-loop.md](type-loop.md) |
| 包含・スコープによる階層 | nested | [type-nested.md](type-nested.md) |
| 親 → 子の関係 | tree | [type-tree.md](type-tree.md) |
| 人・エージェント・チームの責任・報告・振り分け・エスカレーション | org-chart | [type-org-chart.md](type-org-chart.md) |
| 積み重なった抽象レベル | layers | [type-layers.md](type-layers.md) |
| 1つの物を1軸に沿って分解する(分解・開梱・組立順) | exploded | [type-exploded.md](type-exploded.md) |
| 斜め上から見た1フロア・敷地(家具のある部屋、段階別の建物) | axonometric-plan | [type-axonometric-plan.md](type-axonometric-plan.md) |
| 集合の重なり | venn | [type-venn.md](type-venn.md) |
| 順位のある階層、転換率の減衰 | pyramid | [type-pyramid.md](type-pyramid.md) |
| カテゴリ間の定量比較 | bar | [type-bar.md](type-bar.md) |
| 開始値から終了値へ、符号付きの寄与で橋渡しする | waterfall | [type-waterfall.md](type-waterfall.md) |
| 相対サイズが主題の、全体に対する部分 | treemap | [type-treemap.md](type-treemap.md) |
| クロス集計。値をセルの塗りで表す | heatmap | [type-heatmap.md](type-heatmap.md) |
| 時間の連続的な傾向。2点間の変化、系列ごとの分布、順位の推移 | line | [type-line.md](type-line.md) |
| 時間軸上のタスクと段階 | gantt | [type-gantt.md](type-gantt.md) |
| 2変数の相関・分布。バブル(3変数)、ビースウォーム(1変数) | scatter | [type-scatter.md](type-scatter.md) |
| コンテナ基盤上のデータスタック全体 | high-level | [type-high-level.md](type-high-level.md) |
| データの受け渡しのある、複数アクターの逐次工程 | process | [type-process.md](type-process.md) |
| 品質段階とアクセス方針を持つ多層のデータ保管 | medallion | [type-medallion.md](type-medallion.md) |
| 役割ごとのデータフロー(各工程で誰が何をするか) | data-flow | [type-data-flow.md](type-data-flow.md) |
| データ基盤の接続トポロジ(ソース → 中核 → 利用側) | dp-integration | [type-dp-integration.md](type-dp-integration.md) |
| ロール・部品ごとのアクセス権限の行列 | dp-security-matrix | [type-dp-security-matrix.md](type-dp-security-matrix.md) |
| 段階をまたいで分かれて合流する量(帯の幅=量) | sankey | [type-sankey.md](type-sankey.md) |
| 1つの結果の原因を、カテゴリ別に整理する(根本原因分析) | fishbone | [type-fishbone.md](type-fishbone.md) |
| 価値連鎖と進化段階(作る・買う・動いているもの) | wardley | [type-wardley.md](type-wardley.md) |
| 状態別の仕掛り(WIP上限・ブロックされた項目) | kanban | [type-kanban.md](type-kanban.md) |
| 体験の段階ごとの、人の行動と感情 | journey | [type-journey.md](type-journey.md) |
| ソフトウェアが動く場所(ゾーン・ホスト・成果物・レプリカ・ポート) | deployment | [type-deployment.md](type-deployment.md) |
| 依存関係。ツリーで表せないファンインと循環 | dependency | [type-dependency.md](type-dependency.md) |
| 操作・継承・合成を持つクラス | uml-class | [type-uml-class.md](type-uml-class.md) |
| リリースに切り分けた物語の骨格とカットライン | story-map | [type-story-map.md](type-story-map.md) |
| 物理テーブル: SQL型・制約・索引・列単位の外部キー | db-schema | [type-db-schema.md](type-db-schema.md) |

選び方の目安:

- 2つの型が候補なら、支配的な軸で選ぶ。意味パターンは、その挙動に固有の部品を足すだけで、2つ目のレイアウト文法ではない
- §5 の上限を超えるなら、概要と詳細の2枚に分ける

## §3 共通のアンチパターン

型ごとのアンチパターンは各 `type-*.md` にあります。

| アンチパターン | 失敗する理由 |
|---|---|
| すべてのノードが同じ箱 | 階層が消える |
| 凡例が図の内側に浮いている | ノードとぶつかる |
| 矢印ラベルにマスクがない | 線が文字に透ける |
| 矢印の縦書き(`writing-mode`) | 読めない |
| 影 | 影は使わない。境界線を使う |
| 大きな角丸 | 角丸は 4〜8px か、なし |
| `accent` を重要なノードごとに使う | `accent` は文書全体で1箇所。信号機ではない |
| 有彩色を足す | 有彩色は `accent` と `link` だけ(html) |
| 絵文字や矢印文字を図記号に使う | 記号は SVG で描く(html) |
| Mermaid の描画結果の配置をそのまま再現する | 自動配置と経路をそのまま持ち込んでしまう |
| §4 のコネクタ6規則に1つでも反する | **自動的に不合格**: 斜めの線、線に触れるラベル、後から描くノードに隠れるマスク、重なる経路、共有する接続点、端点でない箱の裏を通る経路 |

## §4 コアのSVG部品

部品の正確なマークアップと、各規則の詳細は [`primitives-core.md`](primitives-core.md) にあります。

- **矢印:** 既定は `muted`。見出しとなる経路は `accent`(文書の `accent` を図で使わないときは、太さ 2 の `ink` と `arrow-ink`)、HTTP/API・外部への呼び出しは `link`、任意・受動・戻り・非同期は破線 `5,4`。**矢印は箱より先に描き**、線が箱の背後に回るようにする
- **ノードの箱:** 不透明な `paper` のマスク矩形、`rx=6` の装飾した箱、矩形(`rx=2`、錠剤型でない)の種別タグ、sans 600 の名前、mono の副ラベル

### コネクタ6規則(必須)

交渉の余地はありません。§6 で1つずつ確認します。詳細と例外は [`primitives-core.md`](primitives-core.md) にあります。

1. **直角のみ。** 軸のずれた2ノード間は `r=8`(狭い配置では `r=6` まで)の丸い直角のエルボーにする。直線の `<line>` は両端が同じ x か y を共有する場合だけ。斜めは不合格
2. **ラベルの間隔。** すべての矢印ラベル(14文字以内の大文字、日本語は8文字以内。線分の中央。240px を超える線分では始点から 80px 以内)は不透明なマスクの上に置き、線との間に 6〜10px の隙間を空ける。縦の線分では線の脇に置き、線の上には置かない
3. **重ならない。** 経路を共有・重ねない。平行する経路は 12px 以上離し、1点で交差するときは橋(ホップ)を使う
4. **接続点を分ける。** 箱の同じ辺に出入りするコネクタは、それぞれ `L * k / (N + 1)` の自分の点を持ち、12px 以上離す(非常に小さい箱では 8px)
5. **端点でない箱の裏を通らない。** 迂回させる。箱が幾何学的に避けられない場合のみ、破線(`4,3`)にし、ラベルは見える側の端に置き、途中の箱にマーカーを付けない
6. **マスクを先に描く。** ラベルのマスクは、後から描くノードと重ならない。ノードの内側に完全に収まるバッジのマスクと、先に描くゾーンに重なるマスクは構わない

## §5 寸法と上限

構造の寸法は4pxグリッドに載せます(ノードの原点・幅・高さ・間隔・余白は4の倍数)。使える値、文字サイズの階層、例外は [`layout-budget.md`](layout-budget.md) と [`output-spec.md`](output-spec.md) にあります。

| 項目 | 上限(図1枚) |
|---|---|
| ノード | 9 |
| 矢印・遷移 | 12 |
| `accent` の要素 | 文書全体で1 |
| 注釈の吹き出し | 0 |

型ごとの上限は [`layout-budget.md`](layout-budget.md) にあります。超えるときは、図を2枚に分けます(概要と詳細)。

## §6 点検

図を文書へ入れる前に実行します。

**型の適合**

- [ ] 挙動が主題なら、型より先に意味パターンを1つ選び、`semantic-patterns.md` を読んだか
- [ ] レイアウトに合う型を選んだか(§2)
- [ ] 表や段落で足りないか。足りるなら描かない
- [ ] 選んだ型の `type-*.md` を読んだか

**削除テスト**

- [ ] 削れるノードはないか(読み手は理解できるか)
- [ ] 統合できるノードはないか(いつも一緒に動いていないか)
- [ ] 削れる矢印はないか(配置から関係が明らかではないか)
- [ ] 削れるラベルはないか(色や形がすでに伝えていないか)

**信号**

- [ ] `accent` は文書全体で1箇所以内か
- [ ] 凡例は、図の中で意味が自明でない線種・記号・塗りをすべて含み、余計なものを含まないか(矢印の向きと名前だけで足りる図では省略してよい)
- [ ] 型の上限(§5)に収まっているか

**技術**

- [ ] `<svg>` に `role="img"` と、`<title>` と `<desc>` に解決する `aria-labelledby` があるか(§7)
- [ ] `<title>` は `<svg>` の最初の子で、`<defs>` より前か。`<title>` と `<desc>` の ID は図ごとの接頭辞付きか
- [ ] 矢印を箱より先に描いたか
- [ ] **規則1:** 軸のずれたコネクタは `r=8` のエルボーで、斜めの線がないか
- [ ] **規則2:** すべてのラベルのマスクと線の間に 6〜10px の隙間があるか
- [ ] **規則3:** 重なるコネクタがなく、交差には橋があるか
- [ ] **規則4:** 共有する辺で、コネクタごとに別の接続点(12px 以上)を持つか
- [ ] **規則5:** 端点でない箱の裏を通らないか(避けられない場合は破線で、ラベルは見える端か)
- [ ] **規則6:** ラベルのマスクが、後から描くノードと重なっていないか
- [ ] すべての矢印ラベルの背後に、不透明な `fill="#FFFFFF"` の矩形があるか
- [ ] 凡例は下端の水平な帯か。`writing-mode` の縦書きがないか
- [ ] `viewBox` の幅は `908`、`min-width` は `viewBox` の幅と等しく、SVG は `.diagram-scroll` の中にあるか([`output-spec.md`](output-spec.md))
- [ ] ノードの原点・寸法・間隔・余白は4の倍数か。文字サイズは役割の値か
- [ ] ブラウザで描画して確認したか(ラベルがはみ出していないか、色が黒・赤・青だけか)

**書体**

- [ ] 人が読む名前は sans、技術的な副ラベル(ポート、コマンド、URL)は mono か
- [ ] 日本語のラベルは 12px 以上か。矢印ラベルは 12px の sans に切り替えたか
- [ ] 表題や吹き出しを図に描いていないか(文書の見出しと `figcaption` に任せる)

## §7 アクセシブルな SVG

すべての図はアクセシブルな図として作ります。詳細は [`primitives-core.md`](primitives-core.md) にあります。

1. `<svg>` に `role="img"` と、`<title>` と `<desc>` を指す `aria-labelledby` を付ける
2. `<title>` は `<svg>` の最初の子で、`<defs>` より前に置く
3. ID は図ごとに `<slug>-title` / `<slug>-desc`(例: `order-flow-title`)とし、裸の `title` / `desc` は使わない。文書全体で一意にする
4. `<title>` は対象の短い名前(60文字以内。文書の見出しに近いもの)
5. `<desc>` は図の内容を1文で述べる。形ではなく内容を書く
6. 装飾だけの SVG は `aria-hidden="true"` にする

## §8 参照文書の読み替え

`type-*.md`・`primitives-core.md`・`semantic-patterns.md` は、元の diagram-design の文面を保っています。次の記述は、このスキルでは読み替えます。

| 参照文書の記述 | 読み替え |
|---|---|
| `accent` 1〜2個、`≤ 2 accent elements`、`exactly two focal components` など | 上限であり、文書全体で1個以内が先に効く。2個を求める型は1個に絞り、残りは `ink` の太線・位置・ラベルで示す(`style-guide.md`) |
| 5系列(radar・line) | 4系列(focal 1 + グレー3)。色でなく線種でも区別する(`style-guide.md`) |
| カテゴリ別の `color: "#hex"` と、色名(rust-red など) | `style-guide.md` の「カテゴリ色」のグレー。意味はラベルで伝える |
| `dark` の列、`C_light`、terminal skin | 使わない。ライトのみ |
| `icon` フィールド(dp-integration・high-level・it-state) | アイコンカタログは同梱していない。省略する |
| `assets/example-*.html`、`scripts/*.py`、`animation.md`、`primitive-*.md`、`onboarding.md`、`export*.md` | 同梱していない。検算は手で行う。`data-*` 属性は検算用の宣言で、付けても付けなくてもよい |
| `viewBox` が `960` 幅の例 | `908` 幅で座標を計算し直す(`output-spec.md`) |
| 表題・注釈の吹き出し・サマリーカード・フッター | 図に描かない。文書の見出し・`figcaption`・コンポーネントを使う |
| 「shipped example」への言及 | 同梱の例はない。数値だけを参考にする |
| `1000×500`・`960` 幅などの座標の例 | `908` 幅で、本数・列数・段数で割って4の倍数に丸め、座標を計算し直す |
| ラベルの文字サイズ(11px など)と高さ(12px) | 日本語は 12px 以上、ラベルの高さは 16px。12px の高さを前提にした余白の式は 16px で計算し直す |
| 縦軸のタイトル | 軸の外側(x が 40 以上)に `transform="rotate(-90 x y)"` で置いてよい。禁止されているのは `writing-mode` の縦書き |
| flowchart の「Yes は右、No は下」 | 主な流れを下へ続ける頂点を主経路にし、ほかの出口は空いている頂点から出す。すべての出口にラベルを付ける |
