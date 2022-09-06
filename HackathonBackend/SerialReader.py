import serial
import time


ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)


def Temperature_check():
    line = (ser.readline().decode("utf-8"))[:4]
    return float(line)