import sync
import sys
import web
import exceptions

folder = sys.argv[1]
scanner = sync.DirScanner(folder, 100)
newfiles = scanner.scan()

# this needs to be put into some kind of function, maybe a class which gets the checksum and remembers stuff
for file in newfiles:
    print(f"{file}")

    try:
        web.SendFile("http://127.0.0.0.1/sendfile", file)
        print(f"File {file} sent to server.")
    except exceptions.ConnectionError:
        print("Unable to send file f{file}")
    
