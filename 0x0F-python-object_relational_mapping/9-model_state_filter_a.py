#!/usr/bin/python3
"""
prints the first State object from the database and use sqlalchemy
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                   pool_pre_ping=True))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%')).order_by(
                                        State.id).all()
    for q in query:
        print("{}: {}".format(q.id, q.name))
    session.close()
