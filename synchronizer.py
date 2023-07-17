from logger import *
import shutil
import hashlib
import os
import time, threading

class Synchronizer():
    def __init__(self, sourceDir, replicaDir, logDir, interval):
        self.sourceDir = sourceDir # appends a '/' at the end of path if it doesn't exist
        if not self.sourceDir.endswith("/"):
            self.sourceDir = self.sourceDir + "/"
        self.replicaDir = replicaDir
        if not self.replicaDir.endswith("/"):
            self.replicaDir = self.replicaDir + "/"        
        self.logDir = logDir
        self.logger = Logger(logDir)
        self.interval = interval
        self.sourceArchive = {} # A dictionary with keys filenames already synced from source path  and values their md5 digests
        self.replicaArchive = {} # A dictionary with keys filenames already synced  to replica path and values their md5 digests
        
    def sync(self, tail=""):
        sourcePath = self.sourceDir + tail
        replicaPath = self.replicaDir + tail
        
        # Ignore the hidden files
        sourceContent = [file for file in os.listdir(sourcePath) if not file.startswith(".")] 
 

        # Check if files were deleted from the source path and delete them from replica path
        savedFiles = list(self.sourceArchive.keys())
        for filename in savedFiles:
            if not filename in sourceContent:
                del self.sourceArchive[filename]
                os.remove(replicaPath + filename)
                self.logger.log(filename, "DELETED")
                
                
        # Check for new or updated files in source path. A file is updated if its md5 digest has changed
        for filename in sourceContent: 
            if os.path.isfile(sourcePath + filename): # If it is a file 
                target = sourcePath + filename # file to be copied
                digest = hashlib.md5(open(target, 'rb').read()).digest()

                if filename not in self.sourceArchive.keys():
                    self.sourceArchive[filename] = digest
                    self.replicaArchive[filename] = digest
                    shutil.copy(target, replicaPath + filename)
                    self.logger.log(filename, "CREATED")
                else:
                    if self.sourceArchive[filename] != digest:  # the content of the file has changed
                        self.sourceArchive[filename] = digest
                        self.replicaArchive[filename] = digest
                        shutil.copy(target, replicaPath + filename)
                        self.logger.log(filename, "COPIED")
        threading.Timer(self.interval, self.sync).start()