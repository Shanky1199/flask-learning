from sqlalchemy import engine

engine = engine.create_engine('sqlite:///engine.db')

engine.execute("""CREATE TABLE employee (
id INTEGER PRIMARY KEY,
name VARCHAR(50)
)""")

# insert data (connectionless execution (via engine))
engine.execute("INSERT INTO employee (name) VALUES (:name)", name="Shashank")
engine.execute("INSERT INTO employee (name) VALUES (:name)", name="bangalore")
engine.execute("INSERT INTO employee (name) VALUES (:name)", name="internship")

# query data
result = engine.execute("select id, name from employee")
rows = result.fetchall()
result.close(); # should be done automatically

# display data
for row in rows: 
    print("DATA: " + repr(row))

print("done")