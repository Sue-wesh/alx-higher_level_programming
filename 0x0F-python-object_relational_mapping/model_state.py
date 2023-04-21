#!/usr/bin/python3
"""
python file that contains the class definition of a State 
and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
"""
python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
meta = MetaData()
Base = declarative_base(metadata=meta)

class State(Base):
    """
    a State class for a MySQL database
    its mapped to table "states in the DB
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, auto_increment)
    name = Column(String(128), nullable=False)

engine = create_engine()
Base.metadata.create_all(engine)
