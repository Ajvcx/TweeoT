import tweetid_module
import timeline_module
import serial_module
from time import sleep

CK = ***                                    # Consumer Key
CS = ***                                    # Consumer Secret
AT = ***                                    # Access Token
AS = ***                                    # Accesss Token Secert
ID = ***                                    # ID

timeline = []


since_id = tweetid_module.tweetID(CK, CS, AT, AS, ID)


while True:

    sleep(300)

    timeline = usertimeline_module.usertimeline(CK, CS, AT, AS, ID, since_id)

    # ACオン
    for i in timeline:
        if "#switch_ON" in i:
            flag = 1
            serial_module.serial_com(flag)
            break

    # ACオフ
    for i in timeline:
        if "switch_OFF" in i:
            flag = 0
            serial_module.serial_com(flag)
            break

    # プログラム停止
    for i in timeline:
        if "switch_stop" in i:
            flag = -1
            break
    if flag == -1:
        break

    since_id = tweetid_module.tweetID(CK, CS, AT, AS, ID)

    timeline.clear()