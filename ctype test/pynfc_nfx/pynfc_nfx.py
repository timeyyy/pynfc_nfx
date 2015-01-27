
import ctypes
import os

from . import blank_module		# By importing any sub module i can get the location of this module, required by ctypes.CDLL
def mod_path(mod):
	return os.path.dirname(mod.__file__)
pkg_path = mod_path(blank_module)
build_path = os.path.join(pkg_path, 'build')
def test():
	try:
		#~ print(pkg_path)
		test = ctypes.CDLL(os.path.join(build_path, '_test.so'))
	except OSError:
		print("e1")
		#~ test = ctypes.CDLL('_test.so')
	else:
		test.ass()

