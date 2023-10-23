#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Get_Table & Serch Data"

import cgi, cgitb, sqlite3, codecs
cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
task = form.getvalue("task", "未入力")
form_check = 0

DB_NAME = 'TeamK.db'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
task_id = form["task"].value

cur.execute('SELECT * FROM task_tbl where task_id = ?',(task_id))
account_table_list = cur.fetchall()

def get_account_list() -> str:
    result = '''
    <table border="1">
    <tr>
    <th>task_id</th>
    <th>task</th>
    <th>due_date</th>
    <th>mailaddress</th>
    <th>created_at</th>
    </tr>
    '''
    if account_table_list:
        for row in account_table_list:
            result += "<tr>"
            for item in row:
                result += f"<td>{item}</td>"
            result += "</tr>"
    else:
        result += "<tr><td colspan='5'>Nothing Data</td></tr>"

    result += "</table>"
    afterpage_template = codecs.open('./afterpage/after.html', 'r', 'utf-8').read()
    afterpage_content = afterpage_template.replace('{% result %}', result)

    return afterpage_content

def main():
    try:
        result_page = get_account_list()
        cur.close()
        conn.close()
        print(result_page)
    except Exception as e:
        # ここでエラーメッセージを出力します。
        print(f"<p>An error occurred: {e}</p>")


if __name__ == "__main__":
    main()
