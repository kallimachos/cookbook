#!/bin/python3
"""Basic sqlite example."""

import json
import sqlite3 as sql
from os import path, remove


def add(database):
    """Add an item to the DB."""
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("""INSERT INTO Users VALUES (1, 'Brian', 123456789,
                    'email@example.com', NULL)""")
        resp = json.dumps(cur.rowcount)
        return(resp)


def createdb(database):
    """Create an sqlite database."""
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS Users""")
        cur.execute("""CREATE TABLE Users
                    (id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone INT,
                    email TEXT unique,
                    image BLOB)""")
    return(True)


def delete(database):
    """Delete an item from the DB."""
    con = sql.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Users WHERE name = 'Brian'")
        resp = json.dumps(cur.rowcount)
    return(resp)


def test_createdb():
    """Test createdb()."""
    assert createdb('example.sqlite') is True


def test_add():
    """Test add()."""
    assert add('example.sqlite') == '1'


def test_delete():
    """Test delete()."""
    assert delete('example.sqlite') == '1'


def test_cleanup():
    """Remove example.sqlite file."""
    if path.exists('example.sqlite'):
        remove('example.sqlite')
    assert True is True


if __name__ == '__main__':
    pass
