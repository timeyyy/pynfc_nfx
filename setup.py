from setuptools import setup
from distutils.core import Extension
from distutils.command.build import build
import os
from subprocess import call
import shutil

class build_nxppy(build):
	def run(self):
		starting_dir = os.getcwd()
		src_dir = os.path.join(*(os.getcwd(),'pynfc_nfx', 'c_src','test'))
		build_dir = os.path.join(os.getcwd(),'pynfc_nfx', 'build')
		os.chdir(src_dir)

		def compile():
			call(["gcc -fpic test.c -O2 -c test.c"], shell=True )
			call(["gcc -shared test.o -o _test.so"], shell=True )
			#~ print(os.listdir(src_dir))
			shutil.copy(os.path.join(src_dir,'_test.so'), build_dir)
			os.remove(os.path.join(src_dir,'test.o',))
			os.remove(os.path.join(src_dir,'_test.so',))
		self.execute(compile, [], 'compiling Test')
		os.chdir( starting_dir )
		build.run(self)
		
short_description = 'A python extension for interfacing with the NXP PN512 NFC Reader. Targeted specifically for Raspberry Pi and the EXPLORE-NFC module'

setup (name = 'nxppy',
	   version = '1.2',
	   description = short_description, 
	   #~ long_description = long_description,
	   author = 'Scott Vitale',
	   #~ author_email = 'svvitale@gmail.com',
	   #~ url = 'http://github.com/svvitale/nxppy',
	   #~ test_suite = 'nose.collector',
	   #~ setup_requires=['nose>=1.0'],
	   #~ ext_modules = [nxppy],
	   cmdclass = {'build': build_nxppy})

