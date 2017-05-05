#!/usr/bin/env python3

"""
09b4916ed6147e4504d3d1c88d71f2f9
oopython
lab3
emmd12
2017-02-22 13:03:01
v2.2.30 (2017-02-14)

Generated 2017-02-22 14:03:02 by dbwebb lab-utility v2.2.30 (2017-02-14).
https://github.com/mosbth/lab
"""

# pylint: disable=line-too-long
# pylint: disable=unused-import
import re
from dbwebb import Dbwebb

# pylint: enable=unused-import
#
TEXTFILE = open('ircLog.txt', 'r')
IRCLOG = TEXTFILE.read()
TEXTFILE.close()


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/howto/regex.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Regular expressions
#
#
# The lab consists of three sections. In section one you will practice regex
# on strings. In section two you will practice regex on the content from a
# file, the irc log. In section three you will practice on replacing text in
# strings.
# In section two, use your patterns on the variable `IRCLOG`.
#
# Use double backslashes (`\`) or raw string notation to avoid validation
# errors.
#
# Answer with the result from the re functions unless specified differently
# in the assignment.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Write a pattern that matches the word `can` in the sentence
# 'how can a clam cram in a clean cream can?'.
#
# Use the re modules findall function.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "how can a clam cram in a clean cream can?"

can = re.findall("can", line)


ANSWER = can

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Write a pattern that only matches the words that start with a *big letter*
# in the sentence
# 'Droskkusken Max kuskar med Fuxar och fuskar med droskkusktaxan.'.
#
# Use the re modules findall function.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "Droskkusken Max kuskar med Fuxar och fuskar med droskkusktaxan."

match = re.findall(r"[A-Z]\w*", line)


ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Write a pattern that only matches the `digits` in the string
# 'hej123ko whatup"563" koll726kolla'.
#
# Use the re modules findall function.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "hej123ko whatup'563' koll726kolla"

match = re.findall(r"([0-9][0-9][0-9])", line)


ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Write a pattern that matches the characters `()[] and {}` and `the words
# inside`, in the string
# '[kossor],(blommor),{skor},kossor,blommor,skor'.
#
#
# Use the re modules findall function.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "[kossor],(blommor),{skor},kossor,blommor,skor"

match = re.findall(r"[\[\(\{][a-z]*[\]\)\}]", line)


ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (2 points)
#
# Write a pattern that matches the scheme, the host and the port(if present)
# from the urls in the string
# 'https://dbwebb.se/kunskap/uml#sequence, ftp://bth.com:32/files/im.jpeg,
# file://localhost:8585/zipit, http://v2-dbwebb.se/do%hack'.
#
# A tip, create a group for each element. From the first url we want https
# and dbwebb.se from the second url we want ftp, bth.com and 32 and so on.
#
# Use the re modules findall function. Convert the result to a string and
# answer with it.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "https://dbwebb.se/kunskap/uml#sequence, ftp://bth.com:32/files/im.jpeg, file://localhost:8585/zipit, http://v2-dbwebb.se/do%hack"

match = re.findall(r"([^\W]\w*)://([\w.-]*)[/|:]([\d]*)", line)

mystring = ""
mystring += str([group for group in match])


ANSWER = mystring

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# --------------------------------------------------------------------------
# Section 2. Regex on content from a file
#
# Use the re modules findall function with the variable `IRCLOG`.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Find the whole line where someone talks about `Kaffe`.
#
# Answer with the whole line.
#
# Write your code below and put the answer into the variable ANSWER.
#

match = re.findall(r"[^\n].*Kaffe.*[^\n]", IRCLOG)




ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Find all the lines where `feeloor` joins or quits.
#
# Answer with all the lines.
#
# Write your code below and put the answer into the variable ANSWER.
#

match = re.findall(r".*feeloor.* [joins|quits].*", IRCLOG)




ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (2 points)
#
# At what time interval did `Trekka12` have a `genombrott` with his
# `snakespel`?
#
# Answer with the time interval.
#
# Write your code below and put the answer into the variable ANSWER.
#

match = re.findall(r".*Trekka12.*genombrott.*snakespel.*(\d\d:\d\d-\d\d:\d\d)", IRCLOG)


ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Find the two users who talk to `eline` about `git`/`Git`.
#
# Answer with the two usernames.
#
# Write your code below and put the answer into the variable ANSWER.
#

match = re.findall(r"<.(\w*)>.*eline.*git", IRCLOG)

match.pop(0)

ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (2 points)
#
# Find all the users who talk about themselves.
#
# Tip, create a group and reference to it.
# Answer with the usernames.
#
# Write your code below and put the answer into the variable ANSWER.
#

match = re.findall(r"<.(\w*)> .*\1.*", IRCLOG)


ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (2 points)
#
# Find the users who have atleast one digit in their name and have made a
# forum post in the category `oophp`.
#
# Tip, marvin says when someone makes a forum post.
# Answer with the usernames.
#
# Write your code below and put the answer into the variable ANSWER.
#

match = re.findall(r"marvin.*oophp.*av\s([\w-]*\d+[\w-]*)\s", IRCLOG)




ANSWER = match

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Search and replace
#
# Use the re modules sub function for all the exercises.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Use the sub function to fix the whitespaces in the sentence
# 'I  know	      H.T.M.L. 	How To      Meet Ladies'.
#
# One space between each word.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "I  know	      H.T.M.L. 	How To      Meet Ladies"

sub = re.sub(r"\s+", " ", line)


ANSWER = sub

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Use the sub function to switch the place of the numbers and letters in the
# string
# 'abc123 efg456'
# and also add a space between them, so it becomes '123 abc 456 efg'
#
# Write your code below and put the answer into the variable ANSWER.
#

sub = re.sub(r"([a-z]*)([\d]*)", r"\2 \1", 'abc123 efg456')




ANSWER = sub

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Use the sub function to remove the last three characters from the string
# 'Hello world!-.1'.
#
# Write your code below and put the answer into the variable ANSWER.
#

sub = re.sub(r"[^a-zA-Z\s!]", r"", "Hello world!-.1")




ANSWER = sub

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.4 (1 points)
#
# Use the sub function to remove the commented and the empty line from the
# string
# "#Did you back up the system?\n\nprint('hello world')".
#
# Write your code below and put the answer into the variable ANSWER.
#
line = "#Did you back up the system?\n\nprint('hello world')"
sub = re.sub(r"[# ?\w]+[\Wn]+(.*)", r"\1", line)




ANSWER = sub

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.5 (3 points)
#
# Use the sub function to format the string
# 'Ross McFluff: 0456-45324: 155 Elm Street\nRonald Heathmore: 5543-23464:
# 445 Finley Avenue'.
# For each person it should look like this:
# 'Contact
# Name: xx yy
# Phone number: 0000-00000
# Address: 000 zzz zzz'.
#
# Write your code below and put the answer into the variable ANSWER.
#

line = "Ross McFluff: 0456-45324: 155 Elm Street\nRonald Heathmore: 5543-23464: 445 Finley Avenue"

regex_format = r"([A-Z][a-z]+ [A-Z][\w]+): (\d+-\d+): (\d+ \w+ \w+)"

sub = re.sub(regex_format, r"Contact\nName: \1\nPhone number: \2\nAddress: \3", line)




ANSWER = sub

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.5", ANSWER, True)


dbwebb.exit_with_summary()
