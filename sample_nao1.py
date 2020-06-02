#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import sys

HOST = "192.168.250.110"
PORT = 30002

# 別のスクリプトのテキストを読み込み
def getTxt():
    # コマンドライン引数
    arg = sys.argv
    if len(arg) != 2:
        print('【error】コマンドライン引数の個数が足りません．\n')
        sys.exit()
    
    # テキスト読み込み
    path = arg[1]
    with open(path) as f:
        txt = f.read()
    return txt


def toBytes(str):
    return bytes(str.encode())

def main():
    # ソケット接続
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # 別のスクリプトのテキストを読み込み
    txt = getTxt()
    print(txt)

    # 送信
    s.send(toBytes(txt))

if __name__ == '__main__':
    main()