"""
A container for different type of dogs.
"""

class DogType:
    """
    Container class for different types of dogs.
    """

    def __init__(self, str_size, int_cost, int_numberOfAllowedDogs):
        """
        Constructor.
        """
        # Private list of dogs.
        self._list_dogs = list()
        self.str_size = str_size
        self.int_cost = int_cost
        self.int_numberOfAllowedDogs = int_numberOfAllowedDogs

    def addDog(self, obj_newDog):
        """
        Add a dog to the dog list.
        Returns true or false depending on success.
        """
        bool_result = False

        if len(self._list_dogs) < self.int_numberOfAllowedDogs and             obj_newDog.str_size == self.str_size:
            self._list_dogs.append(obj_newDog)
            bool_result = True

        return bool_result

    def retrieveDog(self, str_dogName):
        """
        Returns a dog based on name object.
        """
        result = False

        for i, dog in enumerate(self._list_dogs):
            if dog.str_name == str_dogName:
                result = self._list_dogs[i]
                del self._list_dogs[i]

        return result
