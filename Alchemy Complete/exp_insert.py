from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

metadata = MetaData() # metadata is collection of tables and can be traversed like XML DOM

user_table = Table("user", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
    )


# i am doing this to make engine 
from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)

# create all tables from metadata
metadata.create_all(engine)

# insert data
sql = user_table.insert().values(name = "shashank")
conn = engine.connect();
result = conn.execute(sql);
conn.close();

# insert data in batch learning to add the json formats
conn = engine.connect();
result = conn.execute(user_table.insert(), [{"name":"bang"}, {"name":"lore"}])
conn.close();

# insert data in batch variant
sql = user_table.insert().values([{"name":"naruto"}, {"name":"sasuke"}])
conn = engine.connect();
result = conn.execute(sql);
sql2 = conn.execute("SELECT * FROM user")
conn.close();

for row in sql2:
    print("DATA: " + repr(row))