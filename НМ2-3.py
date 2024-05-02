import numpy as np
x0 = [0, 0, 0]
def F(x):
    #return x[0]**2 + 4*x[0]*x[1] + 17*x[1]**2 + 5*x[1]
    return x[0] ** 2 + 5 * x[1] ** 2 + 8 * x[2] ** 2 - x[0] * x[1] + x[0] * x[2] - x[1] * x[2] + 5 * x[0] - 3 * x[1] + x[2]

x0[0] = float(input("Xo = "))
x0[1] = float(input("Yo = "))
x0[2] = float(input("Zo = "))
eps = float(input("Введите погрешность: eps = "))
alpha = float(input("Введите коэффициент отражения: alpha = "))
beta = float(input("Введите коэффициент сжатия: betta = "))
gamma = float(input("Введите коэффициент растяжения: gamma = "))

def nelder_mead(f, x0, alpha, beta, gamma, eps):
    count = 0
    x = np.array(x0)
    n = len(x)
    X = [x]
    for i in range(n):  #создаем массив с координатами точек типа [[0., 0.], [1., 0.], [0., 1.]]
        x_new = x.copy()
        x_new[i] += 1
        X.append(x_new)
    while np.linalg.norm(X[0] - X[-1]) >= eps: #условие выхода
        X.sort(key=lambda x: f(x)) #применятся функция f(x) к каждому элементу x в списке X и сортируется список X на основе результатов этой функции.
        x_c = np.mean(X[:-1], axis=0) # Центр масс. будет содержать среднее значение всех элементов массива X, за исключением последнего(он максимальный)
        # Отражение
        x_r = x_c + alpha * (x_c - X[-1]) #формула для отражения X[-1] - максимальный элемент
        X[-1] = x_r #избавляемся от максимума, в процессе сортировки эти точки уйдут в начало к минимальным
        if f(x_r) < f(X[0]): #Условие на расстяжение. Если условие выполняется, то отраженная точка x_r является лучшей точкой симплекса.
            # Растяжение
            x_e = x_c + gamma * (x_r - x_c) #формула для расстяжения
            if f(x_e) < f(x_r):
                X[-1] = x_e
            else:
                X[-1] = x_r
        else:
            # Сжатие
            x_s = x_c + beta * (X[-1] - x_c) #формула для сжатия
            if f(x_s) < f(X[-1]):
                X[-1] = x_s
            else:
                # Уменьшение
                for i in range(1, len(X)):  # перебираем все вершины симплекса, кроме лучшей точки
                    X[i] = 0.5 * (X[i] - X[0]) + X[0] #формула для уменьшения
        count += 1
    return X[0], f(X[0]), count
x, F_min, count = nelder_mead(F, x0,  alpha, beta, gamma, eps)
# Вывод результатов
print(f"\nXmin = {x[0]:.8f}\nYmin = {x[1]:.8f}\nZmin = {x[2]:.8f}\nFmin: {F_min:.8f}\n\nКоличество шагов: {count}")