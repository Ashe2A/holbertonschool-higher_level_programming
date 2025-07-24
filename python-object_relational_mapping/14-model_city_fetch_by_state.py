#!/usr/bin/python3
"""Delete states"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


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
    for i in session.query(City).order_by(City.id).all():
        state = session.query(State).filter(State.id == i.state_id).first()
        print("{}: ({}) {}".format(state.name, i.id, i.name))
    session.close()
