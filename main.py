from tkinter import *
import pyperclip 
import secrets 
import string 

chars = string.digits + string.ascii_letters + string.punctuation 

class GUI:
    

    def __init__(self, master) -> None:

        self.generator(master)

    def generator(self, frame) -> None:

        password = Frame(frame, bd = 3, relief = RIDGE)

        password.grid(column = 0, row = 1, sticky = (E,W))
        Label(password, text = 'Password').pack(fill=BOTH)
        self.password_string = StringVar()
        Entry(password, textvariable = self.password_string, bg = 'white').pack(fill=BOTH)
        self.password_string.set("password")
        password.grid()
        
        generate_button = Button(password, text = "Generate", fg = "red", command = self.generate_password)
        generate_button.pack(fill=BOTH) #.grid(column = 1, row = 1, sticky = (W, E))
        
        copy_button = Button(password, text = "Copy", fg = "red", command = self.copy_password)
        copy_button.pack(fill=BOTH) #.grid(column = 1, row = 2, sticky = (W, E))


    def generate_password(self) -> str:
        
        var = "".join([secrets.choice(chars) for _ in range (40)])
        self.password_string.set(var)
        return var

    def copy_password(self) -> None:
        
        var = self.password_string.get()
        pyperclip.copy(var)
        

root = Tk()
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.title("Password Generator") 
root.geometry("520x100") 
gui = GUI(root)
root.resizable()
root.mainloop()