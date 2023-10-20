from sympy import *


def polinomial():
    fi_i = [0] * n
    for i in range(n):
        fi_i[i] = x**i
    return n, fi_i


def trigonometric():
    n = 4
    fi_i = [x**0, sin(x), cos(x), x]
    return n, fi_i


def solve_system(fi_i):
    linear_system = [0] * n

    for row in range(n):
        part_deriv = 0
        for j in range(m):
            func = f_i[j]
            for i in range(n):
                func -= fi_i[i].subs(x, x_i[j]) * c_i[i]
            part_deriv += diff(func**2, c_i[row])
        linear_system[row] = part_deriv

    solution = solve(linear_system, c_i,  dict=True)
    return solution


def draw_function(g_x, solution, F):
    plot(g_x.subs(solution[0]), F, (x, a-5, b+5), markers=[{'args': [x_i, f_i, "o"]}], legend=True)


if __name__ == '__main__':
    init_printing(use_unicode=False, wrap_line=False)
    x = Symbol('x')
    y = Symbol('y')

    F = sqrt(x)
    a = 0
    b = 9
    m = 15
    n = 4

    if (a > b):
        print ("Wrong limits")
        exit()

    n, fi_i = polinomial()
    # n, fi_i = trigonometric()

    x_i = [0] * m
    f_i = [0] * m
    c_i = symbols('c0:%d'%n)

    h = (b - a)/(m - 1)
    for i in range(m):
        x_i[i] = (i*h) + a
        f_i[i] = F.subs(x, x_i[i])

    print("Table:")
    print("x: ", x_i)
    print("y: ", f_i)

    solution = solve_system(fi_i)

    g_x = 0
    for i in range (n):
        g_x += c_i[i]*fi_i[i]
    print(g_x.subs(solution[0]))

    try:
        draw_function(g_x, solution, F)
    except:
        print("Can't draw graphs")
        exit()
