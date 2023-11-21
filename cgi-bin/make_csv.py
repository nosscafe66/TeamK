#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Get_CSV"

import cgi
import cgitb
import sqlite3
import csv
import io
import datetime

cgitb.enable()

DB_NAME = 'TeamK.db'

def make_csv_content(account_table_list):
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_NONE, escapechar='\\')

    # データベースの内容をCSVとして書き込む
    header = ["TaskID", "Task", "DueDate", "MailAddress", "CreatedAt", "Time"]
    writer.writerow(header)
    for data in account_table_list:
        now_str = datetime.datetime.now().strftime('%H:%M:%S.%f')
        writer.writerow(list(data) + [now_str])

    return output.getvalue()

def main():
    try:
        # データベースからデータを取得
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        account_table_list = cur.execute('SELECT * FROM task_tbl').fetchall()
        cur.close()
        conn.close()

        csv_content = make_csv_content(account_table_list)

        # CSVファイルをダウンロードするためのHTTPヘッダー
        print("Content-Type: text/csv")
        print("Content-Disposition: attachment; filename=\"account_list.csv\"")
        print()
        print(csv_content)

    except Exception as e:
        print("Content-Type: text/html")
        print()
        print(f"<html><body><p>Error: {e}</p></body></html>")

if __name__ == "__main__":
    main()