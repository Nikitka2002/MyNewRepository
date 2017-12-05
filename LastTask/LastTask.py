import random

def MatrixCreature(x,y,Way):
    matrix=[]
    if (Way == "Auto"):
        print("Ввидите дипапазон:")
        for i in range(x):
            for j in range(y):
                z = random.randint(a=int(input("Ввидите число А: ")), b=int(input("Ввидите число В: ")))
                matrix.append(z)
    elif (Way == "Manually"):
        for i in range(x):
            for j in range(y):
                matrix.append(input("Ввидите элемент матрицы: "))


class SquareMatrix:
    matrix=[]
    count = int(0)
    def __init__(self,x,y,Way):
        self.matrix = MatrixCreature(x,y,Way)
        self.count+=1
