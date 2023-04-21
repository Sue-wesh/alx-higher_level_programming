#!/usr/bin/python3
"""
class definition of City
"""
from relationship_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """
    class definition of cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
