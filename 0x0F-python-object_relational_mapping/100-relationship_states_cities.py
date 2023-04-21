#!/usr/bin/python3
"""
City class:
    No change
State class:
    class attribute cities must represent a relationship with the class City. 
    If the State object is deleted, all linked City objects must be automatically 
    deleted
"""
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3],
                                  pool_pre_ping=True))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', states=california)

    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
