import socket  
import time
import threading

# ip 주소 받아오기 // 서버와 같음, 포트만 다름
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# 서버 소켓 연결
server_address = (ip_address, 23456)  
client_socket.connect(server_address)  
print (f"[연결된 서버] == {server_address}")

# send, recv 함수 정의
def send(sock):
    while True:
        sendData = input('>>>')
        if sendData == 'bye': sock.close()
        sock.send(sendData.encode('utf-8'))

def recv(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))

# 쓰레딩
sender = threading.Thread(target=send, args=(client_socket,))
recevier = threading.Thread(target=recv, args=(client_socket,))
sender.start()
recevier.start()