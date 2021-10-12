from simple_db.db import DB
import json

DB_FILEPATH = 'tests/__db/test.json'
db = DB(DB_FILEPATH)

with open(DB_FILEPATH, 'w+') as f:
    json.dump([], f)
