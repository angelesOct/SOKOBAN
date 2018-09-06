fila = 3
columna = 4
mapa = [[3,3,3,3,3,3,3,3,3],[3,4,4,4,4,4,4,4,3],[3,4,1,1,4,4,4,2,3],[3,4,4,4,0,4,4,4,3],[3,4,1,4,4,4,4,2,3],[3,4,4,4,4,4,4,4,3],[3,3,3,3,3,3,3,3,3]]
""""
mapa = [] #codigo para cambiar de nivel (incompleto). 
nivel= 0
while True:
    if 
        print "_________________","NIVEL",nivel,"___________________\n"
        nivel_juego = "mapanivel" + str(nivel) + ".mago"
        file = open(nivel_juego , "r")
        for row in file.readlines():
            lista = []
            for c in row:
                lista.append(c)
            lista.pop()
            mapa.append(lista)
    nivel = nivel +1
"""
while True:
    import os  # limpia pantalla, evitando que se impriman muchos mapas cada vez que se juega
    print "A = izquierda","D = derecha","W = arriba","S = abajo"
    print "f = activar poder","q = desactivar poder"
    for x in mapa: 
        for i in x:
            print i, #imprime el mapa en 2D
        print
    movimiento = raw_input ("Mueve a soko:") 
    if movimiento == "f":
        fuerza = True
    if movimiento == "f": #Activar la fuerza
        fuerza = True   
    if movimiento == "q": 
        fuerza = False 
    if movimiento == "d": #movimiento hacia la izquierda
        if mapa [fila] [columna]  == 0 and mapa [fila] [columna+1]==4:
           mapa [fila] [columna]=4
           mapa [fila] [columna+1]=0
           columna=columna+1
        elif mapa [fila] [columna]  == 0 and mapa [fila] [columna+1]==1 and mapa [fila] [columna+2]==4:
            mapa [fila] [columna]=4
            mapa [fila] [columna+1]=0
            mapa [fila] [columna+2]=1
            columna=columna+1
        elif mapa [fila] [columna]  == 0 and mapa [fila] [columna+1]==1 and mapa [fila] [columna+2]==2:
           mapa [fila] [columna]=4
           mapa [fila] [columna+1]=0
           mapa [fila] [columna+2]=5
           columna=columna+1
        elif mapa [fila] [columna]  == 0 and mapa [fila] [columna+1]==5 and mapa [fila] [columna+2]==2:
           mapa [fila] [columna]=4
           mapa [fila] [columna+1]=6
           mapa [fila] [columna+2]=5
           columna=columna+1
        elif mapa [fila] [columna]  == 6 and mapa [fila] [columna+1]==4:
           mapa [fila] [columna]=2
           mapa [fila] [columna+1]=0
           columna=columna+1
        elif mapa [fila] [columna]== 0 and mapa[fila] [columna+1] ==2:
           mapa [fila] [columna]=4
           mapa [fila] [columna+1]=6
           columna=columna+1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna+1]==5 and mapa [fila] [columna+2]==4:
           mapa [fila] [columna]=2
           mapa [fila] [columna+1]=6
           mapa [fila] [columna+2]=1
           columna=columna+1
        elif mapa [fila] [columna]== 0 and mapa [fila] [columna+1]==5 and mapa [fila] [columna+2]==4:
           mapa [fila] [columna]=4
           mapa [fila] [columna+1]=6
           mapa [fila] [columna+2]=1
           columna=columna+1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna+1]==5 and mapa [fila] [columna+2]==2:
           mapa [fila] [columna]=2
           mapa [fila] [columna+1]=6
           mapa [fila] [columna+2]=5
           columna=columna+1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna+1]==2 :
           mapa [fila] [columna]=2
           mapa [fila] [columna+1]=6
           columna=columna+1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna+1]==1 and mapa [fila] [columna+2]==4:
           mapa [fila] [columna]=2
           mapa [fila] [columna+1]=0
           mapa [fila] [columna+2]=1
           columna=columna+1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna+1]==1 and mapa [fila] [columna+2]==2:
           mapa [fila] [columna]=2
           mapa [fila] [columna+1]=0
           mapa [fila] [columna+2]=1
           columna=columna+1
        if mapa [fila][columna+1] == 1 and mapa [fila][columna+2] == 1 and  mapa [fila][columna+3] ==4 and fuerza == True:  #mover dos cajas
            mapa [fila][columna] = 4
            columna = columna +1
            mapa [fila][columna] = 0
            mapa [fila][columna+1] = 1
            mapa [fila][columna+2] = 1
    if movimiento == "a": #movimiento hacia la derecha 
        if mapa [fila] [columna]  == 0 and mapa [fila] [columna-1]==4:
            mapa [fila] [columna]=4
            mapa [fila] [columna-1]=0
            columna=columna-1
        elif mapa [fila] [columna]  == 0 and mapa [fila] [columna-1]==1 and mapa [fila] [columna-2]==4:
            mapa [fila] [columna]=4
            mapa [fila] [columna-1]=0
            mapa [fila] [columna-2]=1
            columna=columna-1
        elif mapa [fila] [columna]  == 0 and mapa [fila] [columna-1]==1 and mapa [fila] [columna-2]==2:
            mapa [fila] [columna]=4
            mapa [fila] [columna-1]=0
            mapa [fila] [columna-2]=5
            columna=columna-1
        elif mapa [fila] [columna]  == 0 and mapa [fila] [columna-1]==5 and mapa [fila] [columna-2]==2:
            mapa [fila] [columna]=4
            mapa [fila] [columna-1]=6
            mapa [fila] [columna-2]=5
            columna=columna-1
        elif mapa [fila] [columna]  == 6 and mapa [fila] [columna-1]==4:
            mapa [fila] [columna]=2
            mapa [fila] [columna-1]=0
            columna=columna-1
        elif mapa [fila] [columna]== 0 and mapa[fila] [columna-1] ==2:
            mapa [fila] [columna]=4
            mapa [fila] [columna-1]=6
            columna=columna-1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna-1]==5 and mapa [fila] [columna-2]==4:
            mapa [fila] [columna]=2
            mapa [fila] [columna-1]=6
            mapa [fila] [columna-2]=1
            columna=columna-1
        elif mapa [fila] [columna]== 0 and mapa [fila] [columna-1]==5 and mapa [fila] [columna-2]==4:
            mapa [fila] [columna]=4
            mapa [fila] [columna-1]=6
            mapa [fila] [columna-2]=1
            columna=columna-1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna-1]==5 and mapa [fila] [columna-2]==2:
            mapa [fila] [columna]=2
            mapa [fila] [columna-1]=6
            mapa [fila] [columna-2]=5
            columna=columna-1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna-1]==2 :
            mapa [fila] [columna]=2
            mapa [fila] [columna-1]=6
            columna=columna-1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna-1]==1 and mapa [fila] [columna-2]==4:
            mapa [fila] [columna]=2
            mapa [fila] [columna-1]=0
            mapa [fila] [columna-2]=1
            columna=columna-1
        elif mapa [fila] [columna]== 6 and mapa [fila] [columna-1]==1 and mapa [fila] [columna-2]==2:
            mapa [fila] [columna]=2
            mapa [fila] [columna-1]=0
            mapa [fila] [columna-2]=1
            columna=columna-1
        if mapa [fila][columna-1] == 1 and mapa [fila][columna-2] == 1 and  mapa [fila][columna-3] ==4 and fuerza == True:  #mover dos cajas
            mapa [fila][columna] = 4
            columna = columna -1
            mapa [fila][columna] = 0
            mapa [fila][columna-1] = 1
            mapa [fila][columna-2] = 1
    if movimiento == "w": #movimiento hacia arriba 
        if mapa [fila] [columna]  == 0 and mapa [fila-1] [columna]==4:
           mapa [fila] [columna]=4
           mapa [fila-1] [columna]=0
           fila=fila-1
        elif mapa [fila] [columna]  == 0 and mapa [fila-1] [columna]==1 and mapa [fila-2] [columna]==4:
            mapa [fila] [columna]=4
            mapa [fila-1] [columna]=0
            mapa [fila-2] [columna]=1
            fila=fila-1
        elif mapa [fila] [columna]  == 0 and mapa [fila-1] [columna]==1 and mapa [fila-2] [columna]==2:
            mapa [fila] [columna]=4
            mapa [fila-1] [columna]=0
            mapa [fila-2] [columna]=5
            fila=fila-1
        elif mapa [fila] [columna]  == 0 and mapa [fila-1] [columna]==5 and mapa [fila-2] [columna]==2:
            mapa [fila] [columna]=4
            mapa [fila-1] [columna]=6
            mapa [fila-2] [columna]=5
            fila=fila-1  
        elif mapa [fila] [columna]  == 6 and mapa [fila-1] [columna]==4 :
            mapa [fila] [columna]=2
            mapa [fila-1] [columna]=0
            fila=fila-1
        elif mapa [fila] [columna]== 0 and mapa[fila-1] [columna] ==2:
            mapa [fila] [columna]=4
            mapa [fila-1] [columna]=6
            fila=fila-1
        elif mapa [fila] [columna]== 6 and mapa [fila-1] [columna]==5 and mapa [fila-2] [columna]==4:
            mapa [fila] [columna]=2
            mapa [fila-1] [columna]=6
            mapa [fila-2] [columna]=1
            fila=fila-1
        elif mapa [fila] [columna]== 0 and mapa [fila-1] [columna]==5 and mapa [fila-2] [columna]==4:
            mapa [fila] [columna]=4
            mapa [fila-1] [columna]=6
            mapa [fila-2] [columna]=1
            fila=fila-1
        elif mapa [fila] [columna]== 6 and mapa [fila-1] [columna]==5 and mapa [fila-2] [columna]==2:
            mapa [fila] [columna]=2
            mapa [fila-1] [columna]=6
            mapa [fila-2] [columna]=5
            fila=fila-1
        elif mapa [fila] [columna]== 6 and mapa [fila-1] [columna]==2 :
            mapa [fila] [columna]=2
            mapa [fila-1] [columna]=6
            fila=fila-1
        elif mapa [fila] [columna]== 6 and mapa [fila-1] [columna]==1 and mapa [fila-2] [columna]==4:
            mapa [fila] [columna]=2
            mapa [fila-1] [columna]=0
            mapa [fila-2] [columna]=1
            fila=fila-1
        elif mapa [fila] [columna]== 6 and mapa [fila-1] [columna]==1 and mapa [fila-2] [columna]==2:
            mapa [fila] [columna]=2
            mapa [fila-1] [columna]=0
            mapa [fila-2] [columna]=1
            fila=fila-1 
        if mapa [fila-1][columna] == 1 and mapa [fila-2][columna] == 1 and  mapa [fila-3][columna] ==4 and fuerza == True:  #mover dos cajas
            mapa [fila][columna] = 4
            fila = fila -1
            mapa [fila][columna] = 0
            mapa [fila-1][columna] = 1
            mapa [fila-2][columna] = 1
    if movimiento == "s": # movimiento hacia abajo    
        if mapa [fila] [columna]  == 0 and mapa [fila+1] [columna]==4:
           mapa [fila] [columna]=4
           mapa [fila+1] [columna]=0
           fila=fila+1
        elif mapa [fila] [columna]  == 0 and mapa [fila+1] [columna]==1 and mapa [fila+2] [columna]==4:
            mapa [fila] [columna]=4
            mapa [fila+1] [columna]=0
            mapa [fila+2] [columna]=1
            fila=fila+1
        elif mapa [fila] [columna]  == 0 and mapa [fila+1] [columna]==1 and mapa [fila+2] [columna]==2:
            mapa [fila] [columna]=4
            mapa [fila+1] [columna]=0
            mapa [fila+2] [columna]=5
            fila=fila+1
        elif mapa [fila] [columna]  == 0 and mapa [fila+1] [columna]==5 and mapa [fila+2] [columna]==2:
            mapa [fila] [columna]=4
            mapa [fila+1] [columna]=6
            mapa [fila+2] [columna]=5
            fila=fila+1
        elif mapa [fila] [columna]  == 6 and mapa [fila+1] [columna]==4 :
            mapa [fila] [columna]=2
            mapa [fila+1] [columna]=0
            fila=fila+1
        elif mapa [fila] [columna]== 0 and mapa[fila+1] [columna] ==2:
            mapa [fila] [columna]=4
            mapa [fila+1] [columna]=6
            fila=fila+1
        elif mapa [fila] [columna]== 6 and mapa [fila+1] [columna]==5 and mapa [fila+2] [columna]==4:
            mapa [fila] [columna]=2
            mapa [fila+1] [columna]=6
            mapa [fila+2] [columna]=1
            fila=fila+1
        elif mapa [fila] [columna]== 0 and mapa [fila+1] [columna]==5 and mapa [fila+2] [columna]==4:
            mapa [fila] [columna]=4
            mapa [fila+1] [columna]=6
            mapa [fila+2] [columna]=1
            fila=fila+1
        elif mapa [fila] [columna]== 6 and mapa [fila+1] [columna]==5 and mapa [fila+2] [columna]==2:
            mapa [fila] [columna]=2
            mapa [fila+1] [columna]=6
            mapa [fila+2] [columna]=5
            fila=fila+1
        elif mapa [fila] [columna]== 6 and mapa [fila+1] [columna]==2 :
            mapa [fila] [columna]=2
            mapa [fila+1] [columna]=6
            fila=fila+1
        elif mapa [fila] [columna]== 6 and mapa [fila+1] [columna]==1 and mapa [fila+2] [columna]==4:
            mapa [fila] [columna]=2
            mapa [fila+1] [columna]=0
            mapa [fila+2] [columna]=1
            fila=fila+1
        elif mapa [fila] [columna]== 6 and mapa [fila+1] [columna]==1 and mapa [fila+2] [columna]==2:
            mapa [fila] [columna]=2
            mapa [fila+1] [columna]=0
            mapa [fila+2] [columna]=1
            fila=fila+1 
        if mapa [fila+1][columna] == 1 and mapa [fila+2][columna] == 1 and  mapa [fila+3][columna] ==4 and fuerza == True:  #mover dos cajas
            mapa [fila][columna] = 4
            fila = fila +1
            mapa [fila][columna] = 0
            mapa [fila+1][columna] = 1
            mapa [fila+2][columna] = 1
    os.system('cls') #terminacion de limpiar pantalla
