import sys
import time
import os
from synchronizer import *
from logger import *

def checkPath(path): #validates if path is an existing dir
    if not os.path.exists(path) or not os.path.isdir(path):
        return False
    return True

def main():
    print (str(sys.argv))
    print (len(sys.argv))

    
    if not checkPath(sys.argv[1]):
        print("Error1")
        sys.exit(0)
    sourceDir = sys.argv[1]

    if not checkPath(sys.argv[2]):
        print("Error2")
        sys.exit(0)
    replicaDir = sys.argv[2]
        
    print(sys.argv[3])
    if not os.path.isfile(sys.argv[3]):
        print("Error logfile")
        sys.exit(0)
    logDir = sys.argv[3]
        
    if not sys.argv[4].isnumeric():
        print("Error Interval")
        sys.exit(0)
    interval = int(sys.argv[4])
    
    synchro = Synchronizer(sourceDir, replicaDir, logDir, interval)
    while 1==1:
        synchro.sync()
        time.sleep(interval)
        print("WAKEY")
     
if __name__=="__main__":
    main()
    