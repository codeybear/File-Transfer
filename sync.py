import os
import hashlib

class DirScanner():
    def __init__(self, path):
        self.path = path
        self.filelist = {}

    def scan(self):
        """Scan the specified folder for new files and return these as a list."""
        newfiles = []

        for root, _, files in os.walk(self.path):
            for file in files:
                fullpath = os.path.join(root, file)

                if fullpath not in self.filelist:
                    self.filelist[fullpath] = False
                    newfiles.append(fullpath)
        
        return newfiles
