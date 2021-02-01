from tkinter import *
import os, glob, re

master = Tk()
master.title('Filenames changer')


def info():
	manual = Toplevel()
	var = "\n   1. By default only text before the file extension is affected\n      To change that use checkboxes at the bottom\n      'extensions' checkbox - only file extensions will be affected\n   2. Folder paths with and without quotation marks are accepted\n   3. In order to change/remove brackets add backslash before them - \\(, \\), \\(\\)\n   4. If 'New text' is empty, string from 'Old text' will be removed\n   5. If the result file would have the same name as already existing one, script won't work   \n"

	message_1 = Label(manual, text=var, justify=LEFT).grid()


def nameChange():

	if entry_2.get() == '()':
		info()
	oldtext = str(entry_2.get())
	newtext = str(entry_3.get())
	path = os.path.join(entry_1.get())
	path = path.strip('\"').strip('\'')

	name_map = {oldtext: newtext}

	if var1.get() ==1: # only extensions are affected
		for root, dirs, files in os.walk(path):
		    for f in files:
		        for name in name_map.keys():
		        	tmp = f.rsplit(".", 1)
		        	tmp_name = tmp[1]
		        if re.search(name,tmp_name) != None:
		            new_name = tmp[0] + "." + re.sub(name,name_map[name],tmp_name)
		            try:
		                os.rename(os.path.join(root,f), os.path.join(root, new_name))
		            except OSError:
		                print ("No such file or directory!")
	elif var2.get() ==1: # full filenames are affected                
		for root, dirs, files in os.walk(path):
		    for f in files:
		        for name in name_map.keys():
		            if re.search(name,f) != None:
		                new_name = re.sub(name,name_map[name],f)
		                try:
		                    os.rename(os.path.join(root,f), os.path.join(root, new_name))
		                except OSError:
		                    print ("No such file or directory!")
	else: # default, text before the last fullstop is affected
		for root, dirs, files in os.walk(path):
		    for f in files:
		        for name in name_map.keys():
		        	tmp = f.rsplit(".", 1)
		        	tmp_name = tmp[0]
		        if re.search(name,tmp_name) != None:
		            new_name = re.sub(name,name_map[name],tmp_name) + "." + tmp[1]
		            try:
		                os.rename(os.path.join(root,f), os.path.join(root, new_name))
		            except OSError:
		                print ("No such file or directory!")


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, bd=0, cursor="hand2", **kw)
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['foreground'] = self.defaultForeground


def checkboxes_1():
	if var2.get() == 1:
		var2.set(0)

def checkboxes_2():
	if var1.get() == 1:
		var1.set(0)


master.columnconfigure(1, minsize=190, weight=1)
master.columnconfigure(2, weight=1)


button_0 = HoverButton(master, command=info, activeforeground='grey40', text='info')
button_0.grid(row=0, column=2, sticky='e')

frame_right = Frame(master, width=5)
frame_right.grid(row=0, column=3)

label_1 = Label(master, text=' Location ')
label_1.grid(row=1, sticky='w')
entry_1 = Entry(master)
entry_1.grid(row=1, column=1, columnspan=2, sticky='we')

label_2 = Label(master, text=' Old text ')
label_2.grid(row=2, sticky='w')
entry_2 = Entry(master)
entry_2.grid(row=2, column=1, columnspan=2, sticky='we')

label_3 = Label(master, text=' New text ')
label_3.grid(row=3, sticky='w')
entry_3 = Entry(master)
entry_3.grid(row=3, column=1, columnspan=2, sticky='we')

button_1 = HoverButton(master, command=nameChange, borderwidth=1, activeforeground='grey40', text='Change')
button_1.grid(row=4, column=1)

var1 = IntVar()
var2 = IntVar()
c_0 = Checkbutton(master, text='extensions', variable=var1, onvalue=1, offvalue=0, command=checkboxes_1)
c_0.grid(row=5, column=1, sticky='w')
c_1 = Checkbutton(master, text='full name', variable=var2, onvalue=1, offvalue=0, command=checkboxes_2)
c_1.grid(row=5, column=1, sticky='e')

frame_bottom = Frame(master, height=4)
frame_bottom.grid(row=6)

master.minsize(300, 138)
master.mainloop()
