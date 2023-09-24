#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # Check command line arguments
    username, password, database = sys.argv[1:]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    # Create session
    LocalSession = sessionmaker(bind=engine)
    d = LocalSession()
    
    s = d.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    for city, state in s:
        print(f'{state.name}: ({city.id}) {city.name}')
