import sync
import sys
import web

folder = sys.argv[1]
scanner = sync.DirScanner(folder, 100)
newfiles = scanner.scan()

for file in newfiles:
    print(file)
    web.SendFile("http://127.0.0.0.1/sendfile", "file")