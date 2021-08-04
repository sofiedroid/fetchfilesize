import os
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox


def openpad():
    pad = filedialog.askdirectory(title="Select directory!")
    toon_padnaam = Label(filesizefetcher, text="You chose this path: " + pad, bg="#ffdc00")
    toon_padnaam.grid(column=0, row=8, columnspan=4)
    return pad


def openfile():
    file = filedialog.askopenfile(title="Select file!")
    return file


def savefile():
    locatie = filedialog.askdirectory(title="Save File!")
    toon_locatie = Label(filesizefetcher, text="Your file can be found here: " + locatie, bg="#ffdc00")
    toon_locatie.grid(column=0, row=9, columnspan=4)
    return locatie


def start():
    column = ["filename", 'path', "filesize (MB)"]
    lijst = []

    for x, y, z in os.walk(openpad()):
        for a in z:
            b = os.path.join(x, a)
            c = os.path.getsize(b)
            d = round(c / (1024 * 1024), 3)
            e = str(a) + '%£~' + str(b) + '%£~' + str(d)
            f = e.split('%£~')
            lijst.append(f)
    df = pd.DataFrame(lijst, columns=column)
    messagebox.showinfo("Choose file", "Please open file with filenames (one column with header 'filename')")
    filenames = pd.read_csv(openfile())
    result = pd.merge(filenames, df, left_on='filename', right_on="filename", how='left')
    messagebox.showinfo("Choose location", "Please choose a location to store the result")
    result.to_excel(savefile() + r"\result.xlsx")


filesizefetcher = Tk()
filesizefetcher.title("filesizefetcher2.0")
filesizefetcher.configure(bg="#ffdc00")
filesizefetcher.geometry("580x580")


buttonstart = Button(filesizefetcher, text="Start!", padx=50, pady=10, borderwidth=10, bg="#fe37af",
                     command=start)
buttonstart.grid(row=7, column=0, columnspan=4)

filesizefetcher.mainloop()
