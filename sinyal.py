import signal,os
import time

def signal_handler(signum,frame):
    print("Sinyal Numarası",signum,"frame:",frame)

def exit_handler(signum,frame):
    print("Çıkış Yapılıyor...")
    exit(0)


signal.signal(signal.SIGTSTP,signal_handler())
signal.signal(signal.SIGTSTP,exit_handler())

while 1:
    print("PRESS CTRL+C")
    time.sleep(3)
