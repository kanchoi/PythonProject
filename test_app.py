import app

def test_message():
    assert app.get_message() == "Hello, World!"

def test_check_db_connection():
    assert app.check_db_connection() is True

def test_add_number():
    assert app.add_integer(1,2) == 3
    assert app.add_integer(3,5) == 8
