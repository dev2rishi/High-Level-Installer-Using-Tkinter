from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image #Fork of PIL (outdated)
from tkinter import filedialog
from openal import *

gui=Tk()
gui.title('HLL Installer ©Dev Rishi')
gui.iconbitmap('MIGHTY.ico')
gui.geometry("512x610")

#Importing Image to the installer USING PIL and Pillow Library
img = ImageTk.PhotoImage(Image.open("xor.png"))
label = Label(image = img)
label.grid(row=0, column=0, columnspan=3)

#Playing Sound an OGG Opus file (with PyOgg)
source = oalOpen("xor.opus")

# Function for Prompt user to select a directory

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

folderPath = StringVar()

#creating input field
e = Entry(gui, fg="white", bg="black", width=55, textvariable=folderPath)
e.insert(0, "C:\WOWDOGE\MuchGames\ResidentEvilVillage")
e.grid(row=2, column=0, columnspan=3, pady=10)

#creating checkButtions
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
checkvar5 = IntVar()

chkbtn1 = Checkbutton(gui, text="Apply Crack",variable=checkvar1)
chkbtn2 = Checkbutton(gui, text="Create Uninstaller",variable=checkvar2)
chkbtn3 = Checkbutton(gui, text="Create Desktop Icon",variable=checkvar3)
chkbtn4 = Checkbutton(gui, text="Create Start Menu Icon",variable=checkvar4)
chkbtn5 = Checkbutton(gui, text="Play Music", variable=checkvar5, command=source.play, onvalue =1 , offvalue =0)

#displaying the checkButtons on to screen
chkbtn1.grid(row=3, column=0, stick=W)
chkbtn2.grid(row=4, column=0, stick=W)
chkbtn3.grid(row=5, column=0, stick=W)
chkbtn4.grid(row=6, column=0, stick=W)
chkbtn5.grid(row=7, column=0, stick=W)


# Progress bar widget
progress = ttk.Progressbar(gui, 
           orient = 'horizontal',
           length = 490, 
           mode = 'determinate')

def bar():
    import time,sys
    progress['value'] = 10
    gui.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 20
    gui.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 30
    gui.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 40
    gui.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 50
    gui.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

# place the progressbar
progress.grid(row=8, column=0, columnspan=3)


#creating buttons
ExitButton = Button(gui, text="EXIT" , fg="white", bg="red", padx=20 , pady=2 , command=gui.destroy)
InstallButton = Button(gui, text="INSTALL" , fg="white", bg="green", padx= 20 , pady=2, command = bar)
BrowseButton = Button(gui, text="Browse" , fg="white", bg="grey", command=getFolderPath)

ExitButton.grid(row=9, column=0,  padx=12,sticky=W)
InstallButton.grid(row=9, column=2, padx=22,sticky=E) #sticky is used to put widgets in desired direction (N,E,W,S)
BrowseButton.grid(row=2, column=2,padx=43, sticky=E)

#infinite loop
gui.mainloop()
