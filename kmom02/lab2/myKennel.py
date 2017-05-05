"""
A Kennel object for dog objects sorget in DogType objects.
"""

import myDogType

class Kennel:
    """
    A class for a Kennel/dog day-care.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.dict_ourDogTypes = {"small": myDogType.DogType("small", 109, 3),
                                 "medium": myDogType.DogType("medium", 125, 2),
                                 "big": myDogType.DogType("big", 172, 1)}

    def dogCheckIn(self, obj_newDog):
        """
        Checks in a dog, adds it to the appropriate DogType.
        Returns True or False.
        """
        return self.dict_ourDogTypes[obj_newDog.str_size].addDog(obj_newDog)

    def retrieveDog(self, str_dogName, str_dogSize):
        """
        Removes a dog from its DogType and returns the cost for having it there.
        """
        finalCost = "Dog doesn't exist."
        # Get dogs of the correct type.
        list_dogs = self.dict_ourDogTypes[str_dogSize]
        # Get the correct dog, if there is one.
        dog = list_dogs.retrieveDog(str_dogName)
        # Make sure we have a dog.
        if dog is not False:
            finalCost = dog.int_numberOfDays * list_dogs.int_cost

        return finalCost
