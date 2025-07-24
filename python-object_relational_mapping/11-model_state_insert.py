#!/usr/bin/python3
"""Add a new state"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                         argv[2],
                                                         argv[3]),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    session.commit()
    i = session.query(State).filter(State.name == "Louisiana").first()
    print(i.id)
    session.close()
