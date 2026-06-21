import tkinter as tk #import tkinter library as tk
root = tk.Tk() #Create a main window
root.title("MY first GUI") #Set the Window Title
label=tk.Label(root,text="Hello,World..!") 
'''Creates a label (a piece of text displayed on the screen).
root means the label belongs inside the main window.
text="Hello,World..!" is the text displayed.'''

label.pack() # Display the label
root.mainloop()#Start the event loop. 