import sys
import plistlib
def createTrackDict(filePath):
	filePath="data/kanye.xml"
	file=open(filePath,"rb")
	plist=plistlib.load(file,fmt=plistlib.FMT_XML,use_builtin_types=False,dict_type=dict)
	#plist=plistlib.readPlist(filePath) #This is backwards compatible with Python 2.7
	tracks=plist['Tracks']
	trackDict={} #creates an empty dictionary to store the name of the tracks that are duplicates
	for id,track in tracks.items():
		try:
			info={}
			trackName=track['Name']
			trackLength=track['Total Time']
			timesPlayed=track['Play Count']
			info['Duration']=trackLength
			trackDict[trackName]=info
			info['Rating']=trackRating
		except:
			pass
	file.close()
	return trackDict
def findDuplicate(file1Path, file2Path):
	dict1=createTrackDict(file1Path)
	dict2=createTrackDict(file2Path)
	duplicates={}
	for k1,v1 in dict1.items():
		for k2,v2 in dict2.items():
			if k1==k2 and (v2-v1)<500: #Checks whether the names are the same and then whether each song is within 500ms of each other
				duplicates[k1]=v1
	return duplicates
def
def main():
	path1="data/kanye.xml"
	path2="data/sleep.xml"
	
	dict=findDuplicate(path1, path2)
	print (dict)
	
if __name__ == "__main__":
	main()		
