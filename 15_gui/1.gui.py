###################################Tkinter#########################################
# Python has a lot of GUI frameworks, 
# but Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. 
# It’s cross-platform, so the same code works on Windows, macOS, and Linux. 
# Visual elements are rendered using native operating system elements, so applications built with Tkinter look 
# like they belong on the platform where they’re run.
# Although Tkinter is considered the Python GUI framework, it’s not without criticism. 
# One notable criticism is that GUIs built with Tkinter look outdated. If you want a shiny, modern interface, 
# then Tkinter may not be what you’re looking for.
# However, Tkinter is lightweight and relatively painless to use compared to other frameworks. 
# This makes it a compelling choice for building GUI applications in Python, especially for applications where 
# a modern sheen is unnecessary, and the top priority is to quickly build something that’s functional and 
# cross-platform.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the Python GUI Tkinter module
from tkinter import *
import tkinter.messagebox as messagebox

# The class AppUI is based on the class Frame from Tkinter. This means the AppUI class is a type of Frame 
# but with some behaviors slightly different or customized. 
class AppUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        #A ways to add widgets to a window.
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.inputText = Entry(self)
        self.inputText.pack()
        self.alertButton = Button(self, text='Button', command=self.inputMsg)
        self.alertButton.pack()

    def inputMsg(self):
        name = self.inputText.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = AppUI()
app.master.title('Hello World')
# mainloop() tells Python to run the Tkinter event loop. 
# This method listens for events, such as button clicks or keypresses, and blocks any code that comes after
# it from running until you close the window where you called the method.
app.mainloop()

