import sync
import sys
import web
import config

folder = sys.argv[1]
scanner = sync.DirScanner(folder, 100)
newfiles = scanner.scan()

for file in newfiles:
    try:
        web.send_file(file, config.SERVER_HOST, config.SERVER_PORT, config.BUFFER_SIZE)
        print(f"File {file} sent to server.")
    except Exception as exc:
        print(f"Unable to send file {file}")
        print(f"Exception {exc}")