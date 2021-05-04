"""Command line client to send files via HTTP."""
import sys
import time

import config
import IO
import sync

# Get the folder to scan for new files
folder = sys.argv[1]
scanner = sync.DirScanner(folder)

# Repeat folder scan and file send until keyboard interrupt
while True:
    newfiles = scanner.scan()

    for file in newfiles:
        try:
            file_transfer = IO.FileTransfer(config.BUFFER_SIZE)
            file_transfer.send_file(file, config.SERVER_HOST, config.SERVER_PORT)
            scanner.filelist[file].sent = True
            print(f"File {file} sent to server.")
        except ConnectionRefusedError:
            print(f"Unable to contact server file not sent - {file}")

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("Interupted by keyboard, exiting.")
        break
