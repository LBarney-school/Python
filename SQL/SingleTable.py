"""First, create a MySql database or use an existing database and then create a table in the database called "Ages":

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)

Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Jiayi', 34);
INSERT INTO Ages (name, age) VALUES ('Kingston', 30);
INSERT INTO Ages (name, age) VALUES ('Kelan', 15);
INSERT INTO Ages (name, age) VALUES ('Temi', 26);
INSERT INTO Ages (name, age) VALUES ('Darroch', 17);

Once the inserts are done, run the following SQL command:

SELECT sha1(CONCAT(name,age)) AS X FROM Ages ORDER BY X

Find the first row in the resulting record set and enter the long string that looks like 254c6127cdbc4c38e065317667340e8b0950046f.
"""

import hashlib
import sqlite3

connection = sqlite3.connect("Ages.sqlite")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE Ages (name VARCHAR(128),age INTEGER)")
cursor.execute("DELETE FROM Ages;")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Jiayi', 34)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Kingston', 30)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Kelan', 15)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Temi', 26)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Darroch', 17)")

cursor.execute("SELECT (CONCAT(name,age)) AS X FROM Ages ORDER BY X")
for row in cursor.fetchall():
    tohash = row[0].encode()
    print("Hashed\t", row[0], "\tHash:", hashlib.sha1(tohash).hexdigest())


connection.commit()
connection.close()
