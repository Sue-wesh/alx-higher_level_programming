#!/usr/bin/python3
"""
lists all State objects, and corresp...City objects, contained in the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_city import City
from relationship_state import State, Base
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
        for cities in state.cities:
            print("    {}: {}".format(cities.id, cities.name))
        session.close()
