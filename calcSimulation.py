import random
import os
import math

#<---------- Funciones ---------->

def calculateNext(cells):
    for cell in cells:
        locked = cell.currentState
        if locked:
            for i in range(0,9):
                try:
                    locked = locked and cell.neighbors[i].currentState
                except (AttributeError):
                    pass
        if locked:
            cell.nextState = True
            cell.checked = True
    for cell in cells:
        if not cell.checked and cell.currentState:
            movableNeighbors = []
            for n in cell.neighbors:
                try:
                    if not n.currentState and not n.nextState:
                        movableNeighbors.append(n)
                except (AttributeError):
                    pass
            random.shuffle(movableNeighbors)
            i = random.randint(0, math.floor(len(movableNeighbors)*4))
            if i < len(movableNeighbors):
                movableNeighbors[i].nextState = True
                cell.nextState = False
                cell.isMoving = True
            else:
                cell.nextState = True
    for cell in cells:
        cell.currentState = cell.nextState
        cell.nextState = False
        cell.checked = False
        cell.isMoving = False

def calculate(iterations, file):
    import cell
    if os.path.exists(file):
        os.remove(file) #this deletes the file
    f = open(file,"w")
    #Se comienza con el arreglo de las celdas    
    cells = []
    #Se llena el arreglo
    for i in range(0,10000):
        cells.append(cell.cell(i))
    #Se hace la relación entre vecinos
    for cell in cells:
        cell.setNeighbors(cells)
    #Código itrativo de la simulación
    JSON = '['
    for i in range(0,iterations):
        if i != 0:
            calculateNext(cells)
        JSON += '['
        for cell in cells:
            JSON += str(int(cell.currentState))
            if cell.index != 9999:
                JSON += ','
        JSON += ']\n'
        if(i != iterations-1):
            JSON += ',\n'
    JSON += ']'
    f.write(JSON)
    f.close()
