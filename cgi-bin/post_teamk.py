#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "{yourname} <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__ = "02 09 2023"
__productname__ = "Register Task Data"

import cgi
import cgitb
import sqlite3
import sys
import codecs

cgitb.enable()
print("Content-Type: text/html; charset=utf-8")
print()

DB_NAME = 'TeamK.db'
TABLE_NAME = "task_tbl"

def connect_db():
    """データベースへの接続を確立し、コネクションを返します。"""
    return sqlite3.connect(DB_NAME)

def register_data(conn, task_description, due_date, mailaddress, created_at):
    """タスクをデータベースに登録します。"""
    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO {} (task, due_date, mailaddress, created_at) VALUES (?, ?, ?, ?)'.format(TABLE_NAME),
                    (task_description, due_date, mailaddress, created_at))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
        conn.rollback()  # トランザクションのロールバック
        sys.exit(1)  # エラーが発生した場合、スクリプトを終了します。
    finally:
        cur.close()

def delete_task(conn, task_id):
    """指定されたIDのタスクをデータベースから削除する"""
    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM {} WHERE task_id = ?'.format(TABLE_NAME), (task_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        conn.rollback()
        sys.exit(1)
    finally:
        cur.close()

def main():
    form = cgi.FieldStorage()
    action = form.getvalue('action')

    conn = connect_db()

    if action == 'add_task':
        task_description = form.getvalue('task', '')
        due_date = form.getvalue('due_date', '')
        mailaddress = form.getvalue('mailaddress', '')
        created_at = form.getvalue('created_at', '')

        register_data(conn, task_description, due_date, mailaddress, created_at)
        afterpage = codecs.open('./afterpage/RegisterData.html', 'r', 'utf-8').read()
        print(afterpage)

    elif action == 'delete_task':
        task_id = form.getvalue('delete_task_id')
        if task_id:
            delete_task(conn, task_id)
            afterpage = codecs.open('./afterpage/DeleteData.html', 'r', 'utf-8').read()
            print(afterpage)

    conn.close()  # 必ず最後にデータベース接続を閉じる

if __name__ == "__main__":
    main()
