"""
Connects to the database farm.sqlite. Provides CRUD functionality.
"""


# Import database functionality
import dbQuery
# Import tabel containers.
from animals import Animal
from humans import Human
from vehicles import Vehicle


# Skapa ett objekt att lägga till utifrån klassen Car
#aCar = Car(model="v40", price=150000, country="Sweden", manufacturer="Volvo")

# Lägg till i sessionen
#session.add(aCar)

#print(session.new)

# Slutför med commit()
#session.commit()

class Farm():
    """
    Extends and provides more specific functionality of dbQuery.
    """
    def __init__(self, str_dbPath):
        """
        Constructor.
        """
        self._db = dbQuery.dbQuery(str_dbPath)

    def displayAnimals(self):
        """
        Gets all animal rows and returns a dict of lists.
        """
        headers = ["Id", "Species", "Name", "Number of legs"]
        form = [
            {"type": "text", "name": "Species"},
            {"type": "text", "name": "Name"},
            {"type": "number", "name": "Number of legs", "alt": "min='0'"}
        ]
        rows = self._db.read(Animal)
        result = list()

        # Save the variables in a tuple.
        for row in rows:
            result.append((row.id, row.species, row.name, row.nr_of_legs))

        return {"headers": headers, "rows": result, "form": form}



    def displayHumans(self):
        """
        Gets all human rows and returns a dict of lists.
        """
        headers = ["Id", "Name", "Occupation", "Age"]
        form = [
            {"type": "text", "name": "Name"},
            {"type": "text", "name": "Occupation"},
            {"type": "number", "name": "Age", "alt": "min='0'"}
        ]
        rows = self._db.read(Human)
        result = list()

        # Save the variables in a tuple.
        for row in rows:
            result.append((row.id, row.name, row.occupation, row.age))

        return {"headers": headers, "rows": result, "form": form}



    def displayVehicles(self):
        """
        Gets all vehicle rows and returns a dict of lists.
        """
        headers = ["Id", "Type of vehicle", "Price"]
        form = [
            {"type": "text", "name": "Type of vehicle"},
            {"type": "number", "name": "Price", "alt": """min="0" """}
        ]
        rows = self._db.read(Vehicle)
        result = list()

        # Save the variables in a tuple.
        for row in rows:
            result.append((row.id, row.vehicle_type, row.price))

        return {"headers": headers, "rows": result, "form": form}



    def deleteAnimal(self, int_id):
        """
        Deletes one animal based on argument id.
        """
        self._db.delete(Animal, int_id)



    def deleteHuman(self, int_id):
        """
        Deletes one animal based on argument id.
        """
        self._db.delete(Human, int_id)



    def deleteVehicle(self, int_id):
        """
        Deletes one animal based on argument id.
        """
        self._db.delete(Vehicle, int_id)



    def createAnimal(self, species, name, nr_of_legs):
        """
        Create an Animal.
        """
        self._db.create(Animal(species, name, nr_of_legs))



    def createHuman(self, name, occupation, age):
        """
        Create an Animal.
        """
        self._db.create(Human(name, occupation, age))



    def createVehicle(self, vehicle_type, price):
        """
        Create an Animal.
        """
        self._db.create(Vehicle(vehicle_type, price))
