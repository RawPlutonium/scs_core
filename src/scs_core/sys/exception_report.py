"""
Created on 9 Jan 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import sys
import traceback

from collections import OrderedDict

from scs_core.data.json import JSONable
from scs_core.sys.trace_entry import TraceEntry


# TODO: do we need numeric fields for trace in order to comply with a schema?
# http://softwareengineering.stackexchange.com/questions/298364/exception-handling-in-python-am-i-doing-this-wrong-and-why

# --------------------------------------------------------------------------------------------------------------------

class ExceptionReport(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    # TODO: add a print(ex) method?

    @classmethod
    def construct(cls, ex):
        excls = ex.__class__
        args = ex.args

        info = sys.exc_info()

        if len(info) < 3:
            return ExceptionReport(excls, args, None, None)

        tb = info[2]
        fe = traceback.format_exception(excls, ex, tb)
        entries = [entry.strip() for entry in fe]

        trace = [TraceEntry.construct(line) for line in entries[1:-1]]
        summary = entries[-1]

        return ExceptionReport(excls, args, trace, summary)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, cls, args, trace, summary):
        """
        Constructor
        """
        self.__cls = cls
        self.__args = args
        self.__trace = trace
        self.__summary = summary


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['cls'] = self.cls.__name__
        jdict['args'] = self.args
        jdict['trace'] = self.trace
        jdict['sum'] = self.summary

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def cls(self):
        return self.__cls


    @property
    def args(self):
        return self.__args


    @property
    def trace(self):
        return self.__trace


    @property
    def summary(self):
        return self.__summary


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        args = '[' + ', '.join(str(arg) for arg in self.args) + ']'
        trace = '[' + ', '.join(str(entry) for entry in self.trace) + ']'

        return "ExceptionReport:{cls:%s, args:%s, trace:%s, summary:%s}" % \
               (self.cls.__name__, args, trace, self.summary)
