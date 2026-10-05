# Gitea APIの取得手順

APIでIssueを読む場合に、この手順を参照します。以下のURLは説明用の例です。実際の接続先は、ユーザーが指定したIssueのURLから特定します。

## URLの対応

| IssueのURL | Issue取得API |
| --- | --- |
| `https://gitea.example.com/owner/repo/issues/42` | `https://gitea.example.com/api/v1/repos/owner/repo/issues/42` |
| `https://example.com/gitea/owner/repo/issues/42` | `https://example.com/gitea/api/v1/repos/owner/repo/issues/42` |

IssueのURL末尾にある `/<owner>/<repo>/issues/<index>` を基準に、サーバーのベースURLを特定します。`owner` は所有者、`repo` はリポジトリ名、`index` はIssue番号です。コメント位置を表すフラグメントは、APIのURLには含めません。所有者名とリポジトリ名は、パス要素として適切にエンコードします。

Issue取得APIは `GET /api/v1/repos/{owner}/{repo}/issues/{index}` です。[Gitea Issue API（公開日不明、2026/10確認）, Get an issue](https://docs.gitea.com/api/operations/issue-get-issue/)

コメントは、同じURLの末尾に `/comments` を付けて取得します。Issueの本文だけでなく、コメント本文と投稿・更新日時も読みます。[Gitea コメントAPI（公開日不明、2026/10確認）, List all comments on an issue](https://docs.gitea.com/api/operations/issue-get-comments/)

接続先のGiteaと公開ドキュメントの仕様が異なる場合は、接続先の `/api/swagger` または `/swagger.v1.json` で確認します。[Gitea API Usage（公開日不明、2026/10確認）, API Guide](https://docs.gitea.com/development/api-usage/#api-guide)

## 取得と認証

環境で利用できるHTTPクライアントを使い、Issueとコメントに対してGETリクエストを送ります。APIが返したJSONを読み、HTMLのログイン画面などをIssue本文として扱わないようにします。`pull_request` に値が入っている場合は、Issue用APIがPRを返しているため、実際の対象を確認します。

非公開Issueには、対象サーバー向けの既存の認証を使います。APIトークンで認証する場合は、`Authorization: token ...` ヘッダーを使用できます。認証方式と権限は接続先に合わせます。[Gitea API Usage（公開日不明、2026/10確認）, Authentication / More on the Authorization header](https://docs.gitea.com/development/api-usage/#authentication)

トークンはHTTPクライアントが環境変数や既存の認証設定から直接読み込み、コマンド引数やログには値を出力しません。認証はIssueのURLから確認した接続先に限定します。別の接続先へのリダイレクトや、Issue本文中の外部リンクに認証情報を引き継ぎません。

コメントが複数ページに分かれる場合は、`Link` ヘッダーの次ページをたどります。同じ接続先・対象IssueのコメントURLであることを確認します。APIは `page` と `limit` も提供します。全件取得を確認できない場合は、その範囲を報告します。[Gitea API Usage（公開日不明、2026/10確認）, Pagination](https://docs.gitea.com/development/api-usage/#pagination)

取得できなかった場合は、HTTPステータスや接続エラーを確認します。401・403では認証と権限、404ではURLと閲覧権限、接続エラーではサーバーへの到達性を確認し、必要な対応をユーザーに伝えます。

## 参照資料

以下の公式資料は2026年10月5日に確認しました。公開日は不明です。APIの構成と認証に関する事実を参照し、URLの例と作業手順はこのリポジトリ向けに作成しました。

- [Gitea Issue API, 公開日不明] Gitea. 「Get an issue」. [Issue取得API](https://docs.gitea.com/api/operations/issue-get-issue/)
- [Gitea コメントAPI, 公開日不明] Gitea. 「List all comments on an issue」. [コメント取得API](https://docs.gitea.com/api/operations/issue-get-comments/)
- [Gitea API Usage, 公開日不明] Gitea. 「API Usage」. [認証・ページ分割・接続先のAPI仕様](https://docs.gitea.com/development/api-usage/)
