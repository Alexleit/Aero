from tkinter import *




#CRIANDO A JANELA

class app():
    
    #definindo a janela e seus gadgets
    def __init__(self):
        self.janela=Tk()
        self.janela.geometry("600x400")
        self.janela.title('GSDALT')
        
        self.frame= Frame(self.janela)
        self.frame.pack(side= LEFT)

        
            #campo foco
        self.lbfoco = Label(self.frame, text =  'Distância Focal(ex: 0.02)')
        self.lbfoco.grid( row = 0 , column = 1)
        self.efoco = Entry(self.frame)
        self.efoco.grid(row=1, column= 1)

            #campo GSD

        self.lbgsd = Label(self.frame, text =  'GSD (ex: 3.25')
        self.lbgsd.grid( row = 0 , column = 2)


        self.egsd = Entry(self.frame)
        self.egsd.grid(row=1, column= 2)

        
            #Campo Tamanho do Sensor

        self.lbsensor = Label(self.frame, text =  'Tamanho do Sensor (ex: 23.5x15.6 mm  --- X=23.5 Y=15.6')
        self.lbsensor.grid( row =8 , column = 1)

        
        self.lbsensorx = Label(self.frame, text =  'X')
        self.lbsensorx.grid( row = 10 , column = 1)
        self.esensorx = Entry(self.frame)
        self.esensorx.grid(row=12, column= 1)

        
        self.lbsensory = Label(self.frame, text =  'Y')
        self.lbsensory.grid( row = 10 , column = 2)
        self.esensory = Entry(self.frame)
        self.esensory.grid(row=12, column= 2)



        #Tamanho da Imagem

        self.lbimag = Label(self.frame, text =  'Tamanho da Imagem (ex: 6000x4000--- X=6000 Y=4000')
        self.lbimag.grid( row =16 , column = 1)

        
        self.lbimagx = Label(self.frame, text =  'X')
        self.lbimagx.grid( row = 18 , column = 1)
        self.eimagx = Entry(self.frame)
        self.eimagx.grid(row=20, column= 1)

        
        self.lbimagy = Label(self.frame, text =  'Y')
        self.lbimagy.grid( row = 18 , column = 2)
        self.eimagy = Entry(self.frame)
        self.eimagy.grid(row=20, column= 2)

        self.lbresult =  Label(self.frame, text =  'Preencha os campos acima')
        self.lbresult.grid(row=26, column= 1)


        #botão executável

        self.btresult = Button(self.frame, text="Calcular", command= self.calc_alt)
        self.btresult.grid(row= 26, column=3)

        


        self.janela.mainloop() 

        
        #Calcular resutados

    def calc_alt(self):
        
        
        try:
            gsd=float(self.egsd.get())
            foco=float(self.efoco.get())
            imagx=float(self.eimagx.get())
            sensorx=float(self.esensorx.get())
            tampix = sensorx/imagx
            denescala = gsd/tampix
            escala= 1/denescala
            alt=foco*escala
            
            self.lbresult["text"]= self.alt
            
        except ValueError:
            self.lbresult["text"]= "Reveja os valores inseridos"
        
                
        



        

        

app()