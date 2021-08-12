import os
from pathlib import Path
from tkinter import *
import tkinter.messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def onClick():
    try :
        incorrect = int(entry_1.get())
        correct = int(entry_2.get())
        blank = int(entry_3.get())
    except :
        tkinter.messagebox.showerror("Invalid Data", "Please fill in all the boxes with numbers")
        return False
    calc = round(100*(correct-(incorrect/3))/(incorrect+correct+blank),2)
    Result = 'Your KonKur percentage is : '+str(calc)+'%'
    tkinter.messagebox.showinfo("Result", Result)

window = Tk()
window.geometry("850x504")
window.configure(bg = "#492F2F")
window.title('KonKur Percentage Application')
icon = PhotoImage(file = relative_to_assets("icon.png"))
window.iconphoto(False, icon)
canvas = Canvas(
    window,
    bg = "#492F2F",
    height = 504,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    425.0,
    252.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    542.0,
    353.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=452.0,
    y=341.0,
    width=180.0,
    height=23.0
)

canvas.create_rectangle(
    452.0,
    369.0,
    632.0,
    371.0,
    fill="#B7B8B7",
    outline="")

canvas.create_text(
    496.0,
    330.0,
    text="Incorrect tests",
    fill="#7C7B7B",
    font=("Marvel-Regular", int(12.0))
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png")
)
entry_bg_2 = canvas.create_image(
    491.0,
    298.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=401.0,
    y=286.0,
    width=180.0,
    height=23.0
)

canvas.create_rectangle(
    401.0,
    314.0,
    581.0,
    316.0,
    fill="#B7B8B7",
    outline="")

canvas.create_text(
    442.0,
    275.0,
    text="Correct tests",
    fill="#7C7B7B",
    font=("Marvel-Regular", int(12.0))
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png")
)
entry_bg_3 = canvas.create_image(
    436.0,
    243.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=346.0,
    y=231.0,
    width=180.0,
    height=23.0
)

canvas.create_rectangle(
    346.0,
    259.0,
    526.0,
    261.0,
    fill="#B7B8B7",
    outline="")

canvas.create_text(
    383.0,
    220.0,
    text="Blank tests",
    fill="#7C7B7B",
    font=("Marvel-Regular", int(12.0))
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=onClick,
    relief="flat"
)
button_1.place(
    x=651.0,
    y=261.0,
    width=153.0,
    height=69.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    78.0,
    60.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    137.0,
    101.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    453.0,
    133.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    745.0,
    458.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()