---
name: html-explainer
description: 概念・仕組み・調査内容を、図解(インラインSVG)入りのHTML説明文書として作成・編集します。
disable-model-invocation: true
---

# 図入りのHTML説明文書

概念・仕組み・調査内容を、ビルドなしでブラウザが直接描画できるHTML文書にします。文書は同梱の `design-system/` で組み、図は `references/diagrams/` の規則でインラインSVGとして描きます。このスキルだけで利用できます。

文書の規則と図の規則が衝突したら、**文書の規則が勝ちます**。色・書体・赤の予算・記号は下の「デザインシステム」に従い、コネクタ・上限・ラベルのマスクの幾何は `references/diagrams/` に従います。

## 手順

1. **対象を確かめる。** 説明する内容、読者、保存先を確かめる。不明な点は利用者に尋ねる。保存先の指定がなければ現在の作業ディレクトリへ保存する。ファイル名は `{yyyymmdd}-{内容を表すケバブケース}.html`で、既存ファイルの更新では名前を変えない
2. **構成を決める。** 背景と要点、本論、具体例、補足・限界の順にする。h1 とリード文の後に `.mb-toc` の目次を置き、各 h2 に対応する `id` を付ける。専門用語は本文の初出で定義する。複数箇所から参照する用語がある場合だけ `aside.mb-glossary` の用語リストを設ける(正解例は `design-system/component-samples.html`)
3. **図にする箇所を決める。** 候補ごとに [index.md](references/diagrams/index.md) §2 の「描くかどうか」で確かめる。段落・表・番号付きの説明で足りる箇所は描かない。原典に重要な図があるなら、出所を示して引用し、模倣図を作らない
4. **図を描く。** 次の順で進める。完了条件は、[index.md](references/diagrams/index.md) §6 の点検の全項目を満たすこと
   1. [index.md](references/diagrams/index.md) の型の一覧と意味パターンから、型を選ぶ
   2. 選んだ `references/diagrams/type-*.md` を読む。型の記述が [index.md](references/diagrams/index.md) §8 の読み替えの対象なら、その表に従う
   3. [style-guide.md](references/diagrams/style-guide.md) のトークンと [output-spec.md](references/diagrams/output-spec.md) の組み込み(`.mb-figure` / `.mb-figure-frame` / `.diagram-scroll`、`viewBox` 幅 908)で描く
5. **文書を仕上げる。** `design-system/` を成果物の隣へコピーし、下の読み込みを書く。コード、数式、表、引用は下の規則に従う
6. **ブラウザで確認する。** ヘッドレスブラウザなど使える手段で描画し、スクリーンショットで見る。確かめる点は、図のラベルがはみ出していないこと、コネクタが直角で線がラベルに触れていないこと、有彩色が赤とリンク青だけ(グレーは可)であること、赤の強調(コードのシンタックスハイライトを除く)が文書全体で1箇所以内であることである。文字の縁に色が付いて見えるのは、ClearType などの描画によるにじみで、色の違反ではない。幅 1400px と、狭い画面の幅 390px の2通りで撮る。ヘッドレスChromeの窓幅は約500pxで下げ止まるため、390px は幅 390px の `iframe` を置いた使い捨てのHTMLを撮る(高さも指定する。例: 2600px)。狭い画面では図の一部が枠の外になり、横スクロールで見る仕様である。そのため、図だけに情報を置かず、要点を本文にも書く。使える手段がなければ、確認できなかったと報告する
7. **報告する。** 保存先のパス、図の種類と枚数、赤の強調の位置、確認できなかったことを簡潔に伝える。PDF化は利用者から明示的に頼まれた場合だけ、`render-pdf.sh <html-file>` を実行する(macOSとGoogle Chromeが必要)

## デザインシステム

作成前に `design-system/component-samples.html` を確認します。コンポーネントは `design-system/document.css`、数式コピーは `design-system/math-copy.js` が正です。利用者が共有アセットのパスを指定した場合は、そのパスを優先します。

`<head>` は次の読み込みを含めます。`charset`、`viewport`、`title` も必須です。`viewport` がないと、スマートフォンで図の横スクロールの設計が働きません。

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>文書の題名</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Ubuntu+Sans:wght@400;500;600;700&family=Noto+Sans+JP:wght@400;500;600;700&family=Ubuntu+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./design-system/document.css">
<script src="./design-system/math-copy.js"></script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js"></script>
<script>document.addEventListener("DOMContentLoaded", () => hljs.highlightAll());</script>
```

- ページ骨格は `component-samples.html` と同じ構造にする。`html lang="ja"` の `body` に `.mb-page` を置き、その中に `.mb-hero`(`header.mb-header` の h1、`p.mb-lede` のリード文、`nav.mb-toc`、必要なら `.mb-summary`)と `.mb-wrap`(`main.mb-main` と、用語リストを置く場合は `main` の兄弟の `aside.mb-glossary`)を並べる
- 背景は `#FAF9F6`。部品は白地、黒罫線、角丸を基本とする
- 自然言語は Ubuntu Sans と Noto Sans JP、コード・URL・日付は Ubuntu Mono を使う
- 有彩色はリンク青 `#2990DA` とアクセント赤 `#D63A2F` に限る。赤い強調は、図を含めて1ページ1箇所までとする
- シンタックスハイライトとコード差分の色は、意味を区別する機能色としてこの制限の対象外とする
- 絵文字や矢印文字を図記号に使わない。必要な記号はインラインSVGで描く
- 引用は `.mb-quote` を使い、原文と訳文を同じ文字サイズ・色で上下に並べる
- `.mb-chip` は並列の固有名や分類名の列挙にだけ使う
- 表は短い対応関係に使い、3列までを基本とする。行見出しのセルには `.mb-rowlabel` を付ける
- ページ固有の `<style>` は図の配置調整など最小限にとどめる

### 図

- `.mb-figure` は、画像・SVGなどの視覚資料とキャプションを1つにまとめる外枠である。特定の図形を意味しない。`.mb-figure-frame` は視覚資料の表示面、`figcaption` は図番号・説明・出所に使う
- 自作図はインラインSVGで、黒一色の線画を基本とする。アスキーアートを使わない
- ノード数が多い場合は縦方向を優先する。矢印が交差する構成を避ける
- 単なる直列手順は、図にせず番号付きの説明にする

### コード

- Highlight.js を必ず読み込む。`pre code` には `language-javascript`、`language-python`、`language-html` などの言語クラスを付け、ハイライトしないテキストには `language-plaintext` を付ける
- 独自の色付けをせず、`document.css` の `.hljs-*` 規則を使う
- コード差分は `pre.mb-diff` を使い、`code` に `nohighlight` を付ける。変更理由を散文で説明してから、必要な断片を示す

### 数式

- MathJax 3 を使う。インライン数式は `$...$`、ディスプレイ数式は `$$...$$` とする
- ベクトルと行列は `\boldsymbol{...}`、名前付きの演算は `\mathtt{...}` を使い、スカラー・添字・集合名は装飾しない。標準の LaTeX コマンド(`\exp`、`\sum`、`\mathbb{E}` など)はそのまま使う。`component-samples.html` は `\mathrm{softmax}` と書いているが、迷ったら `\mathtt` に揃える
- ページ側で `window.MathJax` を再定義しない。未知のコマンドを別記法へ置き換えない

### 印刷

印刷対応は `document.css` の `@media print` を使います。図の横スクロールを解除する規則は [output-spec.md](references/diagrams/output-spec.md) にあります。

## 文章

文章の書き方は、導入先の規約と利用者の指示に従います。`ja-text-communication` など、文章の書き方を整えるスキルがあれば併用できますが、必須ではありません。
