from simple_db.db import DB

presidents = DB('db/presidents.json')

"""
presidents.add_many([
    {'name': 'Joe Biden', 'party': 'D', 'year_elected': 2020},
    {'name': 'Donald Trump', 'party': 'R', 'year_elected': 2016},
    {'name': 'Barack Obama', 'party': 'D', 'year_elected': 2008},
    {'name': 'George W Bush', 'party': 'R', 'year_elected': 2000},
])
"""

res = presidents.get() 
print(res)