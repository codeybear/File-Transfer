import sync
import sys
import web

folder = sys.argv[1]
scanner = sync.DirScanner(folder, 100)
newfiles = scanner.scan()

# this needs to be put into some kind of function, maybe a class which gets the checksum and remembers stuff
for file in newfiles:
    try:
        web.SendFile("http://localhost:8000/", file)
        print(f"File {file} sent to server.")
    except Exception as exc:
        print(f"Unable to send file {file} will retry later")
        print(f"Exception {exc}")