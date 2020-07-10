import socket
import threading
import time
""" 
- 서버
-- 최초의 수신자가 되는 노드.
-- socket.SOCK
- bind, listen
-- 소켓을 만들어 포트에 매핑하고, 클라이언트가 접속하길 기다린다. 
 """
# ip 주소 받아오기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create TCP/IP socket
hostname = socket.gethostname() # 'DESKTOP-1L61C53'
ip_address = socket.gethostbyname(hostname) # 192.168.0.3

# 소켓 바인딩
server_address = (ip_address, 23456)  
server_socket.bind(server_address)
print (f'[서버 소켓 정보] == {server_address}')  

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