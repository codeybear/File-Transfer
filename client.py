import sys

import config
import IO
import sync

folder = sys.argv[1]
scanner = sync.DirScanner(folder, 100)
newfiles = scanner.scan()

for file in newfiles:
    try:
        file_transfer = IO.FileTransfer(config.BUFFER_SIZE)
        file_transfer.send_file(file, config.SERVER_HOST, config.SERVER_PORT)
        print(f"File {file} sent to server.")
    except Exception as exc:
        print(f"Unable to send file {file}")
        print(f"Exception {exc}")
