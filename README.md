# PythonFolderSyncChallenge
Basic python program which synchronizes the files of a source path to a replica path, logging all the changes.

The source path, replica path, logfile path and the interval for synchronization have to be given as commandline arguments in this exact order. The log file has to be created.
The program supports level 1 directory synchronization, meaning that nested directories and their files inside source path will be ignored.
Any files deleted from replica path will not be replicated, unless their content changes in source path.

An md5 digest of every file is stored in order to determine wether the file has been updated or not and thus avoid unnecessary file copies.

The sync() function runs periodically using the thread module.
