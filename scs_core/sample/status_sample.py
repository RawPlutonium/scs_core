"""
Created on 20 Oct 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.sample.sample import Sample


# --------------------------------------------------------------------------------------------------------------------

class StatusSample(Sample):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, tag, rec, location, temperature, schedule, uptime, psu_status):
        """
        Constructor
        """
        val = []

        if location:
            val.append(('loc', location))

        val.append(('tmp', temperature))
        val.append(('sch', schedule))
        val.append(('up', uptime))

        if psu_status:
            val.append(('psu', psu_status))

        super().__init__(tag, rec, *val)