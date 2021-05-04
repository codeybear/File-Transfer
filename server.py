"""Command line server to recieve files sent via HTTP"""
import socket
import sys

import config
import IO

folder = sys.argv[1] 

with socket.socket() as sock:
    # Listen for call from client.py
    sock.bind((config.SERVER_HOST, config.SERVER_PORT))
    sock.listen(5)
    print(f"[*] Listening as {config.SERVER_HOST}:{config.SERVER_PORT}")

    # Repeat until keyboard interrupt to quit
    while True:
        client_socket, _ = sock.accept() 
        print("client is connected.")
        file_transfer = IO.FileTransfer(config.BUFFER_SIZE)
        filename = file_transfer.write_to_file(folder, client_socket)
        print(f"Stored new file - {filename}")
        client_socket.close()
