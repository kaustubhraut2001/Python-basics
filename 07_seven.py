import sqlite3

con = sqlite3.connect("sample.db")
print(con)
cur = con.cursor()

#cur.execute("CREATE TABLE TEST(Name, Number, Age)")

cur.execute("""
    INSERT INTO TEST VALUES
	('A', 1, 20),
	('B', 2, 21),
	('C', 3, 22),
	('D', 4, 23)
""")



res = cur.execute("SELECT * FROM TEST")
#print(res.fetchall())
data = [
	('E', 5, 24),
	('F', 6, 25),
	('G', 7, 26),
	('H', 8, 27)
]
cur.executemany("INSERT INTO TEST VALUES(?, ?, ?)", data)
cur.execute("SELECT * FROM TEST")
print(cur.fetchall())
con.commit()