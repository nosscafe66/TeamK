#!/usr/bin/env python3
import cgi
import cgitb
import csv
import io
import os  # ユーザーエージェントを取得するために必要
import sqlite3
import datetime

cgitb.enable()

DB_NAME = 'TeamK.db'

def is_mobile_device(user_agent):
    # 簡易検出ルール; 実際にはもっと詳細なチェックが必要
    return 'mobi' in user_agent.lower()

def download_csv(account_table_list):
    output = io.StringIO()
    writer = csv.writer(output)

    # データベースの内容をCSVとして書き込む
    header = ["TaskID", "Task", "DueDate", "MailAddress", "CreatedAt", "Time"]
    writer.writerow(header)
    for data in account_table_list:
        writer.writerow(list(data) + [datetime.datetime.now().strftime('%H:%M:%S.%f')])

    csv_output = output.getvalue()
    output.close()

    # HTTPヘッダーを設定
    print("Content-Type: text/csv")
    print("Content-Disposition: attachment; filename=\"account_list.csv\"")  # または動的なファイル名
    print()
    print(csv_output)

def main():
    user_agent = os.environ.get('HTTP_USER_AGENT', '')

    # データベースからデータを取得
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT * FROM task_tbl')
    account_table_list = cur.fetchall()
    cur.close()
    conn.close()

    if is_mobile_device(user_agent):
        # スマートフォンの場合は、CSVをダイレクトにダウンロード
        download_csv(account_table_list)
    else:
        # PCの場合、既存の処理を実行（ファイルを保存し、リンクまたはリダイレクトを提供）
        # ...（既存の処理）...
        pass  # ここで適切な処理を実装してください。

if __name__ == "__main__":
    main()
