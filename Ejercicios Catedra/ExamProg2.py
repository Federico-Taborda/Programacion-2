#Examen Prog2

# barco ["buque1",(1,2),(1,3),(1,4)]
#tablero {(1,2):"buque1", (1,3):"tocado",(1,4):"buque1", (1,5):"agua tocada", "buque1":[(1,2),(1,3),(1,4)], "dimension":10,TERMINA:1}
#Terminar arranca con valor 0
#Un tablero de inicio seria #{"dimension":10,"TERMINA":0}
#disparo (2,2)




#Ejercicio 2 -----------------------------------------------------------------------------------------

def bloqueador(tablero,barco,i=1):
    bloq=False
    while i<len(barco) and not(bloq):
        (x,y)=barco[i] #coordenadas del barco
        pos_ru=(x+1,y+1)
        pos_u=(x,y+1)
        pos_lu=(x-1,y+1)
        pos_l=(x-1,y)
        pos_ld=(x-1,y-1)
        pos_d=(x,y-1)
        pos_rd=(x+1,y-1)
        pos_r=(x+1,y)
        pos_bloquear=[(x,y),pos_ru,pos_u,pos_lu,pos_l,pos_ld,pos_d,pos_rd,pos_r]
        for pos in pos_bloquear:
            if pos in tablero:
                bloq=True
        i+=1
    return bloq        

def adentro(tablero,tupla):
    dim=tablero["dimension"]
    return 1<=tupla[0] and tupla[0]<=dim and 1<=tupla[1] and tupla[1]<=dim

def valido(tablero, barco, i=1):
    val=True
    while i<len(barco) and val==True:
        (x,y)=barco[i] #mas legible
        if not(adentro(tablero,(x,y))) or bloqueador(tablero,barco): 
            val=False
        i+=1
    return val
       

def agregaBarco(tablero,barco):
        if valido(tablero, barco):
            listabar=[] #lista del barco
            i=1
            while i<len(barco):
                tablero[barco[i]]=barco[0] #pone el nombre del barco en la coordenada del tablero
                listabar.append(barco[i])
                i+=1
            tablero[barco[0]]=listabar #agrega el barco al tablero
            tablero["TERMINA"]+=1

            

#Ejercicio 3-------------------------------------------------------------------------------------------------
def contadorTocado(listabarco):
    contador=0
    for val in listabarco:
        if val=="TOCADO":
            contador+=1
    return contador


def disparo(tablero,disparo):
    dim=tablero["dimension"] 
    frase=""
    if disparo in tablero:
        if tablero[disparo]=="AGUA TOCADA" or tablero[disparo]=="TOCADO":
            frase="tiro no valido"
        else:
            nombrebarco=tablero[disparo] #para facilitar lectura
            tablero[nombrebarco].remove(disparo) 
            tablero[nombrebarco].append("TOCADO") #remplazo coordenada del barco por un "TOCADO"
            tablero[disparo]="TOCADO"
            if contadorTocado(tablero[nombrebarco])==len(tablero[nombrebarco]):
                frase="HUNDIDO"
                tablero["TERMINA"]+=-1
            else:
                frase="TOCADO"
    elif adentro(tablero,disparo):
        frase="AGUA"
        tablero[disparo]="AGUA TOCADA"
    else:
        frase="tiro no valido"
    print(frase)
    return frase
      
#Ejercicio 4-------------------------------------------------------------------------------------------------                

def juegoTerminado(tablero):
    return tablero["TERMINA"]==0

#Prueba

TABLERO={"dimension":10,"TERMINA":0}
agregaBarco(TABLERO,["lancha",(1,1)])
print(TABLERO)  
agregaBarco(TABLERO,["lancha",(1,1)]) 
print(TABLERO) 
agregaBarco(TABLERO,["buque",(1,1),(1,2),(1,3)]) 
print(TABLERO) 
agregaBarco(TABLERO,["buque",(3,1),(3,2),(3,3)])
print(TABLERO) 
disparo(TABLERO,(1,1))
disparo(TABLERO,(1,2))
print(TABLERO) 
disparo(TABLERO,(1,2))
print(TABLERO)
disparo(TABLERO,(3,1))
print(juegoTerminado(TABLERO))
disparo(TABLERO,(3,2))
print(juegoTerminado(TABLERO))
disparo(TABLERO,(3,3))
print(juegoTerminado(TABLERO))