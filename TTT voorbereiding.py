from tkinter import *
from PIL import ImageTk, Image

filesize = Tk()

Invulveld = Entry(filesize)
Invulveld.grid(row=3, column=1)

def info ():
    Popup = Label(filesize, text=var.get())
    Popup.grid(row=1, column=1)

Knop = Button(filesize, text="Ga aan de slag", bg="red", fg="yellow", command=info)
Knop.grid(row=2, column=1)

var = StringVar()
Check = Checkbutton(filesize, text=".tif", variable=var, onvalue=".tif", offvalue="")
Check.grid(row=5, column=1)

filesize.title("dit is mijn eerste tool")
filesize.configure(bg="orange")
filesize.geometry("300x300")

CoGhentlogo = ImageTk.PhotoImage(Image.open(r"C:\Users\teugelso\Pictures\Logo_CollectievandeGentenaar2 (1).jpg"))

logolabel = Label(image=CoGhentlogo)
logolabel.grid(row=10, column=1)



filesize.mainloop()

