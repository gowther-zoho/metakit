# all.py -- Run all tests for the MetaKit Python bindings
# $Id: all.py 1263 2007-03-09 16:51:19Z jcw $
# This is part of MetaKit, see http://www.equi4.com/metakit/

import sys
import os
import test.regrtest

def canonicalPath(path):
    """Do everything but resolve symbolic links to create an absolute path."""
    return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))

# from Python 2.2's regrtest module
def findtestdir():
    if __name__ == '__main__':
        file = sys.argv[0]
    else:
        file = __file__
    testdir = os.path.dirname(file) or os.curdir
    return testdir

testdir = canonicalPath(findtestdir())

# Don't run the standard Python tests, just run MetaKit tests
test.regrtest.STDTESTS = []
test.regrtest.NOTTESTS = []

# Take a look at the 
test.regrtest.main(testdir=testdir)
