from tkinter import *
import os, glob, re

master = Tk()
master.title(' ')


def info():
	manual = Toplevel()
	var = "Location\n   Accepts folder paths with and without quotation marks\n\nOld text\n   In order to change/remove brackets add backslash before them - \\(, \\), \\(\\)\n   E.g. to change (3) use \\(3\\)\n\nNew text\n   If this field is empty, string from 'Old text' field will be removed from file names\n\nScript can be used to change files extension\nIf the result file would have the same name as already existing one, script won't work"

	message_1 = Label(manual, text=var, justify=LEFT).grid()


def nameChange():

	if entry_2.get() == '()':
		info()
	oldtext = str(entry_2.get())
	newtext = str(entry_3.get())
	path = os.path.join(entry_1.get())
	path = path.strip('\"').strip('\'')

	name_map = {
    oldtext: newtext,
	}

	for root, dirs, files in os.walk(path):
	    for f in files:
	        for name in name_map.keys():
	            if re.search(name,f) != None:
	                new_name = re.sub(name,name_map[name],f)
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


master.columnconfigure(1, minsize=190, weight=1)
master.columnconfigure(2, weight=1)

button_0 = HoverButton(master, command=nameChange, activeforeground='grey40', text='File names change')
button_0.grid(row=0, sticky='w', columnspan=2)
button_1 = HoverButton(master, command=info, activeforeground='grey40', text='i')
button_1.grid(row=0, column=2, sticky='e')

label_1 = Label(master, text='Location')
label_1.grid(row=1, sticky='w')
entry_1 = Entry(master)
entry_1.grid(row=1, column=1, columnspan=2, sticky='we')

label_2 = Label(master, text='Old text')
label_2.grid(row=2, sticky='w')
entry_2 = Entry(master)
entry_2.grid(row=2, column=1, columnspan=2, sticky='we')

label_3 = Label(master, text='New text')
label_3.grid(row=3, sticky='w')
entry_3 = Entry(master)
entry_3.grid(row=3, column=1, columnspan=2, sticky='we')


master.minsize(260, 70)
master.mainloop()
