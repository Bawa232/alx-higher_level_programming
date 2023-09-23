#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # connect to database using SQLAlchemy
    usern, passw, dbname = sys.argv[1:]
    engine = create_engine(f'mysql://{usern}:{passw}@localhost:3306/{dbname}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_s = Session()

    # query for states that contain letter "a" and print them
    states = db_s.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
