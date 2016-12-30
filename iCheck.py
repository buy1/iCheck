import re, argparse
import sys
import plistlib
from matplotlib import pyplot
import numpy as np

#creates a Dictionary where the key is the name of the track and the value is the song length
def createTrackDict(filePath):
	#instantiates
	file=open(filePath,"rb")
	plist=plistlib.load(file)
	#plist=plistlib.readPlist(file) #This is backwards compatible with Python 2.7.1
	tracks=plist['Tracks']
	trackDict={} #creates an empty dictionary to store the name of the tracks that are duplicates
	for id,track in tracks.items():
		trackName=track['Name']
		trackLength=track['Total Time']
		trackDict[trackName]=trackLength
	file.close()
	return trackDict

	#finds the same tracks between 2 playlists
def findDuplicate(file1Path, file2Path):
	dict1=createTrackDict(file1Path)
	dict2=createTrackDict(file2Path)
	duplicates={}
	for k1,v1 in dict1.items():
		for k2,v2 in dict2.items():
			if k1==k2 and (v2-v1)<5000: #Checks whether the names are the same and then whether each song is within 500ms of each other
				duplicates[k1]=v1
	return duplicates
#Does the same thing as findDuplicate except doesn't use as much memory
def findDuplicateFast(file1Path, file2Path):
	plist1=plistlib.load(open(file1Path,"rb"))
	plist2=plistlib.load(open(file2Path,"rb"))

	tracks1=plist1['Tracks']
	tracks2=plist2['Tracks']

	duplicates={}

	try:
		for id1,track1 in tracks1.items():
			name1=track1['Name']
			time1=track1['Total Time']
			for id2,track2 in tracks2.items():
				name2=track2['Name']
				time2=track2['Total Time']
				if name1==name2 and (time2-time1)<=5000:
					duplicates[name1]=time1
	except:
		pass
	return duplicates
def plot(filePath):
	plist=plistlib.load(open(filePath,"rb"))
	tracks=plist['Tracks']

	skipCount=[]
	time=[]

	for id,track in tracks.items():
		try:
			skipCount.append(track['Skip Count'])
			time.append(track['Total Time'])
		except:
			pass
	if skipCount==[] or time==[]:
		print("No valid skip counts or time") 
		return

	x=np.array(time,np.int32)/1000
	y=np.array(skipCount, np.int32)

	pyplot.subplot(2,1,1)
	pyplot.plot(x,y, 'o')
	pyplot.axis([0,1.05*np.max(x),-1,110])
	pyplot.xlabel('Track time in s')
	pyplot.ylabel('Number of Times Skipped')

	pyplot.subplot(2,1,2)
	pyplot.hist(x,bins=20)
	pyplot.xlabel('Track time in s')
	pyplot.ylabel('Number of Times Skipped')

	pyplot.show()
def main():
	path1="data/kanye.xml"
	path2="data/sleep.xml"
	path3="data/Library.xml"

	dict=findDuplicateFast(path1, path2)
	print (dict)

	plot(path3)
	
if __name__ == "__main__":
	main()		
