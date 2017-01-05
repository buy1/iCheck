from tkinter import *

class iCheck(Frame):
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

		browseButton = Button(self, text="Browse")
		browseButton.grid(row=3, column=3)


	def client_exit(self):
		exit()
root=Tk()
root.geometry("400x300")
app=iCheck(root)
root.mainloop()