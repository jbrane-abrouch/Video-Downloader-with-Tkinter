
from pathlib import Path
from tkinter import filedialog
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.ttk import *
from pytube import YouTube
from tkinter import *
from tkinter import messagebox




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("770x520")
window.configure(bg = "#2A3278")
window.title("Youtube Video DownLoader")

canvas = Canvas(
    window,
    bg = "#2A3278",
    height = 513,
    width = 755,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    16.0,
    157.0,
    739.0,
    414.0,
    fill="#e6e7f5",
    outline="")

canvas.create_text(
    180.0,
    58.0,
    anchor="nw",
    text="Youtube Video Downloader",
    fill="#FFFFFF",
    font=("RedHatDisplay Regular", 30 * -1)
)

canvas.create_text(
    160.0,
    175.0,
    anchor="nw",
    text="Selectionner l'emplacement de stockage de la vidéo",
    fill="#000000",
    font=("RedHatDisplay Regular", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    471.0,
    231.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=305.0,
    y=215.0,
    width=332.0,
    height=30.0
)

def path():
    p = filedialog.askdirectory()
    entry_1.insert(END,p)
    return p

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: path(),
    relief="flat"
)
button_1.place(
    x=133.0,
    y=215.0,
    width=105.0,
    height=31.0
)

canvas.create_text(
    275.0, 
    273.0,
    anchor="nw",
    text="Coller le lien de la vidéo",
    fill="#000000",
    font=("RedHatDisplay Regular", 18 * -1)
)


def take():
    INPUT = entry_2.get()
    if(INPUT !=''):
       go(INPUT)
    else:
     print("Wrong answer")






button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: take(),
    relief="flat"
)
button_2.place(
    x=300.0,
    y=357.0,
    width=154.0,
    height=37.0
)







def go(i):
    newWindow = Toplevel(window)
    newWindow.title("Télécharger")
 
    newWindow.geometry("300x300")
    my_video=YouTube(i)

    def sel():
        selection = var.get()
        if(selection==1):
          return "240p"
        elif(selection==2):
           return "360p"
        elif(selection==3):
           return "480p"
        elif(selection==4):
           return "720p"
        else:
           return "1080p"



    var = IntVar()
    R1 = Radiobutton(newWindow, text="240p", variable=var, value=1,
                  command=sel)


    R2 = Radiobutton(newWindow, text="360p", variable=var, value=2,
                  command=sel)


    R3 = Radiobutton(newWindow, text="520p", variable=var, value=3,
                  command=sel)

    R4 = Radiobutton(newWindow, text="720p", variable=var, value=4,
                  command=sel)

    R5 = Radiobutton(newWindow, text="1080p", variable=var, value=5,
                  command=sel)
    

    lbl1 = Label(newWindow, text="Le nom de la vidéo est :").pack()
    Output = Text(newWindow, height = 3,
			width = 100,
			bg = "light yellow")
    print("*********************Video Title************************")
    #get Video Title
    print(my_video.title)
    Output.insert(END,my_video.title)
    Output.pack()


    Label(newWindow,text ="Choisissez la résolution de la vidéo").pack()
    
    print(my_video.title)

    R1.pack( anchor = W )
    R2.pack( anchor = W )
    R3.pack( anchor = W)
    R4.pack( anchor = W)
    R5.pack( anchor = W)
    dow = Button(newWindow,
				text ="Téléchager",
				command = lambda:dw(my_video))
    dow.pack()
    
    def dw(my_video):
        tt=entry_1.get()
        my_video.streams.filter(res=sel()).first().download(tt)
        messagebox.showwarning("Downloaded", "téléchargement terminé")
    
    
    




















entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    377.0,
    327.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_2.place(
    x=176.0,
    y=310.0,
    width=402.0,
    height=32.0
)

canvas.create_text(
    560.0,
    500.0,
    anchor="nw",
    text="Developper par jbrane abrouch",
    fill="#6A80A1",
    font=("Roboto", 12 * -1)
)
window.resizable(TRUE, TRUE)
window.mainloop()
