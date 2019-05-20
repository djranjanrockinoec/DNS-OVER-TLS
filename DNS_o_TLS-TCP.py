#!/usr/bin/env python
# DNS Over TLS TCP
# Author: Rashmi Ranjan Behera
# @mail: dj.ranjan.rockin.oec@gmail.com

import socket
import threading
import ssl

#global settings
Cloudfare_IP = '1.1.1.1'
Cloudfare_Port = 853
Cont_host = '127.0.0.1'
Cont_TCP_Port = 53
Max_Conn = 5


#switch between receiving and sending packets up and down
def switch(local, server, updown):
	while True:
		data = local.recv(4096)
        	if len(data) == 0:
			break
		server.send(data)
	local.shutdown(socket.SHUT_RDWR)
	local.close()


#Create TLS socket to Cloudflare
def connect():
        s_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        context = ssl.create_default_context()
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.load_verify_locations('/DNSoTLS/cloudflare-dnscom.crt')
        wrappedSocket = context.wrap_socket(s_conn, server_hostname=Cloudfare_IP)
        wrappedSocket.connect((Cloudfare_IP, Cloudfare_Port))
        return wrappedSocket

#Daemon to listen/receive on ports
def daemon():
	l_conn_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	l_conn_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	l_conn_tcp.bind((Cont_host, Cont_TCP_Port))
	l_conn_tcp.listen(Max_Conn)
	while True:
		l_sock, l_addr = l_conn_tcp.accept()
		Secure_con = connect()
		#Threading to take care of multiple requests parallely
		out_conn = threading.Thread(target=switch, args=(l_sock, Secure_con, True))
		in_conn = threading.Thread(target=switch, args=(Secure_con, l_sock, False))
		out_conn.start()
		in_conn.start()
	#cleanup
	s_conn.shutdown(socket.SHUT_RDWR)
	s_conn.close()
	l_sock.shutdown(socket.SHUT_RDWR)
	l_sock.close()
	l_conn_tcp.shutdown(socket.SHUT_RDWR)
	l_conn_tcp.close()


#main
if __name__ == "__main__":
	daemon()
