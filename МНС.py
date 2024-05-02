import math
x0 = [0, 0, 0]
x = [0, 0, 0]
def F(x):
    #return x[0]**2 + 4*x[0]*x[1] + 17*x[1]**2 + 5*x[1]
    return x[0]**2 + 5*x[1]**2 + 8*x[2]**2 - x[0]*x[1] + x[0]*x[2] - x[1]*x[2] + 5*x[0] - 3*x[1] + x[2]
def dX(x):
    #return 2*x[0] + 4*x[1]
    return 2*x[0] - x[1] + x[2] + 5
def dY(x):
    #return 4*x[0] + 34*x[1] + 5
    return 10*x[1] - x[0] - x[2] - 3
def dZ(x):
    #return 0
    return 16*x[2] + x[0] - x[1] + 1
def normVector(x, y ,z):
    return math.sqrt(x**2 + y**2 + z**2)

print("Введите начальные приближения X, Y, Z (в случае если функция не зависит от Z, введите для Z любое число)")
x[0] = float(input("Xo = "))
x[1] = float(input("Yo = "))
x[2] = float(input("Zo = "))
eps = float(input("Введите погрешность: eps = "))
count = 0
def min(f): #метод деления отрезка пополам
    a = 0
    b = 1
    for i in range(1, 100):
        x1 = (a + b - 0.01) / 2
        x2 = (a + b + 0.01) / 2
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
    return (a + b) / 2
def F1(t0): #функция, у которой ищется минимум
    return (x[0] - t0*dX(x))**2 + 4*(x[0] - t0*dX(x))*(x[1] - t0*dY(x)) + 17*(x[1] - t0*dY(x))**2 + 5*(x[1] - t0*dY(x))
    #return (x[0] - t0 * dX(x)) ** 2 + 5 * (x[1] - t0 * dY(x)) ** 2 + 8 * (x[0] - t0 * dZ(x)) ** 2 - (x[0] - t0 * dX(x)) * (x[1] - t0 * dY(x)) + (x[2] - t0 * dZ(x)) * (x[0] - t0 * dX(x)) - (x[1] - t0 * dY(x)) * (x[2] - t0 * dZ(x)) + 5 * (x[0] - t0 * dX(x)) - 3 * (x[1] - t0 * dY(x)) + (x[2] - t0 * dZ(x))
t0 = 1
while normVector(dX(x), dY(x), dZ(x)) >= eps: #условие выхода
    x[0] -= t0 * dX(x) #находятся новые x
    x[1] -= t0 * dY(x)
    x[2] -= t0 * dZ(x)
    t0 = min(F1) #находится новый параметр альфа
    count += 1

print(f"\nXmin = {x[0]:.8f}\nYmin = {x[1]:.8f}\nZmin = {x[2]:.8f}\nFmin: {F(x):.8f}\n\nКоличество шагов: {count}")


