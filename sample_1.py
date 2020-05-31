#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
ロボットが完全に腕を伸ばした状態へ持っていくスクリプトを記述する．
Socketのクライアントを作成する．

参考資料
サンプルプログラム : https://qiita.com/MrBearing/items/a09ab5751be9333cddc5
Socket : https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
'''

import socket
import time

# 外部マニュアルより
# hostname : ur-xx 
#     (or the IP address found in the About Dialog-Box in PolyScope if the robot is not in DNS)
# port : 30002

HOST = "192.168.250.110"
PORT = 30002

def toBytes(str):
    # 標準のエンコーディングは 'utf-8'
    return bytes(str.encode())

def main():
    # AF = IPv4 という意味, TCP/IP の場合は、SOCK_STREAM を使う
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # サーバを指定
    s.connect((HOST, PORT))
    # サーバにメッセージを送る
    s.send(toBytes("movej([0,-1.57,0,0,-1.57,1.57], a=1.40, v=1.04)" + "\n"))# ラジアン
    # 3秒停止
    time.sleep(3)
    # ネットワークのバッファサイズは1024．サーバからの文字列を取得する
    data = s.recv(1024)
    # Socket接続を閉じ、関連付けられたすべてのリソースを解放する
    s.close()
    print("Receved", repr(data))
    print("Program finish")

if __name__ == '__main__':
    main()

