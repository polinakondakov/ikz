import math
x0 = [0, 0, 0]
x = [0, 0, 0]
def F(x):
    return x[0]**2 + 4*x[0]*x[1] + 17*x[1]**2 + 5*x[1]
    #return x[0]**2 + 5*x[1]**2 + 8*x[2]**2 - x[0]*x[1] + x[0]*x[2] - x[1]*x[2] + 5*x[0] - 3*x[1] + x[2]
def dX(x):
    return 2*x[0] + 4*x[1]
    #return 2*x[0] - x[1] + x[2] + 5
def dY(x):
    return 4*x[0] + 34*x[1] + 5
    #return 10*x[1] - x[0] - x[2] - 3
def dZ(x):
    return 0
    #return 16*x[2] + x[0] - x[1] + 1
def normVector(x, y ,z):
    return math.sqrt(x**2 + y**2 + z**2)

print("Введите начальные приближения X, Y, Z (в случае если функция не зависит от Z, введите для Z любое число)")
x0[0] = float(input("Xo = "))
x0[1] = float(input("Yo = "))
x0[2] = float(input("Zo = "))
eps = float(input("Введите погрешность: eps = "))
a = float(input("Введите начальное значение шага а = "))
x = x0
count = 0
while normVector(dX(x), dY(x), dZ(x)) >= eps: #условие выхода
    f0 = F(x) # f0 хранит старое значение функции
    x[0] -= a * dX(x0) #обновляем точки
    x[1] -= a * dY(x0)
    x[2] -= a * dZ(x0)
    if f0 <= F(x): #сраниваем старое значение функции с новым
        a = a / 2.0
    x0 = x
    count += 1

print(f"\nXmin = {x[0]:.8f}\nYmin = {x[1]:.8f}\nZmin = {x[2]:.8f}\nFmin: {F(x):.8f}\n\nКоличество шагов: {count}")