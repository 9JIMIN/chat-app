import socket

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
    sendData = input('>>>')
    sock.send(sendData.encode('utf-8'))

def recv(sock):
    recvData = sock.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))

# 리스닝
server_socket.listen(1)
print ('[연결 대기중]')
connection, client_address = server_socket.accept()

while True:  
    send(connection)
    recv(connection)