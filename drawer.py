import turtle
import cell

def redrawAll(cells, screen1):
    for cell in cells:
        cell.drawCell()
    screen1.update()
    cells[0].t.penup()
    cells[0].t.goto(-250,250)

def init(json):
    #Se inicia la pantalla de Turtle
    screen1 = turtle.Screen()
    screen1.screensize(300,300)
    screen1.title("Tarea Programada 1")
    t = turtle.Turtle()
    t.hideturtle()
    screen1.tracer(0,0)
    t.speed(0)
    t.penup()
    t.goto(-250,250)
    t.pendown()
    t.pencolor('maroon')
    t.fillcolor('maroon')
    t.begin_fill()
    t.goto(-250,-250)
    t.goto(250,-250)
    t.goto(250,250)
    t.goto(-250,250)
    t.end_fill()
    #Se comienza con el arreglo de las celdas    
    cells = []
    #Se llena el arreglo
    for i in range(0,10000):
        cells.append(cell.cell(i,t))
    for i in range(0, 10000):
        cells[i].currentState = json[i]
    redrawAll(cells, screen1)
