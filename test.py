from tkinter import *

class Window(Frame):
	def __init__(self, master=None): #
		Frame.__init__(self,master)
		self.master=master
		self.init_window()

	def init_window(self):
		self.master.title("GUI") #sets the title to GUI
		self.pack(fill=BOTH, expand=1) #puts itself into the frame
		#quitButton = Button(self, text="Quit", command=self.client_exit)
		#quitButton.place(x=0,y=0)

		menu = Menu(self.master) # makes 
		self.master.config(menu=menu)

		file=Menu(menu) #Makes a menu called menu
		file.add_command(label="Exit",command=self.client_exit) #adds the exit command to the menu
		menu.add_cascade(label="File",menu=file)#makes a topbar item called File and gives it the cascade option

		edit = Menu(menu)
		file.add_command(label="Undo")
		menu.add_cascade(label="Edit",menu=file)#Does the same as above except the menu item is called Edit


	def client_exit(self):
		exit()
root=Tk()
root.geometry("400x300")
app=Window(root)
root.mainloop()