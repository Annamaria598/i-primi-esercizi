class Portamonete:
    
    def __init__(self,capienza_max):
        self.lista_moneta= []
        self.capienza_max = capienza_max
        
    def insertMoneta(self):
      
  
        if len(self.lista_moneta) < len(self.capienza_max):
            self.lista_moneta.append(moneta)
            
       
            
        
    def removeMoneta (self):
        if n in len (self.lista_moneta) == moneta:
            moneta= lista_moneta.pop(moneta)
            return moneta
        
            
    
    def countMoneta (self):
           return ( len(self.lista_moneta)) 
            
    def countValori (self):
        somma = 0
        for n in self.lista_moneta:
            somma=somma + n.valore
        return somma
    
    def empty (self):
        self.lista_moneta = []
            
class Monete:

    def __init__ (self,nome,valore):
        self.nome= nome
        self.valore=valore           
            
