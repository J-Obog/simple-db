import ast 
import test_read
import uuid
import datetime

def setData(data, currentData):
    data["_id"] = uuid.uuid4().hex
    currentData.append(data)
    #print(currentData)
    with open("test", "w") as file: 
        file.write(str(currentData))
        print("Success!")
    #print(datetime.datetime.now().timestamp())
    #print(data)


sampleData = {
    "name":"Bill Clinton",
    "electionYear":1992,
    "party":"D"
}


setData(sampleData, test_read.getData())