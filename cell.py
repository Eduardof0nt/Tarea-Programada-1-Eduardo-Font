#La clase cell define cada celda del arreglo
class cell():    
    def __init__(self, index, t = None):
        #El índice de esta celda en el arreglo
        self.index = index
        #Se toma la tortuga de dibujo
        self.t = t
        #El estado actual de la celda (True para negro y False para blanco)
        self.currentState = False
        if index > 4500 and index < 5500 and index%100 > 45 and index%100 <= 55:
            self.currentState = True
        #El siguente estado de la celda    
        self.nextState = False
        #Los vecinos de esta celda
        # Los vecinos están ubicados con los siguientes índices
        #    0 1 2
        #    3 X 5
        #    6 7 8
        self.neighbors = [None]*9
        #Verificar si en la iteración ya se revisó esta celda
        self.checked = False
        self.isMoving = False

    #Se define la función que dibuja la celda
    def drawCell(self):
        #Color de relleno del cuadrado
        color = 'maroon'
        if self.currentState:
            color = 'chocolate'
        self.t.pencolor(color)
        self.t.fillcolor(color)
        self.t.begin_fill()
        for i in range(0,4):
            self.t.forward(5)
            self.t.right(90)
        self.t.end_fill()
        if(self.index%100 == 99):
            self.t.penup()
            self.t.goto(-250,self.t.ycor()-5)
            self.t.pendown()
        else:
            self.t.forward(5)
            
    def setNeighbors(self, cells):
        if(self.index-101 >= 0 and self.index%100 != 0):
            self.neighbors[0] = cells[self.index-101]
        if(self.index-100 >= 0):
            self.neighbors[1] = cells[self.index-100]
        if(self.index-99 >= 0 and self.index%100 != 99):
            self.neighbors[2] = cells[self.index-99]
        if(self.index%100 != 0):
            self.neighbors[3] = cells[self.index-1]
        if(self.index%100 != 99):
            self.neighbors[5] = cells[self.index+1]
        if(self.index+99 <= 9999 and self.index%100 != 0):
            self.neighbors[6] = cells[self.index+99]
        if(self.index+100 <= 9999):
            self.neighbors[7] = cells[self.index+100]
        if(self.index+101 <= 9999 and self.index%100 != 99):
            self.neighbors[8] = cells[self.index+101]

    def toJSON(self):
        JSON = '{\n"index": ' + str(self.index) + ',\n"currentState": ' + str(self.currentState).lower() + ',\n"neighbors": ['
        for n in range(0,9):
            try:
                JSON += str(self.neighbors[n].index).lower()
            except(AttributeError):
                JSON += 'null'
            if n != 8:
                JSON += ','
            else:
                JSON += ']\n}'
        return JSON
