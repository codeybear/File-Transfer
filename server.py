"""Server to recieve files sent via HTTP"""
import socket
import os
import sys
import config

def LoadHeader():
    """Load the filename from the first section of data."""
    received = client_socket.recv(config.BUFFER_SIZE)
    filename = received[:received.find(0)].decode()
    file_content = received[received.find(0)+1:]

    # Convert path to server folder
    filename = os.path.basename(filename)

    return filename, file_content


folder = sys.argv[1] 

with socket.socket() as s:
    s.bind((config.SERVER_HOST, config.SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {config.SERVER_HOST}:{config.SERVER_PORT}")

    while True:
        # TODO need to make this a context manager, address is not used
        client_socket, address = s.accept() 
        print(f"[+] {address} is connected.")

        filename, file_content = LoadHeader()
        filename = os.path.join(folder, filename)
        print(f"Receiving {filename}")

        with open(filename, "wb") as f:
            f.write(file_content)

            while True:
                bytes_read = client_socket.recv(config.BUFFER_SIZE)
                if not bytes_read:    
                    break
                f.write(bytes_read)
                print(f"{len(bytes_read)}")

        client_socket.close()