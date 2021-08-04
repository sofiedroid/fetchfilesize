import os
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox


def openpad():
    pad = filedialog.askdirectory(title="Select directory!")
    toon_padnaam = Label(fetchfilesize, text="You chose this path: " + pad, bg="#fed2ed")
    toon_padnaam.grid(column=0, row=8, columnspan=4)
    return pad


def openfile():
    file = filedialog.askopenfile(title="Select file!")
    return file


def savefile():
    locatie = filedialog.askdirectory(title="Save File!")
    toon_locatie = Label(fetchfilesize, text="Your file can be found here: " + locatie, bg="#fed2ed")
    toon_locatie.grid(column=0, row=9, columnspan=4)
    return locatie


def start():
    column = ["filename", 'path', "filesize (MB)"]
    lijst = []
    totalsize = 0
    filetypes = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get()]
    while "" in filetypes:
        filetypes.remove("")
    messagebox.showinfo("You chose filetype(s): ", filetypes)

    for x, y, z in os.walk(openpad()):
        for a in z:
            if a.endswith(tuple(filetypes)):
                b = os.path.join(x, a)
                c = os.path.getsize(b)
                d = round(c / (1024 * 1024), 3)
                totalsize += d
                e = str(a) + '%£~' + str(b) + '%£~' + str(d)
                f = e.split('%£~')
                lijst.append(f)
    df = pd.DataFrame(lijst, columns=column)
    messagebox.showinfo("Choose location", "Please choose a location to store the result")
    df.to_excel(savefile() + "\output.xlsx")
    size = Label(fetchfilesize, text="The total size is: " + str(round(totalsize / 1024, 2)) + " GB", bg="#fed2ed")
    size.grid(row=10, column=0, columnspan=4)

    if len(lijst) > 0:
        averagesize = totalsize / len(lijst)
        average = Label(fetchfilesize, text="The average size is: " + str(round(averagesize, 2)) + " MB", bg="#fed2ed")
        average.grid(row=11, column=0, columnspan=4)
    else:
        average = Label(fetchfilesize, text='The average size is: 0.0 MB', bg="#fed2ed")
        average.grid(row=11, column=0, columnspan=4)


fetchfilesize = Tk()
fetchfilesize.title("fetch filesize")
fetchfilesize.configure(bg="#fed2ed")
fetchfilesize.geometry("900x550")

info = Label(fetchfilesize, text="Choose filetypes: ", bg="#fed2ed")
info.grid(column=0, row=1, columnspan=4)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()

checktif = Checkbutton(fetchfilesize, text=".tif", bg="#fed2ed", onvalue=".tif", offvalue="", variable=var1)
checkjpg = Checkbutton(fetchfilesize, text=".jpg", bg="#fed2ed", onvalue=".jpg", offvalue="", variable=var2)
checkwav = Checkbutton(fetchfilesize, text=".wav", bg="#fed2ed", onvalue=".wav", offvalue="", variable=var3)
checkmov = Checkbutton(fetchfilesize, text=".mov", bg="#fed2ed", onvalue=".mov", offvalue="", variable=var4)
checkmp3 = Checkbutton(fetchfilesize, text=".mp3", bg="#fed2ed", onvalue=".mp3", offvalue="", variable=var5)
checkmp4 = Checkbutton(fetchfilesize, text=".mp4", bg="#fed2ed", onvalue=".mp4", offvalue="", variable=var6)
checktiff = Checkbutton(fetchfilesize, text=".tiff", bg="#fed2ed", onvalue=".tiff", offvalue="", variable=var7)
checkJPG = Checkbutton(fetchfilesize, text=".JPG", bg="#fed2ed", onvalue=".JPG", offvalue="", variable=var8)

checktif.grid(row=4, column=0)
checkjpg.grid(row=4, column=1)
checkwav.grid(row=4, column=2)
checkmov.grid(row=4, column=3)
checkmp3.grid(row=5, column=0)
checkmp4.grid(row=5, column=1)
checktiff.grid(row=5, column=2)
checkJPG.grid(row=5, column=3)

buttonstart = Button(fetchfilesize, text="Choose a Directory!", padx=50, pady=10, borderwidth=10, bg="#fe37af",
                     command=start)
buttonstart.grid(row=7, column=0, columnspan=4)

fetchfilesize.mainloop()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
