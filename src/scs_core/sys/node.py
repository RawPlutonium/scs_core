"""
Created on 4 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from abc import abstractmethod


# --------------------------------------------------------------------------------------------------------------------

class Node(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def name(self):
        pass


    @abstractmethod
    def scs_dir(self):
        pass


    @abstractmethod
    def conf_dir(self):
        pass


    @abstractmethod
    def aws_dir(self):
        pass


    @abstractmethod
    def osio_dir(self):
        pass
