import logging

logger = logging.getLogger(__name__)

query = "SELECT breeds FROM breeds"
results = ["buldog", "french bul", "pudel", "terier", "york"]

def test_database_data(db_cursor):
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    assert result is not None

    for breed in result:
        index = result.index(breed)
        logger.info(f"Get result '{breed[0]}' from the database")
        assert breed[0] == results[index]
