import socket
import threading
import time

# ip 주소 받아오기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create TCP/IP socket
local_hostname = socket.gethostname() # 'DESKTOP-1L61C53'
ip_address = socket.gethostbyname(local_hostname) # 192.168.0.3

# 소켓 바인딩
server_address = (ip_address, 23456)  
server_socket.bind(server_address)
print (f'[소켓 정보] == {server_address}')  

# send, recv 함수 정의
def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def recv(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


# 리스닝
server_socket.listen(1)
print ('[연결 대기중]')
connection, client_address = server_socket.accept()
print(f'[연결됨] == {client_address}')

# 쓰레딩
sender = threading.Thread(target=send, args=(connection,))
recevier = threading.Thread(target=recv, args=(connection,))
sender.start()
recevier.start()

while True:  
    time.sleep(1)
    pass