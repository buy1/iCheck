import sys
import plistlib

file=open("Focus.xml","rb")
plist=plistlib.load(file,fmt=plistlib.FMT_XML,use_builtin_types=False,dict_type=dict)
	#plist=plistlib.readPlist(file) #This is backwards compatible with Python 2.7.1
tracks=plist['Tracks']
trackNames={} #creates an empty dictionary to store the name of the tracks that are duplicates
for id,track in tracks.items(): 
	print (track['Name'])
	print (id)