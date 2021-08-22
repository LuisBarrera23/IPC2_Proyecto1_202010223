from xml.dom import minidom
from Terreno import terreno
from ListaTerrenos import listaT
from Area import area
from ListaAreas import listaA

Terrenos=None

def lecturaXml():
    Terrenos=listaT()

    ruta=input("Ingresa la ruta del archivo XML que desea cargar")
    documento=minidom.parse(ruta)
    Listado=documento.getElementsByTagName("terreno")
    for t in Listado:
        areas=listaA()
        nombre=t.getAttribute("nombre")

        dimensiones=t.getElementsByTagName("dimension")[0]
        m=dimensiones.getElementsByTagName("m")[0].firstChild.data
        n=dimensiones.getElementsByTagName("n")[0].firstChild.data

        posicioninicio=t.getElementsByTagName("posicioninicio")[0]
        iniX=posicioninicio.getElementsByTagName("x")[0].firstChild.data
        iniY=posicioninicio.getElementsByTagName("y")[0].firstChild.data

        posicionfinal=t.getElementsByTagName("posicionfin")[0]
        finX=posicionfinal.getElementsByTagName("x")[0].firstChild.data
        finY=posicionfinal.getElementsByTagName("y")[0].firstChild.data
        #print("posicion inicio para:",nombre, "X=",iniX,"Y=",iniY,", su posicion final es:","X=",finX,"Y=",finY)

        posiciones=t.getElementsByTagName("posicion")

        for posicion in posiciones:
            posX=posicion.getAttribute("x")
            posY=posicion.getAttribute("y")
            combustible=posicion.firstChild.data
            #print("posicion:","X:",posX,"Y:",posY,"gasta combustible:",combustible)
            Area=area(posX,posY,combustible)
            areas.insertar(Area)
        Terreno=terreno(nombre,iniX,iniY,finX,finY,m,n,areas)
        Terrenos.insertar(Terreno)

    Terrenos.recorrer()
    

    


def menu():
    opcion=0
    while True:
        print("----------MENU PRINCIPAL----------")
        print("\t1.Cargar archivo")
        print("\t2.Procesar archivo")
        print("\t3.Escribir archivo salida")
        print("\t4.Mostrar datos del estudiante")
        print("\t5.Generar gráfica")
        print("\t6.Salida")
        print("----------------------------------")
        try:
            opcion=int(input('Ingrese el numero de opción deseada:\n'))
            if opcion==1:
                print('Cargar archivo')
                lecturaXml()
            elif opcion==2:
                print('Procesar archivo')
            elif opcion==3:
                print('Escribir archivo salida')
            elif opcion==4:
                print('Datos del Estudiante:')
                print('> Luis Angel Barrera Velásquez')
                print('> 202010223')
                print('> Introducción a la Programación y Computación 2 sección E')
                print('> Ingenieria en Ciencias y Sistemas')
                print('> 4to Semestre')
            elif opcion==5:
                print('Generar gráfica')
            elif opcion==6:
                print("Saliendo del programa")
                exit(0)
            else:
                print("Opción no valida")

        except:
            if opcion==6:
                exit(0)
            print("Error, vuelva a intentarlo")


if __name__=='__main__':
    menu()