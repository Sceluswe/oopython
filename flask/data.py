#!/usr/bin/env python3

"""
A module for the data class.
"""

class Data:
    """
    A class containing data.
    """

    def __init__(self, linklist, pagetitle, imgLink):
        """
        Constructor.
        """
        # save the links here and use a pythonic for loop to print out the links.
        self.list_linkList = linklist
        self.str_pageTitle = pagetitle
        self.str_imgLink = imgLink
