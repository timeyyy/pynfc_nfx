from setuptools import setup
from distutils.core import Extension
from distutils.command.build import build
import os
from subprocess import call
import shutil

class build_pynfc_nfx(build):
	def run(self):
		starting_dir = os.getcwd()
		src_dir = os.path.join(*(os.getcwd(),'pynfc_nfx', 'c_src','NxpRdLib_PublicRelease'))
		build_dir = os.path.join(os.getcwd(),'pynfc_nfx', 'build')
		os.chdir(src_dir)

		def compile():
			call('cmake .', shell=True )
            call('make', shell=True )
			#~ call(["gcc -fpic test.c -O2 -c test.c"], shell=True )
			#~ call(["gcc -shared test.o -o _test.so"], shell=True )
			#~ print(os.listdir(src_dir))
			#~ shutil.copy(os.path.join(src_dir,'_test.so'), build_dir)
			#~ os.remove(os.path.join(src_dir,'test.o',))
			#~ os.remove(os.path.join(src_dir,'_test.so',))
		self.execute(compile, [], 'compiling Test')
		os.chdir( starting_dir )
		build.run(self)
		
short_description = 'A python Interface for interfacing with the Raspberry Pi and the EXPLORE-NFC module'

setup (name = 'pynfc_nfx',
	   version = '1.0',
	   description = short_description, 
	   #~ long_description = long_description,
	   author = 'Timothy C Eichler',
	   author_email = 'timeyyy_da_man@hotmail.com',
	   url = 'https://github.com/timeyyy/pynfc_nfx',
	   cmdclass = {'build': build_pynfc_nfx})

