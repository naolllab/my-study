#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
複数行のプログラムを動かす場合．

参考資料
サンプルプログラム : https://qiita.com/MrBearing/items/a09ab5751be9333cddc5
Socket : https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
'''
import socket
import time
import sys

HOST = "192.168.250.110"
PORT = 30002

def toBytes(str):
    return bytes(str.encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.send(toBytes(
        "def myProg():"+"\n" # 複数行で書く場合のおまじない
        +"begin_pos = get_actual_tcp_pose()" +"\n"  # 現在の手先座標取得
        +"pos_end = pose_add(begin_pos, p[0.100, 0.0, 0.0, 0.0, 0.0, 0.0])" +"\n"# 座標値の演算
        +"movel(pos_end , a=0.39, v=0.05)" + "\n"
        +"end" +"\n")) # ココもおまじない
if __name__ == '__main__':
    main()