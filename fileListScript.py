#!/usr/bin/python3

import configparser
import os
import subprocess
import datetime
import shlex

# Instantiating the configparser to read the 'config.ini'

config = configparser.ConfigParser()
config.read('config.ini')

# Fetching the sections list and storing the name of the first section

sectionsList = config.sections()
dirsSection = sectionsList[0]

# Fetching preferences

prefsSection = sectionsList[1]
command = config[prefsSection]['command']
split_command = shlex.split(command)
date = datetime.datetime.now().strftime("%d_%b_%y_%a")

destination_path = config[prefsSection]['destination']

# Traversing the list of directories and printing the tree of each directory

for key in config[dirsSection]:
	directory_path = config[dirsSection][key]
	os.chdir(directory_path)

	returned_output = subprocess.check_output(split_command).decode('utf-8')

	directory_name = os.path.split(directory_path)[-1]
	filename = "{}_{}.txt".format(directory_name, date)
	destination_file_path = os.path.join(destination_path, filename)

	file = open(destination_file_path, mode='w', encoding='utf-8')
	print(returned_output, file=file)
	file.close()

	if os.path.exists(destination_file_path):
		print("Successfully generated tree for {}".format(directory_name))
