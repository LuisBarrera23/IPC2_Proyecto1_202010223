from Nodoterreno import nodoterreno

class listaT:
    def __init__(self):
        self.primero=None

    def insertar(self,Terreno):
        if self.primero is None:
            self.primero=nodoterreno(Terreno)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoterreno(Terreno)  

    def recorrer(self):
        actual=self.primero
        while actual:
            print("Nombre:",actual.terreno.nombre,"\tdimensiones:",actual.terreno.m,"x",actual.terreno.n)
            actual=actual.siguiente     

    def buscar(self,nombre):
        actual=self.primero
        while actual:
            if actual.terreno.nombre==nombre:
                return actual.terreno
            actual=actual.siguiente
