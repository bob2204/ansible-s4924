#!/usr/bin/python
# -*- encoding: utf8 -*-
#

def msg(data,str):
    return data + ' ' + str

class FilterModule(object):
    ''' Give back filters to Ansible '''

    def filters(self):
        return {
            'filtre_test': msg
        }
