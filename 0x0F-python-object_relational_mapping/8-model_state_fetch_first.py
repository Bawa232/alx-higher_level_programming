#!/usr/bin/python3
"""
    a script that prints the first State
    object from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # connect to database using SQLAlchemy
    usernm, passw, dbname = sys.argv[1:]
    engine = create_engine(f'mysql://{usernm}:{passw}@localhost:3306/{dbname}')
    Base.metadata.create_all(engine)
    LocalSession = sessionmaker(bind=engine)
    db = LocalSession()

    # first_state for all states and print them
    first_state = db.query(State).order_by(State.id).first()
    if not first_state:
        print('Nothing')
    else:
        print(f'{first_state.id}: {first_state.name}')
