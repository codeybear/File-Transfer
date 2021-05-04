"""Command line client to send files via HTTP"""
import time
import sys

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
            scanner.filelist[file] = True
            print(f"File {file} sent to server.")
        except Exception as exc:
            print(f"Unexpected error while sending file {file}")
            print(f"Exception {exc}")

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("Interupted by keyboard, exiting.")
        break
