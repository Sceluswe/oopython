#!/usr/bin/env python3

"""
3d7bb02eba6523a17df5a35ac2f6a1c1
oopython
lab2
emmd12
2017-02-04 16:47:34
v2.2.28* (2017-02-01)

Generated 2017-02-04 17:47:35 by dbwebb lab-utility v2.2.28* (2017-02-01).
https://github.com/mosbth/lab
"""


from dbwebb import Dbwebb
import myDate
import myDog
import myDogType
import myKennel

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
#
#



# --------------------------------------------------------------------------
# Section 1. More classes
#
# Practice more on creating classes in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1
#
# Create a new class named Date.
# Declare the variables `year`, `month` and `day` in the constructor.
# Give it a `info` method that returns a date as a string with the format
# "year-mm-dd". Numbers below 10 should have a leading zero when printed in
# the info method.
#
#
# Initialize a new variable called `date1` which contains a *Date object*,
# give it year `2005`, month `1` and day `4`.
#
# Answer with the result from the info method.
#
# Write your code below and put the answer into the variable ANSWER.
#

date1 = myDate.Date(2005, 1, 4)


ANSWER = date1.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2
#
# Overload the `smaller than method(<)` in the Date class.
# It should return True if date comes before the other.
#
# Initialize a new Date variable called `date2` , give it year `2000`, month
# `11` and day `26`.
#
# Answer with `date1<date2`.
#
# Write your code below and put the answer into the variable ANSWER.
#

date2 = myDate.Date(2000, 11, 26)


ANSWER = date1 < date2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3
#
# For the next few exercises we will work on a dog kennel, we will have three
# classes when we are done, *Dog*, *DogType* and *Kennel*.
#
# Create a new class called Dog. Declare the variables `name`, `size`, `race`
# and numberOfDays (to stay at kennel) in the constructor.
# Give it a method that returns a string of its information in the format
# "name: xxx, size: ccc, race: fff, nrOfDays: 000".
#
# In the code below initialize a new Dog variable calle `dog1`, give it the
# name "Buster", the size "small", the race "Shitzu" and `6` days to stay.
#
# Answer with the info method of `dog1`.
#
# Write your code below and put the answer into the variable ANSWER.
#



dog1 = myDog.Dog("Buster", "small", "Shitzu", 6)



ANSWER = dog1.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4
#
# The next class that you will create will hold dogs of a certain type. Eg.
# small, medium or big sized.
#
# Create a new class called DogType. In the constructor declare the variables
# `size`, `cost` (per day), `numberOfAllowedDogs` and a private list that
# will contain *Dog objects*. Declare the list containing `Dogs` to an empty
# list in the constructor.
# Give the class a new method called `addDog`, it should take a Dog object as
# parameter. In the method add the Dog to the list if you have room for it
# and it has the correct size. If you add the dog return `True` otherwise
# return `False`.
#
# Initialize a new DogType variable in the code below, name it `smallDogs`,
# set `size` to "small", `cost` to `109` and `numberOfAllowedDogs` to `3`.
# Use the add method to add dog1.
#
# Answer with the result from adding `dog1` to `smallDogs`.
#
# Write your code below and put the answer into the variable ANSWER.
#



smallDogs = myDogType.DogType("small", 109, 3)




ANSWER = smallDogs.addDog(dog1)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5
#
# In the DogType class create a new method called `retrieveDog`, take a
# `name` as parameter. If the dogs name is the same as a dog  in the list
# remove it from the list and return the object, otherwise return `False`.
#
# In the code below retrieve "Buster" from `smallDogs`.
#
# Answer with the returned Dogs number of days stayed.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = smallDogs.retrieveDog("Buster").int_numberOfDays

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6
#
# Time to make the Kennel class. Choose a way to store three *DogType
# objects*, a list, a dictionary or one variable for each. We will have the
# dog types `small`, `medium` and `big` dogs.
# In the constructor:
# Initialize the DogType for small dogs with size "small", cost `109` and
# numberOfAllowedDogs `3`.
# Initialize the DogType for medium dogs with size `medium`, cost `125` and
# numberOfAllowedDogs `2`.
# Initialize the DogType for big dogs with size `big`, cost `172` and
# numberOfAllowedDogs `1`.
#
# Create a method in Kennel that checks-in a new dog at the Kennel, it takes
# a *Dog object* as parameter. In the method add the dog to the appropriate
# DogType and return whats returned from the DogType `addDog` method.
#
# In the code below initialize a new Kennel variable and check-in `dog1` to
# the kennel.
#
# Answer with the result from the check-in.
#
# Write your code below and put the answer into the variable ANSWER.
#

dogKennel = myKennel.Kennel()


ANSWER = dogKennel.dogCheckIn(dog1)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7
#
# Create a new method in the kennel class for checking out a Dog. It takes a
# `name` and `size` as parameter.
# In the method try to retrieve the dog from appropriate DogType with the
# DogType method `retrieveDog`. The check out method should return the `cost`
# for having the dog at the Kennel, aka days stayed * cost of size.
#
# In the code below create a new Dog variable called `dog2`, give it the name
# "Zimba", the size "big", the race "Rottweiler" and `10` days to stay.
# Check-in `dog2` at the kennel and checkout `dog1`, "Buster", "small", from
# the Kennel.
#
# Answer with the price of having `dog1` at the Kennel, the result from the
# check out method.
#
# Write your code below and put the answer into the variable ANSWER.
#

dog2 = myDog.Dog("Zimba", "big", "Rottweiler", 10)

dogKennel.dogCheckIn(dog2)



ANSWER = dogKennel.retrieveDog("Buster", "small")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8
#
# Create a class named Present.
# Declare the variables `content` and `recipient` in the constructor.
# Give it a `info` method where you return "content: xxx, recipient: yyy".
#
# Initialize a new Present variable in the code below named `present`. Give
# it the content "Ozelot", recipient "Kvothe".
#
# Answer with the result from the `info` method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Present:
    """
    A gift class, containing the receiver and the content.
    """

    def __init__(self, obj_content, str_recipient):
        """
        Constructor.
        """
        self.obj_content = obj_content
        self.str_recipient = str_recipient

    def info(self):
        """
        Return content and recipient.
        """
        return "content: " + self.obj_content + ", recipient: " + self.str_recipient

present1 = Present("Ozelot", "Kvothe")


ANSWER = present1.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9
#
# Create a new class called ChristmasPresent it should *inherit from
# Present*.
# Give ChristmasPresent the variale `rhyme`. Use *super* to initiate the
# variables from the parent class (Present) with `content` and `recipient`
# from the constructor.
#
# Override the `info` method from Present to return "content: xxx, recipient:
# yyy, rhyme: zzz". A tip, you can access the parent method with super and
# just add rhyme to the returned string and return that.
#
# Create a new ChristmasPresent variable in the code below. Give it the
# content "Pirate", recipient "Zeldah" and rhyme "You, oh, oh, a Christmas.
# My Christmas tree is delicious".
#
# Answer with the christmas presents `info` method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class ChristmasPresent(Present):
    """
    A ChristmasPresent.
    """
    def __init__(self, obj_content, str_recipient, str_rhyme):
        self.str_rhyme = str_rhyme
        super().__init__(obj_content, str_recipient)

    def info(self):
        """
        Returns info of parent and the rhyme of self.
        """
        return super().info() + ", rhyme: " + self.str_rhyme

rhyme = "You, oh, oh, a Christmas. My Christmas tree is delicious"

obj_christmassPresent1 = ChristmasPresent("Pirate", "Zeldah", rhyme)





ANSWER = obj_christmassPresent1.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.9", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.10
#
# Create a new class called CompanyPresent it should *inherit from Present*.
#
# Give CompanyPresent the variale `Cost`. Use "super" to initiate the
# variables from the parent class (Present) with content and recipient from
# the constructor.
#
# Override the `info` method from Present to return "content: xxx, recipient:
# yyy, cost: zzz". A tip, you can access the parent method with super and
# just add cost to the returned string and return that.
#
# Create a new CompanyPresent variable in the code below. Give it the content
# "Icecream", recipient "Lew" and cost `16`.
#
# Write your code below and put the answer into the variable ANSWER.
#

class CompanyPresent(Present):
    """
    A special present for employees.
    """
    def __init__(self, obj_content, str_recipient, int_cost):
        """
        Constructor.
        """
        self.int_cost = int_cost
        super().__init__(obj_content, str_recipient)

    def info(self):
        """
        Prints the Present info and the cost of the CompanyPresent.
        """
        return super().info() + ", cost: " + str(self.int_cost)

obj_companyPresent1 = CompanyPresent("Icecream", "Lew", 16)


ANSWER = obj_companyPresent1.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.10", ANSWER, False)


dbwebb.exit_with_summary()
