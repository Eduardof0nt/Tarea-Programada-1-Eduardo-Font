import json
import cell
import calcSimulation
import drawer
import entropyCalc


if __name__ == "__main__":
    while(True):
        inp = input("Seleccione la función que desea utilizar:\n1) Realizar simulación y guardar en archivo\n2) Dibujar vista seleccionada de una archivo de simulación\n3) Calcular y graficar la entropía de un archvo de simulación\nIngrese la opción deseada: ")
        if inp == '1':
            file = input('Seleccione el nombre del archivo (sin extensión): ')
            file += '.json'
            iterations = int(input('Seleccione el número de iteraciones: '))
            calcSimulation.calculate(iterations, file)
            print('-'*10 + '\n'*4)
        elif inp == '2':
            file = input('Seleccione el nombre del archivo que desea dibujar (sin extensión): ')
            file += '.json'
            iteration = int(input('Seleccione el número de iteracion que desea dibujar: '))
            f = open(file,"r")
            j = json.loads(f.read())
            drawer.init(j[iteration-1])
            print('-'*10 + '\n'*4)
        elif inp == '3':
            file = input('Seleccione el nombre del archivo que desea dibujar (sin extensión): ')
            file += '.json'
            f = open(file,"r")
            j = json.loads(f.read())
            entropyCalc.init(j)
            print('-'*10 + '\n'*4)
        else:
            print('Opción inválida\n')
            print('-'*10 + '\n'*4)
