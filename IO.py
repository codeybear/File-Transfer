import os
import socket


class FileTransfer:
    def __init__(self, buffer_size) -> None:
        self._buffer_size = buffer_size

    def send_file(self, filename, host, port):
        SEPARATOR = chr(0)
        s = socket.socket()

        s.connect((host, port))
        print("[+] Connected to {host}:{port}")
        s.send(f"{filename}{SEPARATOR}".encode())

        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(self._buffer_size)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                print(f"Bytes sent: {len(bytes_read)}")

        s.close()

    def _load_header(self, received):
        """Load the filename from the first section of data."""
        filename = received[:received.find(0)].decode()
        file_content = received[received.find(0)+1:]

        # Convert path to server folder
        filename = os.path.basename(filename)

        return filename, file_content

    def write_to_file(self, folder, socket):
        received = socket.recv(self._buffer_size)
        filename, file_content = self._load_header(received)
        filename = os.path.join(folder, filename)
        print(f"Receiving {filename}")

        with open(filename, "wb") as f:
            f.write(file_content)

            while True:
                bytes_read = socket.recv(self._buffer_size)
                if not bytes_read:    
                    break
                f.write(bytes_read)
                print(f"{len(bytes_read)}")
