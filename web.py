"""
Client that sends the file (uploads)
"""
import socket
import os
import argparse

SEPARATOR = chr(0)
BUFFER_SIZE = 1024 * 4

import requests

def send_file(filename, host, port):
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename at the start of the data
    s.send(f"{filename}{SEPARATOR}".encode())

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            print(f"Bytes sent: {len(bytes_read)}")

    s.close()