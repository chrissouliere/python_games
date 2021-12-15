from tkinter import *


class gui_name():

    def __init__(self, master):  # master is root, but using different master as variable name

        self.master = master
        master.title("Enter Names of Players")
        master.geometry("300x100")

        self.myLabel1 = Label(master, text="Player 1:")
        self.myLabel2 = Label(master, text="Player 2:")
        self.myEntry1 = Entry(master, bg="white")
        self.myEntry2 = Entry(master, bg="white")
        self.myButton = Button(master, text="Click Here to Set Names", command=self.info)

        self.myLabel1.grid(row=0, column=0)
        self.myLabel2.grid(row=1, column=0)
        self.myEntry1.grid(row=0, column=1)
        self.myEntry2.grid(row=1, column=1)
        self.myButton.grid(row=2, column=1)

    def info(self):
        self.players = []
        self.players.extend((self.myEntry1.get(), self.myEntry2.get()))
        return self.players

#root = Tk()
#my_gui = gui_name(root)
#root.mainloop()




