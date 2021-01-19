import socket
import AES
# Made with the help of tutorial from https://www.youtube.com/watch?v=3QiPPX-KeSc
# Aleksander Mielczarek

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.15"
ADDR = (SERVER, PORT)
AES_INIT = ("This is 16 bytes", 128)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def encrypt(msg):
    aes = AES.AESCipher('abcdefghijklmnopqrstuvwxyz123456')
    msg = aes.encrypt(msg)
    print(msg)
    return msg


def send(msg):
    msg = encrypt(msg)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send(input())
send(DISCONNECT_MESSAGE)