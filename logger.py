from datetime import datetime

class Logger:
    def __init__(self, logDir):
        self.logDir = logDir
        self.loggerFP = open(logDir, "w")
        
    def log(self, action, filename):
        logMessage = filename + " " + action + " :" + str(datetime.now())
        self.loggerFP.write(logMessage + "\n")
        print(logMessage)
        
    def close(self):
        loggerFP.close()
        