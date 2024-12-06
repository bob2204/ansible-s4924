#!/usr/bin/python
#

from ansible.plugins.lookup import LookupBase

def explode(str):
    return list(str)

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
            str = terms.pop(0)
            return explode(str)
