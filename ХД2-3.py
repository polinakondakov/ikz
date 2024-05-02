import numpy as np
def F(x, y, z):
    return x * x + 5 * y * y + 8 * z * z - x * y + x * z - y * z + 5 * x - 3 * y + z
    #return x*x + 4*x*y + 17*y*y + 5*y

print("Введите начальные приближения X, Y, Z (в случае если функция не зависит от Z, введите для Z - 0)")
x0 = float(input("Xo = "))
y0 = float(input("Yo = "))
z0 = float(input("Zo = "))
eps = float(input("Введите погрешность: eps = "))
d = float(input("Введите начальное значение вектора d = "))
count = 0
f0 = F(x0, y0, z0)

def search(x, y, z, f_n, d): #получение 4-6 точек путем вычитания и прибавления d
    if F(x + d, y, z) < f_n: #определяемся со значением x
        f_n = F(x + d, y, z)
        x += d
    elif F(x - d, y, z) < f_n:
        f_n = F(x - d, y, z)
        x -= d
    if F(x, y + d, z) < f_n: #определяемся со значением y
        f_n = F(x, y + d, z)
        y += d
    elif F(x, y - d, z) < f_n:
        f_n= F(x, y - d, z)
        y -= d
    if F(x, y, z + d) < f_n: #определяемся со значением z
        f_n = F(x, y, z + d)
        z += d
    elif F(x, y, z - d) < f_n:
        f_n = F(x, y, z - d)
        z -= d
    return x, y, z, f_n

while np.sqrt(2 * d ** 2) > eps: #условие выхода
    x, y, z, f_n = search(x0, y0, z0, f0, d) #определяем новые точки и значение функции по исследующему поиску
    if f_n >= f0: #если поиск по образцу не дал результатов уменьшаем d
        d /= 2
    elif f_n < f0: #если следущее значение меньше предыдущега, выполняем поиск по образцу
        f0 = f_n
        x_n = x + 2 * (x0 - x) # x - точка полученная из исследуещго поиска - базисная, x0 - предыдущая точка
        y_n = y + 2 * (y0 - y)
        z_n = z + 2 * (z0 - z)
        if F(x_n, y_n, z_n) < f_n: #если поиск по образцу дал результат
            x0, y0, z0 = x_n, y_n, z_n #принимаем новые точки
        else:
            x0, y0, z0 = x, y, z #если не дал - оставляем старые
        f_n = F(x0, y0, z0) #новое значение функции
    f0 = f_n #переопределяем предыдущее значение на новое текущее
    count += 1

print(f"\nXmin = {x0:.8f}\nYmin = {y0:.8f}\nZmin = {z0:.8f}\nFmin: {F(x0, y0, z0):.8f}\n\nКоличество шагов: {count}")

