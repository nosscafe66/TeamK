#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "{yourname} <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "02 09 2023"
__prodactname__ = "Register AccountData"

import cgi, cgitb, sqlite3, codecs

cgitb.enable()
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'TeamK.db'
QUERY_PATH= "./sql/Regist_data_insert.sql"
TABLE_NAME="task_tbl"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

def register_data():
    cur.execute('INSERT INTO {} values(?, ?, ?, ?)'.format(TABLE_NAME),
                  (form["task"].value,
                  form["birthday"].value,
                  form["mailaddress"].value,
                  form["date"].value))
    afterpage = codecs.open('./afterpage/RegisterData.html', 'r', 'utf-8').read()
    print(afterpage)
    conn.commit()
    cur.close()
    conn.close()

def main():
  try:
    pass
    # register_data()
  except Exception as exceptmessage:
    return

if __name__=="__main__":
    main()