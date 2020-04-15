from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Data(Base):
    __tablename__ = "inventory"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String, unique=True)
    count = Column('count', Integer)
    price = Column('price', Float)


engine = create_engine('sqlite:///inventory.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

def add_item(item, count, price):
    session = Session()

    data = Data()
    data.item = item
    data.count = count
    data.price = price

    session.add(data)
    session.commit()
    session.close()

def query_item(item):
    session = Session()
    result = session.query(Data).filter(Data.item == item).all()
    if result == []:
        return False
    else:
        return True
    session.close()

def query_id(id):
    session = Session()
    result = session.query(Data).filter(Data.id == id).all()
    print(result)
    session.close()

def query_all():
    session = Session()
    result = session.query(Data).all()
    list = []
    for item in result:
        list.append([item.id, item.item, item.count, item.price])
    session.close()
    return list

def delete_item(item):
    session = Session()
    session.query(Data).filter(Data.item == item).delete()
    session.commit()
    session.close()

def delete_id(id):
    session = Session()
    session.query(Data).filter(Data.id == id).delete()
    session.commit()
    session.close()

def number_of_rows():
    session = Session()
    result = session.query(Data).count()
    session.close()
    return result

def number_of_columns():
    session = Session()
    result = 4
    session.close()
    return result
#add_item("dd",88,99.9)

#query_item("cupcake")
#query_id(0)
#delete_item(3)
#delete_item("dd")
#number_of_columns()
#print(number_of_rows())