from sdb import SimpleDB
from query import QueryManager

"""
pres1 = {
    "name":"Bill Clinton",
    "electionYear":1992,
    "party":"D"
}
pres2 = {
    "name":"Donald Trunp",
    "electionYear":2016,
    "party":"R"
}

pres3 = {
    "name":"Ronald Reagan",
    "electionYear":1980,
    "party":"R"
}
"""

q = QueryManager("server", "todo", "task")

res = q.getById("4d7505a1d6cf44a2bad3f1dfafdab2da")
#print(res)

someNums = [1,5,3,4,6]

for [i,v] in enumerate(someNums):
    print(i, v)

"""
q.create(pres1)
q.create(pres2)
q.create(pres3)
"""