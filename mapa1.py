from tkinter import Tk, Toplevel, Label

class mapinha:
    def __init__(self):
        self.janela = Tk()  # Inicializa a janela principal

    def abrir_janela(self):
        self.janela2 = Toplevel(self.janela)
        self.janela2.title("Nova Janela")
        self.janela2.geometry("666x400")
        self.label2 = Label(text="MAPA")
        self.label2.grid(row=0,column=0)
        self.janela2.mainloop()

mapinha()