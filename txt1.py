# サンプルプログラムをそのまま改良
def myProg():
    begin_pos = get_actual_tcp_pose()# 現在の手先座標取得
    pos_end = pose_add(begin_pos, p[0.100, 0.0, 0.0, 0.0, 0.0, 0.0])# 座標値の演算
    movel(pos_end , a=0.39, v=0.05)
    end
    # endの後に改行が必要です．この行は消さないでください．