"""Scan a folder for new/unsent files"""
import hashlib
import os
from collections import defaultdict

class DirScanner():
    def __init__(self, path):
        self.path = path
        self.filelist = defaultdict(bool)

    def scan(self):
        """Scan the specified folder for new files and return these as a list.
        
        File may exist but have not been sent yet, if so then resend"""
        newfiles = []

        for root, _, files in os.walk(self.path):
            for file in files:
                fullpath = os.path.join(root, file)

                # if the does not exist or has not been sent then add to send list
                if self.filelist[fullpath] == False:
                    newfiles.append(fullpath)
        
        return newfiles
