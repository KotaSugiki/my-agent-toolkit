<!--
MIT License

Copyright (c) 2026 Aichi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-->

# エージェント向け指示

この規約は、人による作業とAIエージェントによる作業に適用します。

## 共通ルール

### コミットメッセージ

先頭行は `<type>(<scope>): <変更内容>` とします。`type` は変更の種類、`scope` は対象です。対象が明確なら、括弧ごと省略できます。変更内容は日本語の短い1行にします。

| type | 用途 |
| --- | --- |
| `feat` | 機能やツール、スキル、プロンプトの新規追加・機能追加 |
| `fix` | 不具合や誤った動作の修正 |
| `docs` | README、利用方法、設計方針などの文書の追加・更新 |
| `refactor` | 動作を変えないコードや構成の整理 |
| `perf` | 実行速度や資源使用量の改善 |
| `test` | テストの追加・修正 |
| `style` | 動作を変えない空白・整形の変更 |
| `build` | 依存関係やビルド方法の変更 |
| `ci` | 継続的インテグレーションの設定変更 |
| `chore` | 上記に当てはまらない保守作業 |
| `revert` | 過去のコミットの取り消し |

- スキルやプロンプト自体の指示を変える場合は、文章であっても機能として扱い、`feat` または `fix` を使います。
- 1コミットには、1つの目的に関係する変更をまとめます。本文は、理由や影響を補足する必要がある場合に記載します。
- 既存の使い方が通用しなくなる変更は、`feat(api)!:` のように `:` の前に `!` を付け、本文の `BREAKING CHANGE:` に影響と移行方法を書きます。

### ブランチの命名

- 作業ブランチは `main` から作成し、`<type>/<short-description>` と命名します。
- `type` はコミットメッセージと同じ種類を使います。説明部分は英小文字・数字・ハイフンで記述します。
- 1ブランチでは1つの目的を扱います。取り込み済みの作業ブランチは削除します。
- 常設ブランチは `main` のみとし、必要になるまでは `develop` やリリース専用ブランチを設けません。

### mainブランチ保護

- ドキュメントや誤字修正を含むすべての変更は、作業ブランチからプルリクエスト（PR）を作成して `main` に取り込みます。`main` への直接pushは許可しません。
- `main` への強制pushと、`main` 自体の削除は禁止します。リポジトリ所有者とAIエージェントにも適用します。
- 取り込む前に差分を確認し、変更に応じた動作確認を行います。取り込み時は、作業中のコミットを1つにまとめる方法（Squash and merge）を基本とします。
- PRの作成とマージは別の操作として扱い、依頼された作業範囲に従います。

### Issue起票とPR作成

GitHubまたはGiteaで操作する前に、次の順で確認します。

1. `git remote -v` で、サービス、接続先ホスト、リポジトリ所有者、リポジトリ名を特定します。複数のリモートがある場合は、依頼された作成先を使います。
2. 認証先のホストとアカウント、対象に必要な権限を確認します。GitHubでは `gh`、Giteaでは `tea` を基本とし、認証済みの連携ツール、Web画面、APIも利用できます。
3. 対象リポジトリの既存Issue・PRを確認し、同じ内容の起票や作成を重複させないようにします。
4. 作成時は対象リポジトリを明示します。PRは、push済みの作業ブランチを変更元、`main` を取り込み先とします。
5. 作成後は番号、URL、本文を確認し、作業報告にURLを記載します。作成先で確認できたものだけを作成済みとして報告します。

- Issueには目的・背景・完了条件を記載します。不具合の場合は、再現手順、期待する動作、実際の動作も記載します。
- 課題や検討事項を記録する必要がある場合にIssueを起票します。小さな修正は、Issueを作らずPRで説明できます。
- PRには解決する問題、変更内容、確認結果、関連するIssueの番号またはURLを記載します。
- タイトルと本文は日本語を基本とします。PRのタイトルはコミットメッセージと同じ形式にします。
- トークンやパスワードは、リポジトリ、Issue本文、PR本文、作業報告に記載しません。
- 利用するCLIの操作やオプションは、そのバージョンのヘルプで確認します。APIを使う場合は、接続先サービスのバージョンに対応した仕様を確認します。
- 認証や権限が不足して作成できない場合は、用意したタイトル・本文と、実行できなかった操作を報告します。ブラウザーでのログインなど利用者の操作が必要な場合は、その操作を依頼します。

### ドキュメントの配置・記述

- 設計、仕様、利用方法などの文書は `docs/` に配置します。ディレクトリの深さは、リポジトリルートから数えて2階層までとします。`docs/` が1階層目、`docs/<分類>/` が2階層目です。
- 最初は `docs/` 直下に置き、関連文書が増えてから分類用のディレクトリを作ります。
- 独自に付けるファイル名・ディレクトリ名は、英小文字・数字・ハイフンを基本とします。`README.md`、`AGENTS.md`、`SKILL.md`、`LICENSE` などの所定の名前や、外部ツールが要求する構成は、その仕様に従います。
- ルートの `README.md` と `AGENTS.md` などの入口ファイルは `docs/` の外に置きます。スキル本体、付属の利用説明、テンプレート、使用例は、それぞれの対象と一緒に配置します。
- 同じルールの本文は1か所に置き、他の文書から参照します。設計・仕様・利用方法には、対象プロジェクトの情報を記載します。
- 文書やディレクトリを移動する場合は、参照リンクも更新します。空ディレクトリの `.gitkeep` は、実際のファイルを追加した時点で削除します。

### 外部由来の素材の記録

外部から取り込むコード、スキル、プロンプトなどには、次の情報を記録します。

- 取得元URL。ローカルから取得した場合は、取得元の場所も記載します。
- 取得日と、分かる場合はバージョン、タグ、コミットなど、取得時点を特定する情報。
- 元のライセンス情報。付属するライセンスや著作権表記は保存します。
- 独自変更の有無と、変更した場合はその概要。

複数ファイルの素材は、同じディレクトリの `provenance.md` に記録します。単体ファイルは冒頭の説明やコメントに記録します。コメントを記載できない形式では付属文書にまとめます。確認できない情報は推測で補わず、「未確認」と記載します。

## このプロジェクトのルール

導入先で、この節に起動・テスト手順、固有の制約、設計・仕様・利用方法の参照先を記載します。
