import socket
import threading

host = ""
port = 8080

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# XXX: Set socket options?

c.bind((host, port))
c.listen(1)

print("Running...")


def handle_request(sock, addr):
    print(f"Handling request with {sock} {addr}")
    cfile = sock.makefile("rwb", 0)
    line = cfile.readline().strip()
    print(line)
    cfile.write(b"HTTP/1.1 200 OK\n\n")
    cfile.write(
        b"<html><head><title>Hello</title></head><body>Hello, world</body></html>"
    )
    cfile.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


threads = []
while True:
    try:
        csock, caddr = c.accept()
        print("Received a connection!")
        thread = threading.Thread(target=handle_request, args=(csock, caddr))
        thread.start()
        threads.append(thread)
    finally:
        print("Closing threads...")
        for thread in threads:
            thread.join()
