# tkinter or toolkit interface is a library to create Graphic User Interface.
# Without it, also there have two modules, which is wxPython (Highly functional user interface)
# and JPython (A java implementation of Python).
from tkinter import *

# Module tkinter.ttk is accessed by tk, introduce in tk 8.5
# The different between tkinter and tkinter.ttk is, tkinter widgets is more configurable and ttk is a
# little bit modern and configurable with style. tkinter.ttk is more handy to use.
from tkinter.ttk import *

# If you want to set a time or calender, the time module is the best module for python language.
# strftime is a function of time module, which is represent a time.
from time import strftime

# Using the Tk function, which is define a main windows of an application. I just put this function to a variable.
root = Tk()

# Using title function we just define the name of the main windows.
root.title('Digital Clock')
# label is a widget, where you place text, image and more attribute of design. This function is divided into two part.
# One is master, represent the parent window. And another one is option, such as font, background, foreground, height,
# weight etc. All of option are separated by comma. peck() function is a geometry manager, which is the widget position.
# Here we use fill option and assign a X value. it's mean fill horizontally. We could use Y (fill vertically) or both.
# Also there has a 'None' (Default) variable. Even 'expand' and 'side' another two option, which I could use.
label = Label(root, anchor='center', font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(fill=X)


# Let have a define a function, name is time. Here, strftime() function return 4 parameter taken from local time.
# %H:%M:%S return Hours:Minutes:Second and %p mean local equivalent of either AM or PM. Using the config() function
# we are changing the text. The function is use to call the function (time) after given specific delay in millisecond.
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# Call the function, which I have created.
time()
# The mainloop() function is used to keep run the application, wait for an event occur as long as the windows is close.
mainloop()
