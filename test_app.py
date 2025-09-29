import app

def test_message():
    assert app.get_message() == "Hello World! Field Engineer"

def test_check_db_connection():
    assert app.check_db_connection() is True