from . import db

def test_get():
    db.remove()
    res1 = db.get()
    assert res1 == []
    db.add_many([{'name': 'Carly', 'age': 30}, {'name': 'Kyle', 'age': 19}, {'name': 'Mark', 'age': 27}, {'name': 'Jack', 'age': 18}])
    res2 = db.get(lambda x: x['age'] > 19) 
    assert res2 == [{'name': 'Carly', 'age': 30}, {'name': 'Mark', 'age': 27}]