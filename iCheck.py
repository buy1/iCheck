import re, argparse
import sys
import plistlib
from matplotlib import pyplot
import numpy as np


#creates a Dictionary where the key is the name of the track and the value is the song length
def createTrackDict(filePath):
	#instantiates
	file=open(filePath,"rb")
	plist=plistlib.load(file,fmt=plistlib.FMT_XML,use_builtin_types=False,dict_type=dict)
	#plist=plistlib.readPlist(file) #This is backwards compatible with Python 2.7.1
	tracks=plist['Tracks']
	trackDict={} #creates an empty dictionary to store the name of the tracks that are duplicates
	for id,track in tracks.items():
		trackName=track['Name']
		trackLength=track['Total Time']
		trackDict[trackName]=trackLength
	return trackDict

	#finds the
def findDuplicates(file1Path, file2Path)
	dict1=createTrackDict(file1Path)
	dict2=createTrackDict(file2Path)
	for name
def main():


if __name__ == "__main__":
	main()		
