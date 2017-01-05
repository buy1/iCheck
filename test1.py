from tkinter import *
import re, argparse
import sys
import plistlib
import numpy as np

class iCheck(Frame):
	path1=""
	path2=""
	path3=""

	def __init__(self, master=None): #
		Frame.__init__(self,master)
		self.master=master
		self.init_iCheck()

	def init_iCheck(self):
		self.master.title("GUI") #sets the title to GUI
		self.pack(fill=BOTH, expand=1) #puts itself into the frame

		menu = Menu(self.master) # makes 
		self.master.config(menu=menu)

		file = Menu(menu) #Makes a menu called menu
		file.add_command(label="Exit",command=self.client_exit) #adds the exit command to the menu
		menu.add_cascade(label="File",menu=file)#makes a topbar item called File and gives it the cascade option

		edit = Menu(menu)
		edit.add_command(label="Undo")
		menu.add_cascade(label="Edit",menu=edit)#Does the same as above except the menu item is called Edit

		browseButton1 = Button(self, text="Browse",command=self.browseButton1)
		browseButton1.grid(row=3, column=3)

		browseButton2=Button(self,text="Browse",command=self.browseButton2)
		browseButton2.grid(row=3,column=6)

		compareButton=Button(self,text="Compare",command=self.compareButton)
		compareButton.grid(row=5,column=3)

		browseButton3=Button(self,text="Browse",command=self.browseButton3)
		browseButton3.grid(row=8,column=3)

		plotButton=Button(self,text="Plot",command=self.plotButton)
		plotButton.grid(row=8,column=6)

	def browseButton1(self):
		from tkinter import filedialog

		file=filedialog.askopenfile(mode='rb',title='Choose a file')
		self.path1=file.name

	def browseButton2(self):
		from tkinter import filedialog

		file=filedialog.askopenfile(mode='rb',title='Choose a file')
		self.path2=file.name

	def compareButton(self):
		if self.path1 != "" and self.path2 != "":
			print (iCheck.findDuplicateFast(self.path1,self.path2))
		else:
			print ("Error: Missing path")

	def browseButton3(self):
		from tkinter import filedialog

		file=filedialog.askopenfile(mode='rb',title='Choose a file')
		self.path3=file.name

	def plotButton(self):
		if self.path3 != "":
			iCheck.plot(self.path3)
		else:
			print ("Error: Missing path")

	def client_exit(self):
		exit()
#======================================================================================
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
		import matplotlib
		matplotlib.use("TkAgg")
		from matplotlib import pyplot

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
#==============================================
def main():
	root=Tk()
	root.geometry("400x300")
	app=iCheck(root)
	root.mainloop()
if __name__ == "__main__":
	main()	