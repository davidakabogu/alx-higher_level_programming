#!/usr/bin/python3
"""Deletes State objects with a name containing the letter 'a'
from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

kini = "Usage: {} < mysql_username > < mysql_password > < database_name >"
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(kini.format(sys.argv[0]))

        # print("Usage: {} < mysql_username > < mysql_password >
        # < database_name >".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Construct the connection URL
    connection_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name
    )

    # Create an engine
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete State objects with names containing the letter 'a'
    states_to_delete = session.query(
            State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes and close the session
    session.commit()
    session.close()
