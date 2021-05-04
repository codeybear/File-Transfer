"""Send and receive files using HTTP sockets.

File is sent in the format Filename[null character]File Content
so that the filename can be preserved.
"""
import os
import socket

SEPARATOR = 0


class FileTransfer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size

    def send_file(self, filename, host, port):
        """Send a file over an HTTP socket."""
        sock = socket.socket()

        sock.connect((host, port))
        sock.send(f"{filename}{chr(SEPARATOR)}".encode())

        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(self._buffer_size)
                if not bytes_read:
                    break
                sock.sendall(bytes_read)

        sock.close()

    def _load_header(self, received):
        """Load the filename from the first section of data."""
        filename = received[:received.find(SEPARATOR)].decode()
        file_content = received[received.find(SEPARATOR)+1:]

        # Convert path to server folder
        filename = os.path.basename(filename)

        return filename, file_content

    def write_to_file(self, folder, sock):
        """Write a file to disc using an open client HTTP socket"""
        received = sock.recv(self._buffer_size)
        filename, file_content = self._load_header(received)
        filename = os.path.join(folder, filename)

        with open(filename, "wb") as f:
            f.write(file_content)

            while True:
                bytes_read = sock.recv(self._buffer_size)

                if not bytes_read:
                    break

                f.write(bytes_read)

        return filename
