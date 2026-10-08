# html-explainer

概念・仕組み・調査内容を、図解入りのHTML説明文書として作成・編集するスキルです。文書は [mathbullet/skills](https://github.com/mathbullet/skills) の `html` のデザインシステムで組み、図は [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) の44種の型の規則で、文書と同じ配色・書体のインラインSVGとして描きます。両方の素材を同梱しているため、このスキルだけで利用できます。

## 前提条件

導入先のファイルを読み書きできるClaude CodeまたはCodexを使います。生成したHTMLは、ビルドなしでブラウザから開けます。

- 書体(Google Fonts)、数式(MathJax)、コードの色付け(highlight.js)は外部から読み込みます。オフラインでは、書体が代替になり、数式とコードの色付けは働きません
- PDF化(`render-pdf.sh`)は、macOSとGoogle Chromeが必要です。利用者が明示的に頼んだときだけ実行します
- 描画結果の確認には、ヘッドレスブラウザなどが使える環境が必要です。使えない場合、スキルは確認できなかったと報告します

## 使い方

Codexでは `$html-explainer`、Claude Codeでは `/html-explainer` を指定し、説明したい内容を伝えます。導入しただけでは起動しません。次はこのツールキット用に作成した依頼例です。

```text
html-explainerを使って、注文が確定するまでの仕組みを説明するHTML文書を作ってください。
読者はバックエンド開発の新人です。判断の流れと構成要素を図にしてください。
```

スキルは、内容・読者・保存先を確かめてから、構成を決めます。図にする箇所は、段落や表で足りないものだけを選びます。型を選び、その型の参照文書を読んで描き、ブラウザで描画して確かめます。保存先の指定がなければ、現在の作業ディレクトリに `{yyyymmdd}-{内容を表すケバブケース}.html` で保存し、隣に `design-system/` を置きます。作成例は [examples/html-explainer](../../examples/html-explainer/README.md) にあります。

## 構成

| パス | 内容 |
| --- | --- |
| `SKILL.md` | 手順と、文書のデザインシステム、コード・数式の規則 |
| `design-system/` | 文書のCSS、数式コピーのJavaScript、コンポーネント集。`html` から無改変で取り込んだもの |
| `references/diagrams/` | 図の選び方(`index.md`)、配色・書体(`style-guide.md`)、組み込み方(`output-spec.md`)、型ごとの上限(`layout-budget.md`)、コネクタなどの部品(`primitives-core.md`)、意味パターン、44種の型の参照文書(`type-*.md`) |
| `render-pdf.sh` | HTMLをPDFにするスクリプト。`html` から無改変で取り込んだもの |
| `licenses/` | 2つの取得元のMITライセンス全文 |
| `provenance.md` | 取得元、取得時点、独自変更の記録 |

## 範囲と制約

- **配色は `html` に合わせています。** 図は黒一色の線画で、有彩色は赤とリンク青だけです。赤い強調は、図を含めて文書全体で1箇所です。元の `diagram-design` が色で区別していた系列やカテゴリは、濃淡と線種に置き換えているため、折れ線・レーダーの系列は最大4本です
- **44種の型を同梱していますが、実描画で確認した型は flowchart・architecture・bar の3種です。** 残りは配色・書体・参照先の機械的な置き換えまでで、描画しての確認はこれからです。詳細は [provenance.md](provenance.md) に記録しています
- **狭い画面では、図が枠の中で横スクロールになります。** スキルは、図だけに情報を置かず、要点を本文にも書くよう指示します
- **幅の狭い画面で、数式コピーのボタンが幅の広い数式に重なると報告されています。** 取り込んだ `document.css` の配置(右端に絶対配置)による挙動で、無改変のため直していません
- **アイコンのカタログは同梱していません。** `dp-integration`、`high-level`、`it-state` はアイコンなしで描きます
- **型の参照文書は、元の英語のままです。** 配色・書体・参照先を機械的に置き換え、同梱しない機能への言及を取り除いています。読み替えは `references/diagrams/index.md` の §8 にまとめています
- **上流の更新には追従しません。** 取得時点のスナップショットです。導入先での変更の扱いは [リポジトリの取り扱いルール](../../docs/repository-rules.md)に従います

導入手順は [Skillsの導入方法](../../docs/skills-installation.md)にまとめています。取得元とライセンスは [provenance.md](provenance.md) と `licenses/` を参照してください。

## 呼び出し形式の出典

Codexは `$` とスキル名で明示的に呼び出せます。[OpenAI Skills（2026/10確認）, How ChatGPT and Codex use skills](https://developers.openai.com/codex/skills)

Claude Codeは `/` とスキル名で呼び出せます。[Claude Code Skills（2026/10確認）, Create your first skill](https://code.claude.com/docs/en/skills)

[OpenAI Skills, 公開日不明（2026/10確認）] OpenAI. 「Agent Skills」. [公式ドキュメント](https://developers.openai.com/codex/skills)

[Claude Code Skills, 公開日不明（2026/10確認）] Anthropic. 「Extend Claude with skills」. [公式ドキュメント](https://code.claude.com/docs/en/skills)
