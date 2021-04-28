import os

class DirScanner():
    def __init__(self, path, timer):
        self.timer = timer
        self.path = path
        self.filelist = {}

    def scan(self):
        """Scan the specified folder for new files and return these as a list."""
        newfiles = []

        for root, _, files in os.walk(self.path):
            for file in files:
                fullpath = os.path.join(root, file)

                if fullpath not in files:
                    self.filelist[fullpath] = ""
                    newfiles.append(fullpath)
        
        return newfiles
