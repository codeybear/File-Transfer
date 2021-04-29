import os
import hashlib

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

    def md5(self, filename):
        """Create a checksum for a specified file to test to see if its unique."""
        hash_md5 = hashlib.md5()

        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()