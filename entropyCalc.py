import math
import matplotlib.pyplot as plt

def init(json):
    S = []
    for i in range(0, len(json)):
        c = json[i]
        N = [0]*100
        S1 = 0
        for j in range(0,10000):
            if(c[j]):
                N[(j//10)%10 + 10*((j//1000))] += 1
        for j in range(0,100):
            try:
                S1 += -(N[j]/100)*math.log(N[j]/100)
            except (ValueError):
                S1 += 0
        S.append(S1)
    plt.plot(S)
    plt.ylabel('Entropía')
    plt.xlabel('Pasos')
    plt.show()
