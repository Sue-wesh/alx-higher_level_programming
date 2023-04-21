#!/usr/bin/python3
"""
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
    for st in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
        for c in state.cities:
            print("    {}: {}".format(c.id, c.name))
        session.close()
