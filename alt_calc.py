from tkinter import (Tk, Frame, Button, Label, Entry)
from mapa1 import mapinha  # Importa a classe mapinha do arquivo mapa1.py

# CRIANDO A JANELA
class app:
    # Definindo a janela e seus gadgets
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("600x400")
        self.janela.title('GSDALT')

        self.frame = Frame(self.janela)
        self.frame.pack(side='left')

        self.cabec = Label(self.frame, text='PARÂMETROS ÓPTICOS E DE IMAGEM', bg='#fff', fg='#f00', pady=0, padx=0, font=10)
        self.cabec.grid(row=0, column=1)

        # Campo foco
        self.lbfoco = Label(self.frame, text='Distância Focal(ex: 0.02)')
        self.lbfoco.grid(row=2, column=1)
        self.efoco = Entry(self.frame)
        self.efoco.grid(row=3, column=1)

        # Campo GSD
        self.lbgsd = Label(self.frame, text='GSD (ex: 3.25)')
        self.lbgsd.grid(row=2, column=2)
        self.egsd = Entry(self.frame)
        self.egsd.grid(row=3, column=2)

        # Campo Tamanho do Sensor
        self.lbsensor = Label(self.frame, text='Tamanho do Sensor (ex: 23.5x15.6 mm  --- X=23.5 Y=15.6')
        self.lbsensor.grid(row=8, column=1)

        self.lbsensorx = Label(self.frame, text='X')
        self.lbsensorx.grid(row=10, column=1)
        self.esensorx = Entry(self.frame)
        self.esensorx.grid(row=12, column=1)

        self.lbsensory = Label(self.frame, text='Y')
        self.lbsensory.grid(row=10, column=2)
        self.esensory = Entry(self.frame)
        self.esensory.grid(row=12, column=2)

        # Tamanho da Imagem
        self.lbimag = Label(self.frame, text='Tamanho da Imagem (ex: 6000x4000--- X=6000 Y=4000')
        self.lbimag.grid(row=16, column=1)

        self.lbimagx = Label(self.frame, text='X')
        self.lbimagx.grid(row=18, column=1)
        self.eimagx = Entry(self.frame)
        self.eimagx.grid(row=20, column=1)

        self.lbimagy = Label(self.frame, text='Y')
        self.lbimagy.grid(row=18, column=2)
        self.eimagy = Entry(self.frame)
        self.eimagy.grid(row=20, column=2)

        # Resultados
        self.lbresult = Label(self.frame, text='Preencha os campos acima')
        self.lbresult.grid(row=30, column=1)

        self.lbsuperf = Label(self.frame, text='')
        self.lbsuperf.grid(row=32, column=1)

        # Botão executável
        self.btresult = Button(self.frame, text="Calcular", command=self.calc_alt)
        self.btresult.grid(row=26, column=3)

        # Cria uma instância da classe mapinha
        self.mapa_instancia = mapinha()

        # Cria o botão e associa o comando à função abrir_janela da instância de mapinha
        self.map = Button(self.frame, text="Mapa", command=self.mapa_instancia.abrir_janela)
        self.map.grid(row=30, column=3)

        self.janela.mainloop()

    # Calcular resultados
    def calc_alt(self):
        try:
            gsd = float(self.egsd.get())
            gsd_mm = gsd * 10
            foco = float(self.efoco.get())
            foco_mm = foco * (10 ** (-3))
            imagx = float(self.eimagx.get())
            imagy = float(self.eimagy.get())
            sensorx = float(self.esensorx.get())
            tampix = sensorx / imagx
            denescala = gsd_mm / tampix
            alt = int((foco_mm) * denescala)
            largura = int((gsd * imagx) / 100)
            comprimento = int((gsd * imagy) / 100)
            area = largura * comprimento
            text_alt = f"""A Altitude Máxima para voo deve ser de {alt} metros.
            A superfície imageada a esta altura de voo possui {largura} m de largura 
            e cerca de {comprimento} m de comprimento, perfazendo uma área de {area} m²."""

            self.lbresult["text"] = text_alt
        except ValueError:
            self.lbresult["text"] = "Reveja os valores inseridos"

if __name__ == "__main__":
    app()
