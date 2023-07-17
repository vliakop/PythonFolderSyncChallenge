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

    # Source path validation
    if not checkPath(sys.argv[1]):
        print("The 'source' path you provided is not valid.")
        sys.exit(0)
    sourceDir = sys.argv[1]

    # Replica path validation
    if not checkPath(sys.argv[2]):
        print("The 'replica' path you provided is not valid.")
        sys.exit(0)
    replicaDir = sys.argv[2]
    
    # Logfile path validation
    print(sys.argv[3])
    if not os.path.isfile(sys.argv[3]):
        print("The logfile you provided is not valid.")
        sys.exit(0)
    logDir = sys.argv[3]
    
    # Interval validation
    if not sys.argv[4].isnumeric():
        print("The synchronization interval you provided is not valid.")
        sys.exit(0)
    interval = int(sys.argv[4])
    
    # Create an object instance and start syncing - ends with Keyboard Interruption
    synchro = Synchronizer(sourceDir, replicaDir, logDir, interval)
    synchro.sync()
     
if __name__=="__main__":
    main()
    