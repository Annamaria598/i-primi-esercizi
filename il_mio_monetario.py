class Portamonete:
    
    def __init__(self,capienza_max):
        self.lista_moneta= []
        self.capienza_max = capienza_max
        
    def insertMoneta(self):
      
  
        if len(self.lista_moneta) < len(self.capienza_max):
            self.lista_moneta.append(moneta)
            
       
            
        
    def removeMoneta (self):
        if n in lista_monete == moneta:
            moneta= lista_monete.pop(moneta)
        
            
    
    def countMoneta (self):
            print ( len(self.lista_monete)) 
            
    def countValori (self):
        somma = 0
        for n in self.lista_moneta:
            somma=somma + n.valore
        return somma
    
    def empty (self):
        self.lista_monete = []
            
class Monete:

    def __init__ (self,nome,valore):
        self.nome= nome
        self.valore=valore           
            
