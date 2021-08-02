from tkinter import *
from PIL import ImageTk, Image #Fork of PIL (outdated)


gui=Tk()
gui.title('python tkinter tutorial')
gui.geometry("400x400")


checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
checkvar5 = IntVar()

chkbtn1 = Checkbutton(gui, text="Apply Crack", variable=checkvar1, onvalue = 1, offvalue = 0)
chkbtn2 = Checkbutton(gui, text="Create Uninstaller",variable=checkvar2, onvalue = 1, offvalue = 0)
chkbtn3 = Checkbutton(gui, text="Create Desktop Icon",variable=checkvar3, onvalue = 1, offvalue = 0)
chkbtn4 = Checkbutton(gui, text="Create Start Menu Icon",variable=checkvar4, onvalue = 1, offvalue = 0)
chkbtn5 = Checkbutton(gui, text="Pause Music",variable=checkvar5, onvalue = 1, offvalue = 0)

chkbtn1.grid(row=3, column=0, stick=W)
chkbtn2.grid(row=4, column=0, stick=W)
chkbtn3.grid(row=5, column=0, stick=W)
chkbtn4.grid(row=6, column=0, stick=W)
chkbtn5.grid(row=7, column=0, stick=W)




gui.mainloop()