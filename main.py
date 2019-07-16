class Fila(object): #Clase base de fila
    def __init__(self): #constructor de la clase Fila
        self.enfila=0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=1
        self.fila.append(cliente.dni)
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)

    def abrircajanueva(self,maxenfila,filanueva):
#Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja
        if maxenfila<self.enfila:
                n=self.enfila//2
                m=self.enfila-n
                for i in range(m):filanueva.insert(self.fila[m])
                for i in range(m):self.atender()
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila+=1
        self.fila.append(cliente.dni)
        pass

    def atender(self):
        """Atiende al proximo cliente preferencial"""
        self.enfila-=1
        self.fila.pop(0)
        pass      

    

class cliente(object):
#clase cliente """
    def __init__(self,dni):
         #""" constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        #"""modifica el atributo categoria del cliente """
        self.categoria=categoria
        pass
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""



pepe=cliente(999)
pepe.modificarcategoria('A')

print (pepe.dni,pepe.categoria)

fg=FilaGeneral()

fp1=FilaPreferencial()

fp2=FilaPreferencial()

FilaGeneral.insertar(pepe)

print (FilaGeneral.enfila,FilaGeneral.fila)

for i in range(10):
       FilaPreferencial.insertar(pepe)

fp1.abrircajanueva(5,fp2)

print(fp1.enfila,fp2.enfila)
