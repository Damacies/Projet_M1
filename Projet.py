import tkinter as Tk
from tkinter.filedialog import *
import webbrowser
from programmes.main import main
import tkinter.filedialog
from PIL import Image

def Parcourir():
	fichier = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
	main(fichier,interface,var_label)
	bouton_afficher=Button(interface, command=Afficher, text="Afficher", bg="#e53737", activebackground="#ea7575", width="20", height="3", font=("bold",15),fg="#f1f1f1", relief="flat")
	bouton_afficher = bouton_afficher.pack()
	interface.update()

def Afficher():
	webbrowser.open("result_projet.html", new=0, autoraise=True)

def Enregistrer():
	sauvegarder = open("result_projet.html","r")
	fichier = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".html")
	fichier.write(sauvegarder.read())

interface = Tk()
interface.title("Projet de M1")
interface.geometry("450x450")
menubar = Menu(interface)

imgicon = PhotoImage(file=os.path.join('','dove.png'))
interface.tk.call('wm','iconphoto',interface._w,imgicon)

photo = PhotoImage(file="dove_3.png")

canvas = Canvas(interface,width=100, height=100)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

"""
p = PanedWindow(interface, orient=HORIZONTAL)
p.pack(side=TOP, expand=N, fill=BOTH, pady=20, padx=2)
p.add(canvas.pack())
p.add(Label(p, text='Projet de M1\nFreeDoM Tools\n2018-2019\n', background='white', anchor=CENTER,width=25) )
p.add(canvas.pack())
p.pack()
"""
menu1 = Menu(menubar, tearoff=0, font=("bold",10))
menu1.add_command(label="Sauvegarder", command=Enregistrer)
menu1.add_command(label="rien")
menu1.add_separator()
menu1.add_command(label="Quitter", command=interface.quit)
menubar.add_cascade(label="Fichier", menu=menu1)
interface.config(menu=menubar)

var_label = StringVar()

label = Label(interface, text="Projet de M1\nFreeDoM Tools\n2018-2019\n", font=("bold",10))
label.pack()

bouton=Button(interface, text="Parcourir",command = Parcourir, width="20", height="3",font=("bold",15),bg="#0d4fba", activebackground="#75b1ea", relief="flat")
bouton = bouton.pack()

label=Label(interface,textvariable=var_label, font=("bold",15), width="20", height="3").pack()
var_label.set(' ')

interface.mainloop()
