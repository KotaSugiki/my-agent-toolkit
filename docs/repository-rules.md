# リポジトリの取り扱いルール

コミット・ブランチ・PR・Issueの規約、ドキュメントの配置・記述、外部由来の素材の記録は、[共通ルール](../templates/AGENTS.md)に定めています。この文書は、このツールキット固有の規約と補足説明を扱います。

共通ルールを他のリポジトリへ導入する手順は、[AGENTS.mdの手動導入](agents-installation.md)を参照してください。GitHub・Giteaの操作手順は `github-gitea-operations` スキルにまとめています。規約との役割分担と利用案内は、[Issue起票とPR作成](github-gitea.md)を参照してください。

## GitHub側の保護設定

[共通ルールのmainブランチ保護](../templates/AGENTS.md#mainブランチ保護)に対応するGitHub側の設定は、管理者による保護の迂回も許可しない方針とします。

個人運用のため、他者による承認レビューは必須にしません。必須の自動チェックも現時点では設定しません。自動チェックを導入する際に設定を見直します。

GitHubのブランチ保護は、対象ブランチへのpushやPRに要件を設定する仕組みです。[GitHub Docs（公開日不明、2026/10確認）, About branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#about-branch-protection-rules)

この文書は設定方針を定めるものであり、GitHub側への適用状況は別途確認します。

## 編集元と導入先

ツール、スキル、プロンプトなどの編集元は、このリポジトリとします。共通ルール本文の編集元は `templates/AGENTS.md` に一本化し、このツールキット自身もルートの `AGENTS.md` から参照します。

導入先で修正した内容は、原則として編集元には反映しません。導入先の変更を同期したり、編集元へ戻したりすることは必須にしません。

導入先の変更のうち、リポジトリ所有者が個人的に良いと思ったものだけを選んで採用します。採用する場合は、このリポジトリで変更を行い、共通ルールで定めるPRの手順で取り込みます。AIエージェントは、導入先に変更があることだけを理由に、編集元へ反映しません。

### 種類ごとの導入方法

このリポジトリでは、対象の種類に応じて次の導入方法を採用します。

| 対象 | 導入方法と説明の記載先 |
| --- | --- |
| `templates/AGENTS.md` | 手動でコピーするか、既存のAGENTS.mdへ組み込みます。導入・更新は [AGENTS.mdの手動導入](agents-installation.md)にまとめます |
| `skills/` | `npx skills` を使います。導入手順は [Skillsの導入方法](skills-installation.md)に集約し、各スキルの `README.md` には使い方を記載します |
| `harnesses/` | 各ハーネスの `README.md` に、必要な依存関係の導入、セットアップ、実行方法を記載します |
| `hooks/` | 各フックの利用説明に、対応エージェント、ファイルの配置先、イベントへの登録・解除方法を記載します |
| その他のツール・素材 | 追加時に、各ツール・素材の利用説明へ導入方法を記載します |

`npx skills` を使う方針は、Skillsの導入に適用します。独立したハーネスやフックは、上記の個別の手順で導入します。現時点で中身がないディレクトリは、実際のツールを追加する際に手順を定めます。

## ツールの配置単位

単体で完結するツールは、用途に合うディレクトリに1ファイルとして配置します。複数ファイルで構成するツールは、`<分類>/<名前>/` にまとめます。Skillsは `skills/<名前>/SKILL.md` を基本とし、利用説明や補助ファイルも同じディレクトリに置きます。

## スキルの独立性

各スキルは単独で利用できる構成にします。他のスキルの導入・実行や、別のスキルが生成する文書を前提にしません。実行に必要な補助資料は、同じスキルのディレクトリにまとめます。

## 最低限の利用説明

各ツールには、目的・前提条件・使い方を記載します。単体ファイルは冒頭の説明やコメント、複数ファイルのツールは付属の `README.md` を基本とします。スキルの利用者向け説明は、エージェント向けの指示である `SKILL.md` と分け、付属の `README.md` に記載します。

導入にパッケージマネージャを使う場合は、その前提条件、導入コマンド、導入先、確認方法、更新・削除の方法を説明します。共通の手順は1か所にまとめます。Skillsの導入手順は `docs/skills-installation.md` に記載し、各スキルの `README.md` には導入方法を記載しません。

## 参照資料

[GitHub Docs, 公開日不明（2026/10確認）] GitHub. 「About protected branches」. GitHub Docs. [ブランチ保護の公式ドキュメント](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
