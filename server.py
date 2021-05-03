"""Server to recieve files sent via HTTP"""
import socket
import sys

import config
import IO

folder = sys.argv[1] 

with socket.socket() as sock:
    sock.bind((config.SERVER_HOST, config.SERVER_PORT))
    sock.listen(5)
    print(f"[*] Listening as {config.SERVER_HOST}:{config.SERVER_PORT}")

    while True:
        #TODO need to make this a context manager, address is not used
        client_socket, address = sock.accept() 
        print("client is connected.")
        file_transfer = IO.FileTransfer(config.BUFFER_SIZE)
        file_transfer.write_to_file(folder, client_socket)
        client_socket.close()
