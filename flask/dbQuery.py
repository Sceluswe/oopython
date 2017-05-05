"""
dbQuery object that queries a database.
"""

# Import framework.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class dbQuery():
    """
    Provides basic connect functionality to the database.
    """
    def __init__(self, str_dbPath):
        # Connect to the database.
        engine = create_engine("sqlite:///" + str_dbPath)

        # Create session.
        Session = sessionmaker(bind=engine)

        # Save session as private variable.
        self._session = Session()


    def create(self, obj_tableobj):
        """
        Allows the user to create a row in the specified table.
        @query_obj, is either a "declarative_base" object or a list.
        """
        self._session.add(obj_tableobj)
        #print("Creating object:" + str(self._session.new))
        self._session.commit()


    def read(self, obj_tableobj):
        """
        Reads from the database and returns a list of objects, one for each row.
        """
        return self._session.query(obj_tableobj).all()


    def delete(self, obj_tableobj, int_id):
        """
        Allows the user to remove a row in the specified table, using its id.
        """
        self._session.query(obj_tableobj).filter(obj_tableobj.id == int_id).delete()
        self._session.commit()
