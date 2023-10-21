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

cur.execute('SELECT * FROM task_tbl')
account_table_list = cur.fetchall()

result = '''
<table border="1">
<tr>
<th>task</th>
<th>birthday</th>
<th>mailaddress</th>
# <th>created_at</th>
</tr>
'''
print(task)
def get_account_list(result:str) -> str:
    for data in account_table_list:
        if form["task"].value in data:
            result += "<tr>"
            result += "<td>" + str(data[0]) + "</td>"
            result += "<td>" + str(data[1]) + "</td>"
            result += "<td>" + str(data[2]) + "</td>"
            result += "</tr>"
            afterpage = codecs.open('./afterpage/after.html', 'r', 'utf-8').read()
            afterpage = afterpage.replace('{% task %}', str(data[0]))
            afterpage = afterpage.replace('{% userinfo %}', str(data[1]))
            afterpage = afterpage.replace('{% result %}', result)
            #conn.commit()
            #cur.close()
            #conn.close()
        elif not form["task"].value in data:
            result += "<tr>"
            result += "<td> Nothing Data </td>"
            result += "<td> Nothing Data </td>"
            result += "<td> Nothing Data </td>"
            result += "</tr>"
            afterpage = codecs.open('./afterpage/after.html', 'r', 'utf-8').read()
            afterpage = afterpage.replace('{% task %}', "Nothing Register")
            afterpage = afterpage.replace('{% userinfo %}', "Nothing Register")
            afterpage = afterpage.replace('{% result %}', result)
            # conn.commit()
            #cur.close()
            #conn.close()
    return afterpage

def main():
    try:
        result_page=get_account_list(result)
        cur.close()
        conn.close()
        print(result_page)
    except Exception as exceptmessage:
        print(exceptmessage)

if __name__ == "__main__":
    main()