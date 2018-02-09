#!/usr/bin/python3

import configparser
import os
import subprocess

# Instantiating the configparser to read the 'config.ini'

config = configparser.ConfigParser()
config.read('config.ini')

# Fetching the sections list and storing the name of the first section

sectionsList = config.sections()
dirsSection = sectionsList[0]
print(sectionsList)
print(dirsSection)

# Traversing the list of directories and printing the tree of each directory

for key in config[dirsSection]:
	print(key)
	dir = config[dirsSection][key]
	print(dir)
	os.chdir(dir)
	print(os.getcwd())

	cmd = ['tree','-alpuhD','--du']
	returned_output = subprocess.check_output(cmd).decode('utf-8')

	filename = "tree.txt"
	file = open(filename, mode='w', encoding='utf-8')
	print(returned_output, file=file)
	file.close()
