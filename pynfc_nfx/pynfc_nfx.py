'''
Wrapper for some c code provided by the manufacturers
'''

import ctypes
import os
import time

# By importing any sub module i can get the location of this module, required by ctypes.CDLL
# Dunno why but it wasn't finding it after being installed
from . import blank_module		
def mod_path(mod):
	return os.path.dirname(mod.__file__)
PKG_PATH = mod_path(blank_module)
BUILD_PATH = os.path.join(PKG_PATH, 'build')

NUM_TO_INTERFACE = {5:'felica'}

try:
	#~ print(BUILD_PATH)
	#~ self.test = ctypes.CDLL(os.path.join(BUILD_PATH, '_test.so'))
	clib_polling = ctypes.CDLL(os.path.join(BUILD_PATH, 'libcard_polling.so'))
except OSError as e:
	print('The c library could not be found!')
	raise e


def poll():
	while 1:
		index = clib_polling.setup()
		try:
			card = NUM_TO_INTERFACE[index]
			print(card,"back in python, do sth with the card now...")
		except KeyError:
			pass
		time.sleep(0.5)
def setup():
	index = clib_polling.setup()
	card = NUM_TO_INTERFACE[index]
	print(value,"back in python")
