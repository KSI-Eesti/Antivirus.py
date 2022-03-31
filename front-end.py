import tkinter
from tkinter import *
from AV import *
from AV2 import *

mainapp = Tk()
mainapp.title('my antivirus program')
mainapp.minsize(640, 480)
mainapp.maxsize(1280, 960)
mainapp.sizefrom("user")

label_welcome = Label(mainapp, text="WELCOME!!!")
print(label_welcome.cget("text"))

button_scan = Button(mainapp, text = "Launch Smart Scan", width = 25, height = 4, command = scan)

button_deepscann = Button(mainapp, text = "Deep scan", width = 25, height = 4, command = deep_scan)

label_welcome.pack()
button_scan.pack()
button_deepscann.pack()
mainapp.mainloop()


