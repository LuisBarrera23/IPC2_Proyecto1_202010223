from Nodoarea import nodoarea

class listaA:
    def __init__(self):
        self.primero=None

    def insertar(self,Area):
        if self.primero is None:
            self.primero=nodoarea(Area)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoarea(Area)

    def recorrer(self):
        actual=self.primero
        while actual:
            print("X=",actual.area.posx,"Y=",actual.area.posy,"Combustible=",actual.area.combustible)
            actual=actual.siguiente
