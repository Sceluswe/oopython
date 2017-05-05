#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
7adb9ab377fc4a858832c70893858950
oopython
lab1
emmd12
2017-01-24 13:30:18
v2.2.26 (2017-01-20)

Generated 2017-01-24 14:30:18 by dbwebb lab-utility v2.2.26 (2017-01-20).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb
import Cat
import Dog
import BankAccount

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 1 - oopython

If you need to peek at examples or just want to know more, take a look at
the [Python documentation](https://docs.python.org/3/library/index.html).
Here you will find everything this lab will go through and much more.

"""



"""
--------------------------------------------------------------------------
Section 1. Objects and classes

Basic object oriented python.

"""



"""
Exercise 1.1

Create a class called Cat in a new file. Give the Cat the attributes
`eyeColor` and `name` in the constructor.

Dont forget to import the file.

In the code below initiate a variable named `cat` with a *Cat object*, give
it eye color "blue" and name "Basion".

Answer with the string "My cats name is `name` and has `eyeColor` eyes.".


Write your code below and put the answer into the variable ANSWER.
"""

cat = Cat.Cat("blue", "Basion")



ANSWER = "My cats name is {name} and has {eyeColor} eyes.".format(name=cat.str_name, eyeColor=cat.str_eyeColor)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Expand your Cat class with the variables `livesLeft`.

Initialize the attribute in the constructor to `-1`. In the code below
change the value to `9`.

Answer with number of lives the cat has left.


Write your code below and put the answer into the variable ANSWER.
"""

cat.int_livesLeft = 9




ANSWER = cat.int_livesLeft

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Create a new function in the Cat class, called `description()`, that
returns the string "My cats name is `name`, has `color` eyes and
`livesLeft` lives left to live.".

Answer with the result returned from the function.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = cat.description()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Create a new class named Dog, it should look the same as the Cat class. But
in the description function it should print "My dogs name..." instead of
"My cats name...".

In the constructor set lives left to live to `1`. Dont forget to import the
new class.
Initiate a new variable called `dog` with the *Dog class*, give dog the
name "Lilly" and eye color "blue".

Put cat and dog variables in a list. Iterate through the list and put their
descriptions together in a string without any seperation between the two.

Answer with the string.


Write your code below and put the answer into the variable ANSWER.
"""

dog = Dog.Dog("blue", "Lilly")

list_dogsAndCats = [cat, dog]
str_result = ""

for obj in list_dogsAndCats:
    str_result += obj.description()



ANSWER = str_result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Create a private variable for the Cat class called `evil`.
In the constructor the variable should be set to `True` by default if no
argument is given.

Create a function in the class that returns if the cat is evil or not.

Answer with if the cat is evil or not.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = cat.isEvil()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

In the code below create a function that takes a Cat object as an argument.
If attribute `evil` for Cat is true, return "All cats are evil!" otherwise
return "This cat is not evil!".

Answer with the returned string.


Write your code below and put the answer into the variable ANSWER.
"""

def areCatsEvil(Cat_obj):
    """
    Function that determines the alignment of cats.
    """
    str_align = "This cat is not evil!"

    if Cat_obj.isEvil():
        str_align = "All cats are evil!"

    return str_align





ANSWER = areCatsEvil(cat)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Create a static variable in the Cat class that contains the number of paws
a cat have. Set its value to `4` in the declaration.

Answer with the string "`Basion` has `4` paws."


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "{name} has {paws} paws.".format(name=cat.str_name, paws=cat.int_nrOfPaws)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

In the code below assign the number of paws variable for `cat` to `3`.

Answer with the string "`Basion` has `3` paws but cats have
`<Cat.nrOfpaws>` paws.".


Write your code below and put the answer into the variable ANSWER.
"""

cat.int_nrOfPaws = 3

str_info = "{name} has {paws} paws but cats have {catpaws} paws."


ANSWER = str_info.format(name=cat.str_name, paws=cat.int_nrOfPaws, catpaws=Cat.Cat.int_nrOfPaws)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Inheritance



"""



"""
Exercise 2.1

Create a new class, Animal, that will act as a *parent* to Cat and Dog.
The Animal class shall contain the attributes `name` and `eyeColor` instead
of the Cat and Dog classes.
Rewrite Dog and Cat so that they inherit from Animal.

Answer with the description from `cat` and `dog`, seperated with space.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = cat.description() + " " + dog.description()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Create a new function in Animal named `speak`, *force* child classes to
override it.

Overwrite it in Dog and Cat. In dog return "Voff" and in cat "Meow".

Create another function in Animal called `speakTwice`. It should return a
string where `self.speak` is called twice, with space as seperation between
the two.

Answer with `speakTwice` for cat.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = cat.speakTwice()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Create a static method in Dog called `interact`. Its input parameter should
be an object.
If the argument is of class Cat return the string "Chase!" otherwise return
"Lick!".

Answer with dog interact function and pass cat as argument.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = dog.interact(cat)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Overriding methods



"""



"""
Exercise 3.1

Create a new class called BankAccount.

Declare the attributes `balance` and `owner` in the constructor. `owner`
should be a private attribute.

The constructor should take the name for the owner as argument. Balance
should be initalized to `113` in the constructor.

BankAccount should also have four functions: `accountInfo` `getBalance`,
`depositMoney` and `withdrawMoney`.
accountInfo returns "`Misty` has `191` kr".
getBalance returns the balance.
depositMoney takes one argument, `amount`, and adds the amount to the
balance.
withdrawMoney draws the `amount` of money sent as an argument from balance.

In the code below create a function, where you create a *new instance of
the class BankAccount*, the function should take the `owner` name as
argument, and return the created object.

Create a new variable called `bankAccount1` and initialize it with the
create bank account function, name the owner "Misty".
Deposit `78` kr to the account and answer with the `accountInfo` function.


Write your code below and put the answer into the variable ANSWER.
"""

def newBankAccount(owner):
    """
    Create a new bankaccount object and returns it.
    """
    return BankAccount.BankAccount(owner)

bankAccount1 = newBankAccount("Misty")

bankAccount1.depositMoney(78)

ANSWER = bankAccount1.accountInfo()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2

Overload the *add(+)* function for the BankAccount class. The function
should be able to sum the balance of two bank accounts (BankAccount +
BankAccount) and BankAccount + an int.

Initiate a new BankAccount called `bankAccount2` with the owner "Misha" and
withdraw `52` kr from it.

Answer with `bankAccount1 + bankAccount2`.


Write your code below and put the answer into the variable ANSWER.
"""

bankAccount2 = newBankAccount("Misha")
bankAccount2.withdrawMoney(52)




ANSWER = bankAccount1 + bankAccount2

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3

Overload the *iadd(+=)* function for the BankAccount class. The function
should be able to add two bank accounts together (BankAccount +=
BankAccount) and BankAccount += an int.

Update `bankAccount1` with `bankAccount1 += bankAccount2`.

Answer with `accountInfo` for bankAccount1.


Write your code below and put the answer into the variable ANSWER.
"""

bankAccount1 += bankAccount2




ANSWER = bankAccount1.accountInfo()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, True))

"""
Exercise 3.4

If you look in the `iadd` and `add` functions for BankAccount you should be
using basically the same code in both functions.
To minize code size of the class, create a private function where you do
the shared calculations and then call it from `iadd` and `add`.

calculate `bankAccount2 += bankAccount1 + 5`.

Answer with bankAccount2.accountInfo()


Write your code below and put the answer into the variable ANSWER.
"""

bankAccount2 += bankAccount1 + 5




ANSWER = bankAccount2.accountInfo()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))


dbwebb.exitWithSummary()
