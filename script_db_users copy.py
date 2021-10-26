import sqlite3


conn = sqlite3.connect("login.db")
c = conn.cursor()

#c.execute("CREATE TABLE users (input_email text, input_password text)")
#conn.commit()


c.execute("INSERT INTO users VALUES('emyungu@gmail.com', '123456789')")
conn.commit()

c.execute("SELECT * FROM users")
#input_email = request.form["input_email"]
#input_password = request.form["input_password"]

for x in c.fetchall():
    print(x)