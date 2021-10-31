from setuptools import setup, Extension, find_packages

requirements_noversion = [
	'requests',
	'beautifulsoup4',
	'feedparser',
	'pandas',
	'selenium',
	'scapy'
]
setup(
	# Meta information
	name				= 'atrow',
	version				= '0.0.1',
	author				= 'Supratik Chatterjee',
	author_email		= 'supratikdevm96@gmail.com',
	# license			= '2-clause BSD',
	url					= 'https://github.com/supratikchatterjee16/',
	description			= 'Automated tool for reporting on metrics for websites',
	keywords			= ['automated', 'testing', 'websites', 'scraping', 'crawling', 'summary', 'tool'],
	install_requires	= requirements_noversion,
	# build information
	py_modules			= ['atrow'],
	packages			= find_packages(),
	package_dir			= {'atrow' : './atrow'},
	include_package_data= True,
	# package_data		= {'workbench' : [
	# 							'frontend/*',
	# 							'frontend/*/*',
	# 							'frontend/*/*/*',
	# 							'frontend/*/*/*/*',
	# 							'frontend/*/*/*/*/*',
	# 							'frontend/*/*/*/*/*/*',
	# 							]},
	zip_safe			= True,
	# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
	entry_points		= {'console_scripts' : ['atrow = atrow:run'],},
	# ext_modules			= [bjoern_extension],
	classifiers			= [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
