import json 

class DB:
    def __init__(self, path):
        self.path = path

    def _file_manip(self, data):
        with open(self.path, 'w') as file:
            json.dump(data, file)

    #adding data
    def add(self, obj):
        data = self.get()
        data.append(obj)
        self._file_manip(data)

    #bulk adding support
    def add_many(self, arr):
        data = self.get()
        self._file_manip(data + arr)

    #getting data
    def get(self, fn=None):
        with open(self.path, 'r') as file: 
            data = json.load(file)
            return list(filter(fn, data)) if fn else data 

    #update data
    def set(self, obj, fn=None):
        data = self.get()
        data = list(map(lambda x: {**x, **obj} if fn(x) else x, data)) if fn else data
        self._file_manip(data)

    #deleting data
    def remove(self, fn=None):
        data = self.get()
        data = list(filter(lambda x: not fn(x), data)) if fn else []
        self._file_manip(data)