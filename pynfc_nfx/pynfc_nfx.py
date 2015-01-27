
import ctypes
import os

# By importing any sub module i can get the location of this module, required by ctypes.CDLL
# Dunno why but it wasn't finding it after being installed
from . import blank_module		
def mod_path(mod):
	return os.path.dirname(mod.__file__)
PKG_PATH = mod_path(blank_module)
BUILD_PATH = os.path.join(PKG_PATH, 'build')

'''
Wrapper for some c code provided by the manufacturers
'''

try:
	#~ print(BUILD_PATH)
	#~ self.test = ctypes.CDLL(os.path.join(BUILD_PATH, '_test.so'))
	clib_polling = ctypes.CDLL(os.path.join(BUILD_PATH, 'libcard_polling.so'))
except OSError as e:
	print('The c library could not be found!')
	raise e


def poll():
	value = clib_polling.poll()
	print(value,"back in python")
	
def setup():
	value = clib_polling.setup()
	print(value,"back in python")
