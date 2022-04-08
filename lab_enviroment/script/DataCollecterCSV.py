from read_dataset import DataSet
from pathlib import Path


##Collectar data från jabRef_architecture och skriver in i samma CVS fil, 
#data är EJ ren i efter detta stadiet.
def collectJabRef(csvFile):
    directoryPath = getJabRefDirectory()
    labels = [ 'CLI', 'GLOBALS', 'GUI', 'LOGIC', 'MODEL', 'PREF' ]
    collectDataFromDirectory(csvFile, directoryPath, labels)

def getCurrentDirectory():
    return Path.cwd()

def getParentDirectory():
    return Path.cwd().parent
    
def getJabRefDirectory():
    return getParentDirectory() / 'JabRef_architecture'

def collectDataFromDirectory(csvFile, directoryPath, labels):
    for label in labels:
        DataSet( str(directoryPath / label), label, csvFile)
