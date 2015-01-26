'''
This setup.py file handles the compiling of the c modules and turns them into the python modules
as the c code must be compiled it is different depending on the system and has to be done by the
user.

http://www.swig.org/Doc1.3/Python.html#Python_nn6

'''

from setuptools import setup
from distutils.core import Extension
from distutils.command.build import build
import os
from subprocess import call
import multiprocessing

class build_polling(build):
	def run(self):
		startingDir = os.getcwd()
		os.chdir( os.path.join('NxpRdLib_PublicRelease', 'build') )
		def compile():
			call( 'cmake .', shell=True )
			call( 'make', shell=True )

		self.execute(compile, [], 'compiling NxpRdLib')
		os.chdir( startingDir )
		# Run the rest of the build
		build.run(self)

polling = Extension('polling',
					sources = ['polling.c'],
					include_dirs = ['NxpRdLib_PublicRelease/types', 'NxpRdLib_PublicRelease/intfs', 'NxpRdLib_PublicRelease/comps/phpalSli15693/src/Sw'],
					extra_compile_args=['-O1'],
					extra_link_args=['NxpRdLib_PublicRelease/build/libnxprd.a'])

short_description = 'Python interface for the nfx_explore nfc board for the rasperry pi '

'''
setup (name = 'pynfc_nfx',
	   version = '1.0',
	   description = short_description, 
	   #~ long_description = long_description,
	   author = 'Timothy Eichler',
	   author_email = 'tim_eichler@hotmail.com',
	   url = 'https://github.com/timeyyy/pynfc_nfx',
	   #~ test_suite = 'nose.collector',
	   #~ setup_requires=['nose>=1.0'],
	   #~ ext_modules = [nxppy],
	   

	   ext_modules = [polling],
	   py_modules = ["example"],
	   )
'''
if __name__ == '__main__':
	
	example_module = Extension('_example',
							   sources=['example_wrap.c', 'example.c'],
							   )
	setup (name = 'pynfc_nfx',
		   version = '0.1',
		   author      = "Timothy C Eichler",
		   description = short_description,
           cmdclass = {'build': build_polling},
		   ext_modules = [polling],
		   py_modules = ["example"],
		
		)
