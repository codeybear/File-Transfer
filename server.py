"""Server to recieve files sent via HTTP"""
import socket
import os
import sys
import config

folder = sys.argv[1] 

s = socket.socket()
s.bind((config.SERVER_HOST, config.SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {config.SERVER_HOST}:{config.SERVER_PORT}")

def LoadHeader():
    # receive using client socket, not server socket
    received = client_socket.recv(config.BUFFER_SIZE)
    filename = received[:received.find(0)].decode()
    file_content = received[received.find(0)+1:]

    # Convert path to server folder
    filename = os.path.basename(filename)
    filename = os.path.join(folder, filename)
    print(f"Receiving {filename}")

    return filename, file_content

while True:
    client_socket, address = s.accept() 
    print(f"[+] {address} is connected.")

    # receive using client socket, not server socket
    filename, file_content = LoadHeader()

    with open(filename, "wb") as f:
        f.write(file_content)

        while True:
            bytes_read = client_socket.recv(config.BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
            print(f"{len(bytes_read)}")

    client_socket.close()
        
s.close()