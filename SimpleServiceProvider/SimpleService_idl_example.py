#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 \file SimpleService_idl_examplefile.py
 \brief Python example implementations generated from SimpleService.idl
 \date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import ysuga, ysuga__POA


class SimpleService_i (ysuga__POA.SimpleService):
    """
    \class SimpleService_i
    Example class implementing IDL interface ysuga.SimpleService
    """

    def __init__(self):
        """
        \brief standard constructor
        Initialise member variables here
        """

        self._data = 0
        pass

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    # long read(out long data)
    def read(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result, data
        return (0, self._data)

    # long write(in long data)
    def write(self, data):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        self._data = data
        return 0

    # long reset()
    def reset(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        buffer = self._data
        self._data = 0
        return buffer


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = SimpleService_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

