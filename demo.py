import serial
import cv2
import time
import threading
import playsound


serialPort = "COM3"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("参数设置：串口={} ，波特率={}".format(serialPort, baudRate))


framelist = ['0.jpg', '1.jpg', '2.jpg']
frameindex = 0


def changeimage():
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    global framelist, frameindex
    while True:
        frame = cv2.imread(framelist[frameindex])
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break


def main():
    global frameindex
    while True:
        s = ser.read()
        if s == b'1':
            frameindex = 0
            playsound.playsound('0.mp3')
            time.sleep(1)
        if s == b'2':
            frameindex = 1
            playsound.playsound('1.mp3')
            time.sleep(1)
        if s == b'3':
            frameindex = 2
            playsound.playsound('2.mp3')
            time.sleep(1)


th1 = threading.Thread(target=main, )
th2 = threading.Thread(target=changeimage, )
threads = [th1, th2]

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print('end')
    cv2.destroyAllWindows()
