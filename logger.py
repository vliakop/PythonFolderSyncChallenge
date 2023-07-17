from datetime import datetime

class Logger:
    def __init__(self, logDir):
        self.logDir = logDir
        self.loggerFP = open(logDir, "w")
        
    # Prepares the message to be written in logfile, stdout
    def log(self, action, filename):
        logMessage = filename + " " + action + " :" + str(datetime.now())
        self.loggerFP.write(logMessage + "\n")
        print(logMessage)
        
    # Closes the opened file
    def close(self):
        loggerFP.close()
        