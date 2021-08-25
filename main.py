from xml.dom import minidom
from Terreno import terreno
from ListaTerrenos import listaT
from Area import area
from ListaAreas import listaA
import time

Terrenos=listaT()

def lecturaXml():
    global Terrenos
    Terrenos=listaT()

    ruta=input("Ingresa la ruta del archivo XML que desea cargar: ")
    documento=minidom.parse(ruta)
    Listado=documento.getElementsByTagName("terreno")
    for t in Listado:
        areas=listaA()
        nombre=t.getAttribute("nombre")

        dimensiones=t.getElementsByTagName("dimension")[0]
        m=int(dimensiones.getElementsByTagName("m")[0].firstChild.data)
        n=int(dimensiones.getElementsByTagName("n")[0].firstChild.data)

        posicioninicio=t.getElementsByTagName("posicioninicio")[0]
        iniX=int(posicioninicio.getElementsByTagName("x")[0].firstChild.data)
        iniY=int(posicioninicio.getElementsByTagName("y")[0].firstChild.data)

        posicionfinal=t.getElementsByTagName("posicionfin")[0]
        finX=int(posicionfinal.getElementsByTagName("x")[0].firstChild.data)
        finY=int(posicionfinal.getElementsByTagName("y")[0].firstChild.data)
        #print("posicion inicio para:",nombre, "X=",iniX,"Y=",iniY,", su posicion final es:","X=",finX,"Y=",finY)

        posiciones=t.getElementsByTagName("posicion")

        for posicion in posiciones:
            posX=int(posicion.getAttribute("x"))
            posY=int(posicion.getAttribute("y"))
            combustible=int(posicion.firstChild.data)
            #print("posicion:","X:",posX,"Y:",posY,"gasta combustible:",combustible)
            Area=area(posX,posY,combustible)
            areas.insertar(Area)
        Terreno=terreno(nombre,iniX,iniY,finX,finY,m,n,areas)
        Terrenos.insertar(Terreno)

def escrituraXml(Tobjeto):
    pass
    
def analizarTerreno(terreno):
    mapa=terreno.mapa
    iniX=terreno.posXinicio
    iniY=terreno.posYinicio
    finX=terreno.posXfinal
    finY=terreno.posYfinal
    m=terreno.m
    n=terreno.n
    combustible=0

    actualx=iniX
    actualy=iniY
    mapa.actualizar(actualx,actualy)
    while actualx!=finX or actualy!=finY:
        if actualx<finX:
            actualx+=1
            mapa.actualizar(actualx,actualy)
            continue
        if actualx>finX:
            actualx-=1
            mapa.actualizar(actualx,actualy)
            continue
        if actualy<finY:
            actualy+=1
            mapa.actualizar(actualx,actualy)
            continue
        if actualy>finY:
            actualy-=1
            mapa.actualizar(actualx,actualy)
            continue
    
    Terrenos.actualizarmapa(terreno.nombre,mapa,combustible)
    cadena=""
    print("Calculando la mejor ruta")
    time.sleep(5)
    print("Calculando cantidad de combustible")
    time.sleep(3)
    print()
    for j in range(1,n+1):
        for i in range(1,m+1):
            area=mapa.buscar(i,j)
            if area is None:
                continue
            else:
                cadena+="|"
                if area.usado:
                    cadena+=" 1 "
                    combustible+=area.combustible
                else:
                    cadena+=" 0 "
                cadena+="|"
        cadena+="\n"
    print(cadena)
    Terrenos.actualizarmapa(terreno.nombre,mapa,combustible)
    print("Combustible necesario: ",combustible,"unidades")

   

def menu():
    global Terrenos
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
                lecturaXml()
            elif opcion==2:
                if Terrenos.primero:
                    Terrenos.recorrer()
                    nombre=str(input("Ingrese el nombre del terreno que desea procesar: "))
                    solicitado=Terrenos.buscar(nombre)
                    analizarTerreno(solicitado)
                else:
                    print("Por favor Cargue primero el archivo XML")

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