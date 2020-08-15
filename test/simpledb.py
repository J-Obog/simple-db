import os 

class SimpleDB():
    def __init__(self, hostName="server"):
        self.host = hostName
    ##CREATE
    def addDb(self, dbName):
        os.mkdir(f"{self.host}/{dbName}")

    def addTable(self, dbName, tableName):
        with open(f"{self.host}/{dbName}/{tableName}", "w+") as tbl: 
            emptyList = []
            tbl.write(str(emptyList))
    ##READ 
    def listDbs(self):
        return os.listdir(self.host)

    def listTables(self, dbName="test"):
        return os.listdir(f"{self.host}/{dbName}")
    ##UPDATE
    def renameDb(self, oldName, newName):
        os.rename(f"{self.host}/{oldName}", f"{self.host}/{newName}")
    ##DELETE
    def removeDb(self, dbName):
        os.rmdir(f"{self.host}/{dbName}")

    def removeTable(self, dbName, tableName):
        os.remove(f"{self.host}/{dbName}/{tableName}")