import tkinter as tk
import tkinter.font as tkFont



class App:
    def __init__(self, root):
        #setting title
        root.title("hesap makinesi-zeysu")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_191=tk.Button(root)
        GButton_191["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_191["font"] = ft
        GButton_191["fg"] = "#000000"
        GButton_191["justify"] = "center"
        GButton_191["text"] = "Button"
        GButton_191.place(x=70,y=380,width=70,height=25)
        GButton_191["command"] = self.GButton_191_command

        GButton_508=tk.Button(root)
        GButton_508["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_508["font"] = ft
        GButton_508["fg"] = "#000000"
        GButton_508["justify"] = "center"
        GButton_508["text"] = "Button"
        GButton_508.place(x=200,y=380,width=70,height=25)
        GButton_508["command"] = self.GButton_508_command

        GButton_202=tk.Button(root)
        GButton_202["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_202["font"] = ft
        GButton_202["fg"] = "#000000"
        GButton_202["justify"] = "center"
        GButton_202["text"] = "Button"
        GButton_202.place(x=350,y=380,width=70,height=25)
        GButton_202["command"] = self.GButton_202_command

        GButton_647=tk.Button(root)
        GButton_647["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_647["font"] = ft
        GButton_647["fg"] = "#000000"
        GButton_647["justify"] = "center"
        GButton_647["text"] = "Button"
        GButton_647.place(x=500,y=380,width=70,height=25)
        GButton_647["command"] = self.GButton_647_command

        GLineEdit_290=tk.Entry(root)
        GLineEdit_290["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_290["font"] = ft
        GLineEdit_290["fg"] = "#333333"
        GLineEdit_290["justify"] = "center"
        GLineEdit_290["text"] = "Entry"
        GLineEdit_290.place(x=90,y=440,width=70,height=25)

        GLineEdit_724=tk.Entry(root)
        GLineEdit_724["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_724["font"] = ft
        GLineEdit_724["fg"] = "#333333"
        GLineEdit_724["justify"] = "center"
        GLineEdit_724["text"] = "Entry"
        GLineEdit_724.place(x=360,y=450,width=70,height=25)

    def GButton_191_command(self):
        print("Buton 1e basildi")


    def GButton_508_command(self):
        print("Buton 2ye basildi")


    def GButton_202_command(self):
        print("Buton 3e basildi")


    def GButton_647_command(self):
        print("Buton 4e basildi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    #buraya aşağıdakileri ekledim
    textBoxYazilanlar1=tk.StringVar()#degişken tanimlama
    textBoxYazilanlar2=tk.StringVar()#degişken tanimlama
    textBoxYazilanlar3=tk.StringVar()#degişken tanimlama

    root.mainloop()
