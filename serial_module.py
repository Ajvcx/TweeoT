import serial
from time import sleep


def serial_com(flag):
    with serial.Serial("/dev/tty.usbmodem1421",9600,timeout=1) as ser:

            sleep(5)

            flag_byte = flag.to_bytes(1,"big")

            # 送信
            ser.write(flag_byte)


if __name__ == "__main__":
    serial_com()
