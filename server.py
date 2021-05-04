"""Command line server to recieve files sent via HTTP"""
import socket
import sys

import config
import IO

folder = sys.argv[1] 

with socket.socket() as sock:
    # Listen for call from client.py
    sock.bind((config.SERVER_HOST, config.SERVER_PORT))
    print(f"[*] Listening as {config.SERVER_HOST}:{config.SERVER_PORT}")

    # The socket needs a timeout to allow for keyboard interrupt
    sock.settimeout(1)
    sock.listen(5)

    try:
        while True:
            try:
                client_socket, address = sock.accept() 
                print(f"client ({address}) is connected.")
                file_transfer = IO.FileTransfer(config.BUFFER_SIZE)
                filename = file_transfer.write_to_file(folder, client_socket)
                print(f"Stored new file - {filename}")
                client_socket.close()
            except socket.timeout:
                pass
    except KeyboardInterrupt:
        print('Keyboard interrupt stopping...')
