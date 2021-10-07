import json 

class DB:
    def __init__(self, path):
        self.path = path

    #adding data
    def add(self, obj):
        data = self.get()
        with open(self.path, 'w') as file:
            data.append(obj)
            json.dump(data, file)

    #bulk adding support
    def add_many(self, arr):
        data = self.get()
        with open(self.path, 'w') as file:
            json.dump(data + arr, file)

    #getting data
    def get(self, fn=None):
        with open(self.path, 'r') as file: 
            data = json.load(file)
            return list(filter(fn, data)) if fn else data 

    #update data
    def set(self, obj, fn=None):
        data = self.get()
        with open(self.path, 'w') as file:
            data = list(map(lambda x: {**x, **obj} if fn(x) else x, data)) if fn else data
            json.dump(data, file)

    #deleting data
    def remove(self, fn=None):
        data = self.get()
        with open(self.path, 'w') as file:
            data = list(filter(lambda x: not fn(x), data)) if fn else []
            json.dump(data, file)