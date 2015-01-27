
import ctypes
import os

from . import blank_module		# By importing any sub module i can get the location of this module, required by ctypes.CDLL
def mod_path(mod):
	return os.path.dirname(mod.__file__)
PKG_PATH = mod_path(blank_module)
BUILD_PATH = os.path.join(PKG_PATH, 'build')

class pynfc_nfx():
	# This is what the user of the Api Interacts with
	'''
Wrapper for some c code provided by the manufacturers
	'''
	
	def __init__(self):
		try:
			self.test = ctypes.CDLL(os.path.join(BUILD_PATH, '_test.so'))
		except OSError as e:
			print('The c library could not be found!')
			
	def ass(self):
		self.test.ass()
