#!/usr/bin/python

import logging
import sys
import os
from   ansible.inventory.ini import InventoryParser

def parseCmdLineArgs():
    """ Command line parsing and validation """
    if sys.argv < 2:
        logging.error('Please provide a ini file name')
        sys.exit(1)

    iniFile = sys.argv[1]

    if not os.path.isfile(iniFile):
        logging.error('Ini File does not exists: %s' % (iniFile))
        sys.exit(1)

    return iniFile

if __name__ == '__main__':
    iniFile = parseCmdLineArgs()
    ini     = InventoryParser(iniFile)
    for name in ini.hosts:
        print 'Host %s' % (name)
        vars = ini.hosts[name].get_variables()
        for var in vars:
            # filter out variables with _. Ansible adds variables like ansible_hostname.
            # SSH does not have any keyword with the underscore
            if not '_' in var:
                print "    %s %s" % (var, vars[var])
