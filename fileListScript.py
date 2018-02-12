#!/usr/bin/python3

import configparser
import os
import subprocess
import datetime

# Instantiating the configparser to read the 'config.ini'

config = configparser.ConfigParser()
config.read('config.ini')

# Fetching the sections list and storing the name of the first section

sectionsList = config.sections()
dirsSection = sectionsList[0]

# Traversing the list of directories and printing the tree of each directory

for key in config[dirsSection]:
	dir = config[dirsSection][key]
	os.chdir(dir)

	cmd = ['tree','-alpuhD','--du']
	returned_output = subprocess.check_output(cmd).decode('utf-8')

	date = datetime.datetime.now().strftime("%d_%b_%y_%a")

	filename = "{}_{}.txt".format(key, date)
	print("Filename: " + filename)

	file = open(filename, mode='w', encoding='utf-8')
	print(returned_output, file=file)
	file.close()
