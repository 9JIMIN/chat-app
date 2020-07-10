# basic socket programming

**파이썬 소켓 모듈을 통한 실시간 채팅 프로그램**

- ## 이론

    - ### 소켓모듈 주요 메서드
        - `socket()` : 소켓 생성
            - TCP: socket.SOCK_STREAM
            - UDP: socket.SOCK_DGRAM
        - `bind()` : 소켓에 주소 연결
        - `listen()` : accept가 되도록
            - listen은 connection의 accept가 가능하도록 해준다.
            - backlog 파라미터를 지정가능.
        - `connect()` : 클라에서 서버로 연결
            - 연결요청을 보냄.
        - `accept()` : 서버에서 클라이언트를 연결
            - 코드를 block, 연결을 기다린다.
            - 연결요청을 받음. (host, port)
            - 클라이언트 소켓을 받아서, 그걸로 통신을 한다.
        - `send()` : 데이터 송신
        - `recv()` : 수신
        - `close()` : 연결해제
    
    - ### 흐름
        <p align="center">
        <img src="https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg" width="600" >
        <p align="center"></p>
        </p>
    - [https://realpython.com/python-sockets/](https://realpython.com/python-sockets/)
    - ip 주소가 로컬호스트면 loopback interface, 외부주소면, ethernet interface.