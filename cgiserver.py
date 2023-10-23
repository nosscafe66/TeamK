#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "CgiServer Up"
__command__ = "python cgiserver.py"
import os
import http.server

PORT = int(os.getenv('PORT', 8000))  # デフォルトのポートは、ローカルでのテスト用です。

server_address = ("", PORT)
handler_class = http.server.CGIHTTPRequestHandler  # CGIスクリプトを処理するハンドラー
httpd = http.server.HTTPServer(server_address, handler_class)

httpd.serve_forever()