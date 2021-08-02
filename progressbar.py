# importing tkinter module
from tkinter import * 
from tkinter.ttk import *
from tkinter.messagebox import showinfo

# creating tkinter window
root = Tk()
root.geometry("400x400")

# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def update_progress_label():
    return f"Current Progress: {progress['value']}%"


def progress():
    if progress['value'] &lt; 100:
        progress['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='Installation Complete!')


def stop():
    progress.stop()
    value_label['text'] = update_progress_label()

 #place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# start button
start_button = ttk.Button(
    root,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


root.mainloop()