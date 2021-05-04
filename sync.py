"""Scan a folder for new/unsent files."""
import hashlib
import os
from dataclasses import dataclass

@dataclass
class FileInfo:
    """Status of a file to be sent to the server"""
    sent: bool
    checksum: str

class DirScanner():
    def __init__(self, path):
        self.path = path
        self.filelist = {}

    def scan(self):
        """Scan the specified folder for new files and return these as a list.

        Files may exist but have not been sent yet, if so then add to the send list.
        Also file changes are detected using a checksum, in case of a change they
        are also added to be resent"""
        newfiles = []

        for file in os.listdir(self.path):
            fullpath = os.path.join(self.path, file)
            checksum = self.md5(fullpath)

            # if the does not exist then add to send list
            if fullpath not in self.filelist:
                fileinfo = FileInfo(False, checksum)
                self.filelist[fullpath] = fileinfo
                newfiles.append(fullpath)
            else:
                # check to see if a file has not been sent or has changed, if so send again
                if self.filelist[fullpath].sent is False or self.filelist[fullpath].checksum != checksum:
                    newfiles.append(fullpath)

        return newfiles

    def md5(self, filename):
        """Create a checksum for a specified file."""
        hash_md5 = hashlib.md5()

        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()
