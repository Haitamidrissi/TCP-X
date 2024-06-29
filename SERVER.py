import socket
import threading
import logging

# Set up logging
logging.basicConfig(filename='logs server.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def handle_client(client_socket, client_address):
    logging.info(f"NEW CONNECTION: {client_address} (connected).")
    print(f"NEW CONNECTION FOUNDED: ADDRESS IP OF NEW CLIENT ==  {client_address} (connected).")

    client_socket.send("VOTRE NOM DANS CHAT : ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username

    welcome_message = f"{username} : JOIN THE CHAT ROOM !"
    broadcast(welcome_message, client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(f"{username}: {message}", client_socket)
                logging.info(f"{username}: {message}")
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        username = clients[client_socket]
        goodbye_message = f"{username} : QUIT THE CHAT ROOM."
        broadcast(goodbye_message, client_socket)
        logging.info(goodbye_message)
        del clients[client_socket]
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()

clients = {}

print("\033[0;31m")
print(r"""
     ______   ________  _______   __     __  ________  _______         ________   ______   _______         __    __ 
    /      \ |        \|       \ |  \   |  \|        \|       \       |        \ /      \ |       \       |  \  |  \
   |  $$$$$$\| $$$$$$$$| $$$$$$$\| $$   | $$| $$$$$$$$| $$$$$$$\       \$$$$$$$$|  $$$$$$\| $$$$$$$\      | $$  | $$
   | $$___\$$| $$__    | $$__| $$| $$   | $$| $$__    | $$__| $$         | $$   | $$   \$$| $$__/ $$       \$$\/  $$
    \$$    \ | $$  \   | $$    $$ \$$\ /  $$| $$  \   | $$    $$         | $$   | $$      | $$    $$        >$$  $$ 
    _\$$$$$$\| $$$$$   | $$$$$$$\  \$$\  $$ | $$$$$   | $$$$$$$\         | $$   | $$   __ | $$$$$$$        /  $$$$\ 
   |  \__| $$| $$_____ | $$  | $$   \$$ $$  | $$_____ | $$  | $$         | $$   | $$__/  \| $$            |  $$ \$$\
    \$$    $$| $$     \| $$  | $$    \$$$   | $$     \| $$  | $$         | $$    \$$    $$| $$            | $$  | $$
     \$$$$$$  \$$$$$$$$ \$$   \$$     \$     \$$$$$$$$ \$$   \$$          \$$     \$$$$$$  \$$             \$$   \$$
                                                                                                                 
                                                                                                                 
                                            BREAK  YOUR   CHAT  WITH  TCP X    
                                                    
                                  ( THIS  IS  THE  MAIN  INTERFACE  OF  SERVER  TCP X )

      
                                                                                    created by HAITAM BEN DAHMANE IDRISSI - V 1.0
----------------------------------------------------------------------------------------------------------------------------------                                                                                                   

      
===>  Mode d'écoute est activé!
===>  En attente de connexion...
.........

===>  LE SERVER TCP X EST MAINTENANT ACTIF AVEC SUCCES ...
                                                                                                                                                                              
    """)

while True:
    client_socket, client_address = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
    logging.info(f"ACTIVE CONNECTIONS = {threading.activeCount() - 1}")
    print(f"ACTIVE CONNECTIONS = {threading.activeCount() - 1}")
