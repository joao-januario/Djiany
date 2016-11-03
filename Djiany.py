import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu
import tkinter.filedialog as tkfiledialog
import tkinter.messagebox as tkmessagebox


def new_command():
    textPad.delete('1.0','end')  #Deletes everything



def open_command():
    file = tkfiledialog.askopenfile(mode='r', title='Select a file') #Asks for a file to open and saves its contents to the file variable
    if file != None:
        textPad.insert('1.0',file.read()) #Writes everything read from file into the text area.
        file.close()

def save_command():
    file = tkfiledialog.asksaveasfile(mode='w')
    if file != None:
        data = textPad.get('1.0','end-1c') #Writes everything from the text area into the chosen file (except the last special character).
        file.write(data)
        file.close()

def exit_command():
    if tkmessagebox.askokcancel("Quit", "Do you really want to quit?"): # Closes the program if the user clicks ok
        root.destroy()

def about_command():
    label = tkmessagebox.showinfo("About","Vamos abrir o Djiany") # Information menu

root = tkinter.Tk(className="Djiany")
root.wm_title("Djiany")

textPad = ScrolledText(root, width=100, height=80) # creates the text area
textPad.pack()

menu=Menu(root) #adds menu to root
root.config(menu=menu)

filemenu= Menu(menu)  # Adds filemenu to the parent menu
menu.add_cascade(label="File",menu=filemenu) #Adds a label and a cascade menu to filemenu

#Adds some commands to the already existing cascade in filemenu
filemenu.add_command(label="New",command=new_command)
filemenu.add_command(label="Open",command=open_command)
filemenu.add_command(label="Save",command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_command)

helpmenu = Menu(menu) # Adds helpmenu to the parent menu
menu.add_cascade(label="Help",menu=helpmenu)  # adds a cascade menu to the helpmenu
helpmenu.add_command(label="About...",command=about_command) #adds the about command to the helpmenu

root.mainloop()


