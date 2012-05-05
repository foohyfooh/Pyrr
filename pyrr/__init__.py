import pkgutil
import os
import pyrr

# the version of software
# this is used by the setup.py script
__version__ = '20120506'

# make 'from module import *' work dynamically.
# otherwise we have to manually update the __all__ list.
# http://stackoverflow.com/questions/1057431/loading-all-modules-in-a-folder-in-python
for module in os.listdir( os.path.dirname( __file__ ) ):
    name, extension = os.path.splitext( module )

    # don't import ourself
    if name == '__init__':
        print 'found init %s' % module
        continue

    # we can import .py, .pyc and .pyo file types
    if \
        extension != '.py' and \
        extension != '.pyc' and \
        extension != '.pyo':
        continue

    # file type is ok, import it
    __import__( name, locals(), globals() )
    del module

