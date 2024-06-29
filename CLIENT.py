#client code
import socket
import threading
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == '\nUSERNAME SHOWN IN CHAT ROOM : ':
                client_socket.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("SERVER IS DOWN!")
            client_socket.close()
            break
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

username = input("WELCOME TO SERVER TCP X\n\n PLEASE ENTER YOUR USERNAME FOR SERVER DATA: ")

receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client,))

receive_thread.start()
send_thread.start()
