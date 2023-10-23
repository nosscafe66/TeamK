#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Get_CSV"

import cgi, cgitb, sqlite3, codecs
import csv
import datetime
cgitb.enable()

print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'TeamK.db'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

account_table_list=cur.execute('SELECT * FROM task_tbl')
account_table_list = cur.fetchall()

now = datetime.datetime.now()
filename = './csv/account_list_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'

def make_file(account_table_list:list) -> None:
    header = ["TaskID", "Task", "DueDate", "MailAddress", "CreatedAt","Time"]
    with open(filename, 'a', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerow(header)
        for data in account_table_list:
            now_str = datetime.datetime.now().strftime('%H:%M:%S.%f')
            writer.writerow(list(data) + [now_str])

def download_csvfile(csvfile:str) -> str:
    afterpage = codecs.open('./afterpage/DataUnload.html', 'r', 'utf-8').read()
    afterpage = afterpage.replace('{% filename %}', str(csvfile))
    # conn.commit()
    #cur.close()
    #conn.close()
    return afterpage

def main():
    try:
      csvfile=make_file(account_table_list)
      afterpage=download_csvfile(csvfile)
      print(afterpage)
      cur.close()
      conn.close()
    except Exception as exceptmessage:
      print(exceptmessage)

if __name__=="__main__":
    main()