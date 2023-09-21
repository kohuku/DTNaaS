import getpass

import sys
import pprint

pprint.pprint(sys.path)
import pyroute2


# import Flask


# print(getpass.getuser())
ipdb=pyroute2.IPDB()
interfaces = dir(ipdb.interfaces)
#print(interfaces)