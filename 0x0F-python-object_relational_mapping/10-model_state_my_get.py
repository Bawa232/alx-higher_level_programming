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
    usern, passw, dbn, state_name = sys.argv[1:]
    engine = create_engine(f'mysql://{usern}:{passw}@localhost:3306/{dbn}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_s = Session()

    # query for states that contain letter "a" and print them
    state = db_s.query(State).filter_by(name=state_name).first()
    if not state:
        print("Not found")
    else:
        print(f"{state.id}")
