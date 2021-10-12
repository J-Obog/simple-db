from . import db

def test_add():
    db.remove()
    db.add({'name': 'Joshua', 'age': 20})
    res = db.get()
    assert res == [{'name': 'Joshua', 'age': 20}]
