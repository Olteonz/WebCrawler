import socket
import threading
import AES
# Made with the help of tutorial from https://www.youtube.com/watch?v=3QiPPX-KeSc
# Aleksander Mielczarek

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)





def decrypt(msg):
    """
    decrypt function decrypts a string using AES decryption

    :param msg: string (encrypted messege)
    :return: string (decrypted messege)
    """
    aes = AES.AESCipher('abcdefghijklmnopqrstuvwxyz123456')
    msg = aes.decrypt(msg)
    return msg


def handle_client(conn, addr):
    """
    handle_client function listens for incoming messeges from the client and prints them to console

    :param conn: the object of connection with the client
    :param addr: the address of the client
    :return: N/A
    """
    print(f"[NEW CONNECTION {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg = decrypt(msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
    conn.close()


def start():
    """
    start function starts listening for incoming connections and forwards the connection to the handle_client
    client on a new thread

    :return: N/A
    """
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("server is starting")
start()
