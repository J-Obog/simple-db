from . import db

def test_add_many():
    db.remove()
    db.add_many([{'name': 'Carly', 'age': 30}, {'name': 'Kyle', 'age': 19}])
    res = db.get()
    assert res == [{'name': 'Carly', 'age': 30}, {'name': 'Kyle', 'age': 19}]
