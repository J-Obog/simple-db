import ast 
import uuid 

class QueryManager():
    def __init__(self, hostName="server", dbName="test", tableName="someTable"):
        self.host = hostName
        self.db = dbName
        self.tbl = tableName
        self.tblpath = f"{hostName}/{dbName}/{tableName}"
    ##CREATE
    def create(self, data):
        items = self.getAll()
        data["_id"] = uuid.uuid4().hex
        items.append(data)
        with open(self.tblpath, "w+") as tbl_ref: 
            tbl_ref.write(str(items))

    ##READ
    def getAll(self):
        with open(self.tblpath, "r") as data:
            res = ast.literal_eval(data.read()) 
            return res
    
    def getById(self, id):
        items = self.getAll()
        res = filter(lambda item: item["_id"] == id, items)
        return list(res) 
    
    ##UPDATE
    def setById(self, id): 
        pass

    ##DELETE
    def removeById(self):
        pass

    def removeAll(self):
        pass


