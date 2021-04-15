from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

metadata = MetaData() # metadata is collection of tables and can be traversed like XML DOM

user_table = Table("user", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
    )


# init engine over database
from sqlalchemy import create_engine, select
engine = create_engine("sqlite://", echo=True)


metadata.create_all(engine)

# insert data in batches as json
sql = user_table.insert().values([{"name":"shashank"}, {"name":"messi"}, {"name":"naruto"}, {"name":"sasuke"}, {"name":"jiaya"}])
conn = engine.connect()
result = conn.execute(sql)
conn.close();


# DELETE
sql = user_table.delete().\
    where(user_table.c.id == 2)

engine.execute(sql);

# SELECT
result = engine.execute(select([user_table]))
for row in result:
    print(row)