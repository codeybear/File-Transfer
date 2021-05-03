"""
Server receiver of the file
"""
import socket
import os

# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
folder = "C:/Users/pjcps/Documents/pexip/test_Output_Files"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
# Accept up to 5 connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, address = s.accept() 
    print(f"[+] {address} is connected.")

    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE) # 
    filename = received[:received.find(0)].decode()
    file_content = received[received.find(0)+1:]

    # remove absolute path 
    filename = os.path.basename(filename)
    filename = os.path.join(folder, filename)
    print(f"Receiving {filename}")

    with open(filename, "wb") as f:
        f.write(file_content)

        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
            print(f"{len(bytes_read)}")

    client_socket.close()
        
s.close()