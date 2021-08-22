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
            print("Nombre:",actual.terreno.nombre)
            print("posinicio:(",actual.terreno.posXinicio,actual.terreno.posYinicio,")")
            print("posfinal:(",actual.terreno.posXfinal,actual.terreno.posYfinal,")")
            print("dimensiones:(",actual.terreno.m,actual.terreno.n,")")
            actual.terreno.mapa.recorrer()
            actual=actual.siguiente      