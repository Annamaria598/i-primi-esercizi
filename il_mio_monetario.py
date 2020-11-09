class Portamonete:
    
    def __init__(self,lista_monete,capienza_max):
        self.lista_moneta= []
        self.capienza_max = 8
        
    def insertMoneta(self):
        somma = 0
        if self.lista_moneta + moneta1 + moneta2 + moneta3 < 8:
            somma= somma + moneta1 + moneta2 + moneta3
        else:
            print ('Fermati!')
            
        
    def removeMoneta (self):
        differenza = self.lista_moneta - moneta1
        return (moneta1)
    
    def countMoneta (self):
        for n in self.lista_moneta:
            print ('il  numero di monete è '+ n) 
            
    def countValori (self):
        somma = 0
        for n in self.lista:
            somma=somma + n
        print ('la somma nel portamonete è'+ somma)
    
    def empty (self):
        svuota = self.lista[0]
        for n in self.lista:
            svuota= svuota - n
            
class Monete:

    def __init__ (self,nome,valore):
        self.nome= nome
        self.valore=valore           
            
