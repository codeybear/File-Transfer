import socket

def send_file(filename, host, port, buffer_size):
    SEPARATOR = chr(0)
    s = socket.socket()

    s.connect((host, port))
    print("[+] Connected to {host}:{port}")
    s.send(f"{filename}{SEPARATOR}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(buffer_size)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            print(f"Bytes sent: {len(bytes_read)}")

    s.close()