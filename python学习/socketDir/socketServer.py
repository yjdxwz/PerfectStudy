import socket

import threading

# IPV4 AF_INET
# IPV6 AF_INET6
# 类型， 协议 ，
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()


# 只能处理一个

def handle_sock(sock, addr):
    while True:
        # 获取从客户端发送的数据  单位是字节 一次获取1k 的数据
        data = sock.recv(1024)
        data = data.decode("utf8")
        print(data)
        # if "exit" in data:
        #     break
        re_data = input()
        sock.send(re_data.encode("utf8"))
        sock.close()
    # sock.close()
    # server.close()
    # sock.close()


while True:
    sock, addr = server.accept()
    # 用线程去处理新接受的连接

    client_thread = threading.Thread(target=handle_sock, args=(sock, addr,))
    client_thread.start()

#
