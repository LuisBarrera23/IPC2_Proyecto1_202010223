from xml.dom import minidom
from xml.dom.minidom import parseString
from Terreno import terreno
from ListaTerrenos import listaT
from Area import area
from ListaAreas import listaA
import time
from os import system,startfile

Terrenos=listaT()

def lecturaXml():
    global Terrenos
    Terrenos=listaT()

    ruta=input("Ingresa la ruta del archivo XML que desea cargar: ")
    a=open(ruta,"r")
    cadena=a.read().lower()
    a.close()
    documento=minidom.parseString(cadena)
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

def escrituraXml(Tobjeto,destino):
    f=open(destino,"w",encoding='UTF-8')
    mapa=Tobjeto.mapa
    nombre=Tobjeto.nombre
    iniX=Tobjeto.posXinicio
    iniY=Tobjeto.posYinicio
    finX=Tobjeto.posXfinal
    finY=Tobjeto.posYfinal
    m=Tobjeto.m
    n=Tobjeto.n
    combustible=Tobjeto.combustible
    documento="<terreno nombre="+nombre+">"
    documento+="\n\t<posicioninicio>\n\t\t<x>"+str(iniX)+"</x>\n\t\t<y>"+str(iniY)+"</y>\n\t</posicioninicio>"
    documento+="\n\t<posicionfin>\n\t\t<x>"+str(finX)+"</x>\n\t\t<y>"+str(finY)+"</y>\n\t</posicionfin>"
    documento+="\n\t<combustible>"+str(combustible)+"</combustible>"
    for j in range(1,n+1):
        for i in range(1,m+1):
            area=mapa.buscar(i,j)
            if area.usado:
                documento+="\n\t<posicion x=\""+str(area.posx)+"\" y=\""+str(area.posy)+"\">1</posicion>"
    documento+="\n</terreno>"
    f.write(documento)
    f.close()
    print("Se escribio el archivo satisfactoriamente")
    
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
    print("Calculando la mejor ruta...")
    time.sleep(3)
    print("Calculando cantidad de combustible...")
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
    if combustible<9999:
        print("El Robot si llego a su destino")
    else:
        print("El Robot no llego a su destino, combustible insuficiente...")
    print("Combustible necesario: ",combustible,"unidades")

def graficarTerreno(terreno):
    mapa=terreno.mapa
    nombre=terreno.nombre
    m=terreno.m
    n=terreno.n
    #asignando nombre a cada nodo area
    iterador=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            area=mapa.buscar(i,j)
            if area is None:
                continue
            else:
                area.nombre="nodo"+str(iterador)
                iterador+=1
    cadena="""
    graph grid{
	layout=dot
	labelloc = "t"
	node [shape=ellipse]
	// arbitrary path on rigid grid

	edge [weight=1500 color=black]
    """
    for i in range(1,m+1):
        for j in range(1,n+1):
            area=mapa.buscar(i,j)
            if area is None:
                continue
            else:
                if area.usado:
                    cadena+=str(area.nombre)+"[color=greenyellow style=filled label="+str(area.combustible)+"]\n"
                else:
                    cadena+=str(area.nombre)+"[color=skyblue style=filled label=\""+str(area.combustible)+"\"]\n"
    for i in range(1,m+1):
        for j in range(1,n+1):
            area=mapa.buscar(i,j)
            if area is None:
                continue
            else:
                if j==n:
                    cadena+=str(area.nombre)+"\n"
                else:
                    cadena+=str(area.nombre)+" --"
    

    for j in range(1,n+1):
        cadena+="rank=same {"
        for i in range(1,m+1):
            area=mapa.buscar(i,j)
            if area is None:
                continue
            else:
                if i==m:
                    cadena+=str(area.nombre)+"}\n"
                else:
                    cadena+=str(area.nombre)+" --"


    cadena+="label="+str(nombre)+"}"
    archivo=open("grafica"+str(nombre)+".dot","w")
    archivo.write(cadena)
    archivo.close()
    original="grafica"+str(nombre)+".dot"
    convertido="grafica"+str(nombre)+".png"
    system("dot -Tpng "+original+" -o "+convertido)
    startfile("grafica"+str(nombre)+".png")

def menu():
    global Terrenos
    opcion=0
    while True:
        print("----------MENU PRINCIPAL----------")
        print("\t1.Cargar archivo")
        print("\t2.Procesar archivo")
        print("\t3.Escribir archivo salida")
        print("\t4.Mostrar datos del estudiante")
        print("\t5.Generar gr??fica")
        print("\t6.Salida")
        print("----------------------------------")
        try:
            opcion=int(input('Ingrese el numero de opci??n deseada:\n'))
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
                if Terrenos.primero:
                    print('Los terrenos procesados son los siguientes:')
                    comprobacion=Terrenos.verUsados()
                    if comprobacion!=False:   
                        nombre=str(input("Ingrese el nombre del terreno que desea generar el archivo XML: "))
                        ruta=str(input("Escribir una ruta especifica: "))
                        solicitado=Terrenos.buscar(nombre)
                        escrituraXml(solicitado,ruta)
            elif opcion==4:
                print('Datos del Estudiante:')
                print('> Luis Angel Barrera Vel??squez')
                print('> 202010223')
                print('> Introducci??n a la Programaci??n y Computaci??n 2 secci??n E')
                print('> Ingenieria en Ciencias y Sistemas')
                print('> 4to Semestre')
            elif opcion==5:
                if Terrenos.primero:
                    Terrenos.recorrer()
                    nombre=str(input("Ingrese el nombre del terreno que desea graficar: "))
                    solicitado=Terrenos.buscar(nombre)
                    graficarTerreno(solicitado)
                else:
                    print("Por favor Cargue primero el archivo XML")
            elif opcion==6:
                print("Saliendo del programa")
                exit(0)
            else:
                print("Opci??n no valida")

        except:
            if opcion==6:
                exit(0)
            print("Error, vuelva a intentarlo")


if __name__=='__main__':
    menu()