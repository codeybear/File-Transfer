import DirScanner

scanner = DirScanner.DirScanner("C:/Users/pjcps/Documents/pexip/test_Files", 100)
newfiles = scanner.scan()

for file in newfiles:
    print(file)


