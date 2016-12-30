import sys
import plistlib

filePath="Focus.xml"
file=open(filePath,"rb")
plist=plistlib.load(file,fmt=plistlib.FMT_XML,use_builtin_types=False,dict_type=dict)
#plist=plistlib.readPlist(file) #This is backwards compatible with Python 2.7.1
tracks=plist['Tracks']
trackDict={} #creates an empty dictionary to store the name of the tracks that are duplicates
for id,track in tracks.items():
	trackName=track['Name']
	trackLength=track['Total Time']
	trackDict[trackName]=trackLength
print (trackDict)