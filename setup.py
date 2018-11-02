from setuptools import setup
import os

def load(filename):
	return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
	name="mark2troff",
	version="0.1",
	description="Transpile markdown documents into troff documents.",
	long_description=load('README.txt'),
	classifiers=[
		"License :: OSI Approved :: isc",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Topic :: Text Processing",
	],
	keywords='regex structured regular expression',
	author='Parker Ellertson',
	author_email='pellertson@firemail.cc',
	url='https://github.com/rasputinmachine/mark2troff',
	license='ISC',
)