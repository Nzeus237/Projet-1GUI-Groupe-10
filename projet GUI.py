#iportation des differentes biblioteques 
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter import colorchooser
from tkinter import simpledialog

#open frame

root=tk.Tk()
root.title("NOTE-IT")
root.geometry("940x600")

def mini_cal(a,b):
    pass

#fonction pour changer la police
def change_font():
    font_name=simpledialog.askstring("changer la police", "entrez le nom de la police:", initialvalue=my_text["font"].split()[0])
    if font_name:
        my_text.config(font=(font_name, my_text["font"].split()[1])) 

#change font size
def changer_police():
    size=simpledialog.askinteger("Changer la taillle de la police", "enterz la taille de la police:", initialvalue=my_text["font"].split()[1])
    if size:
        my_text.config(font=("Arial",size)) 

#open new file
def new_file():
    my_text.delete("1.0", "end")
    root.title('new File - TextPad!')
    status_bar.config(text="new file   ")


#open file
def open_file():
    my_text.delete("1.0", "end")


    text_file= filedialog.askopenfilename(initialdir="C:/projet GUI/", title="open file", filetypes=(("text files","*.txt"),("python Files", "*.py"),("html","*.html"),("all files", "*.")))
    name= text_file
    status_bar.config(text=f'{name}        ')
    name=name.replace("c:/projet GUI/","")
    root.title(f'{name} - TextPad!')

    text_file=open(text_file, 'r')
    stuff= text_file.read()

    my_text.insert("end", stuff)
    text_file.close()


#save file
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/projet GUI/", title="Save File", filetypes=(("text files", "*.txt"),("python Files", "*.py"),("html","*.html"),("all files", "*.")))
    if text_file:

        name=text_file
        status_bar.config(text=f'saved: {name}')
        name=name.replace(("c:/projet GUI/",""))
        root.title(f'{name} - TextPad!')

        text_file=open(text_file, 'w')
        text_file.write(my_text.get(1.0), "end")


#couleur de police
def change_color():
    color= colorchooser.askcolor(title="choisir une couleur")
    if color:
        my_text.config(fg=color[1])



my_frame=tk.Frame(root)
my_frame.pack(pady=5)

text_scroll=tk.Scrollbar(my_frame)
text_scroll.pack(side="right", fill="y")

#open text editor
my_text=tk.Text(my_frame, width=97, height=25, font=("Helvetica", 12), selectbackground="blue",selectforeground="black", undo=True, yscrollcommand=text_scroll)
my_text.pack()

#scroll barre
text_scroll.config(command=my_text.yview)

#set variable for open file name
global open_status_name
open_status_name=False

global selected
selected=False


#menu
my_menu=tk.Menu(root)
root.config(menu=my_menu)


#menu file
file_menu=tk.Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="new", command=new_file)
file_menu.add_command(label="open", command=open_file)
file_menu.add_command(label="save")
file_menu.add_command(label="save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="exit", command=root.quit)

#menu edit
edit_menu=tk.Menu(my_menu,tearoff=False )
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut   (Ctrl+x)", command=lambda: cut_text(False))
edit_menu.add_command(label="copy  (Ctrl+c)", command=lambda: copy_text(False))
edit_menu.add_command(label="paste (Ctrl+v)", command=lambda: paste_text(False))
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#menu option
options=tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="options", menu=options)
options.add_command(label="taille de police", command=changer_police)
options.add_command(label="couleur police", command=change_color)
options.add_command(label="font police", command=change_font)


#menu outils
outils=tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="outils", menu=outils)
outils.add_command(label='calculatrice', command=mini_cal)

#add Status Bar to bottom of App
status_bar=tk.Label(root, text='Ready        ', anchor="e")
status_bar.pack(fill="x", side="bottom", ipady=5)



#cut text
def cut_text(e):
    global selected

    if e:
        selected=root.clipboard_get()
    if my_text.selection_get():
        
        selected=my_text.selection_get()
        # delete selected text from text box
        my_text.delete("sel.first", "sel.last")

#copy text
def copy_text(e):
    global selected
    #check to see if we used keyboard shortcuts
    if e:
        selected=root.clipboard_get()

    if my_text.selection_get():
        #grab selected text from text box
        selected=my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


#paste text
def paste_text(e):
    global selected
    #check to see if keyboard shutcut  ussed
    if e:
         selected=root.clipboard_get()
    if selected:
       position=my_text.index('insert')
       my_text.insert(position, selected)





root.mainloop()
