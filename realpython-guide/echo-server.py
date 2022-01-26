import socket

HOST = '127.0.0.1'  # standard loopback traffic address/localhost address. Managed within the OS
PORT = 65432        # port to listen on (non-privileged ports are >1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # socket() specifies address family and socket type
                                                        # socket.AF_INET is the internet address family IPv4.
                                                        # socket.SOCK_STREAM is the socket type for TCP
    s.bind((HOST, PORT))    # bind() used to associate the socket with a specific network interface and port number
                            # bind() depends on address family (IPv4) so here it expects a 2-tuple (host, port)
                                # host can be hostname, IP address or empty string
                                # port should be integer from 1-65535. Or >1024
    s.listen()              # listen() enables server to accept() connections. Makes it a listening socket
    conn, addr = s.accept() # ^
                            # accept() blocks and waits for incoming connection.
                            # when client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.
                            # tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6.
                        # WE NOW HAVE NEW SOCKET OBJECT FROM .accept()
                        # new socket object will be used to communicate with the client. Distinct from listening socket that the server is using to accept connections

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)