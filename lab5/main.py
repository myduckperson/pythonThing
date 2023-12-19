import math
# first task
# first task
def findS():
    ok = False
    while not ok:
        side_1 = float(input("Введіть першу сторону прямокутника: "))
        side_2 = float(input("Введіть другу сторону прямокутника: "))
        if side_1 > 0 and side_2 > 0:
            ok = True
    return side_1*side_2
def task1():
    N = 4
    for itr in range(N,1):
        print(f"Введіть сторони {itr} прямокутника")
        print(f"Площа {itr} прямокутника ",findS())

# first task
# first task

# second task
# second task
def find_h():
    ok = False
    while not ok:
        side_1 = float(input("Введіть першу сторону прямокутного трикутника: "))
        side_2 = float(input("Введіть другу сторону прямокутного трикутника: "))
        if side_1 > 0 and side_2 > 0:
            ok = True
    return math.sqrt(side_1**2 + side_2**2)
def task2():
    print(f"Введіть сторони першого прямокутного трикутника")
    h_1 = find_h()
    print(f"Введіть сторони другого прямокутного трикутника")
    h_2 = find_h()
    print(f"Гіпотенуза першого трикутника: {h_1}, гіпотенуза {h_2}")
    if h_1 > h_2:
        print("Перша гіпотенуза більша!")
    elif h_1 < h_2:
        print("Друга гіпотенуза більша!")
    else:
        print("Гіпотенузи однакові!")
# second task
# second task

# third task
# third task
def is_inside(a, b, R):
    p1 = float(input("Введіть першу координату точки: "))
    p2 = float(input("Введіть другу координату точки: "))
    if (p1-a)**2 + (p2-b)**2 == R**2:
        print("Ваша точка входить в коло")
        return True
    else:
        print("Ваша точка не входить в коло")
        return False
def task3():
    a = float(input("Введіть 'а' з формули (x-a)^2 + (y-b)^2 == R^2 "))
    b = float(input("Введіть 'b' з формули (x-a)^2 + (y-b)^2 == R^2 "))
    R = float(input("Введіть 'R' з формули (x-a)^2 + (y-b)^2 == R^2 "))
    N = 4
    count = 0
    for itr in range(N,1):
        print(f"Введіть координати {itr} точки")
        if is_inside(a,b,R):
            count += 1
    print(f"Усього {count} точок входить в коло")
# third task
# third task

# fourth task
# fourth task
def find_silly_shape_area(X,Y,Z,T):
    area_1 = X*Y/2
    pseudo_side = math.sqrt(X ** 2 + Y ** 2)
    p = (pseudo_side + Z + Y)/2
    area_2 = math.sqrt(p*(p-pseudo_side)* (p-Z) * (p-T))
    return area_2+area_1
def task4():
    X = float(input("Введіть сторону X (X,Y,Z,T) довільного чотирикутника"))
    Y = float(input("Введіть сторону Y (X,Y,Z,T) довільного чотирикутника"))
    Z = float(input("Введіть сторону Z (X,Y,Z,T) довільного чотирикутника"))
    T = float(input("Введіть сторону T (X,Y,Z,T) довільного чотирикутника"))
    print("Площа чотирикутника: ", find_silly_shape_area(X, Y, Z, T))
# fourth task
# fourth task

# fifth task
# fifth task
def check_a_n(n_max,n):
    numbers = []
    acc = True
    for x in range(1,n_max):
        for y in n:
            if x % y != 0:
                acc = False
        if acc:
            numbers.append(x)
        acc = True
    return numbers
def task5():
    ok = False
    while not ok:
        n_max = int(input("Введіть натуральне n: "))
        amount_n = int(input("Введіть кількість ділених: "))
        n = []
        for itr in range(amount_n):
            temp = int(input("Введіть дільник: "))
            n.append(temp)
        if not n_max <= 0 and amount_n > 0:
            ok = True
    print("Результат: ",check_a_n(n_max, n))

# fifth task
# fifth task

# sixth task
# sixth task
def find_d_a(n):
    abs_n = abs(n)
    acc = 0
    for itr in range(1, abs_n):
        if abs_n % itr == 0:
            acc += 1
    return acc
def task6():
    ok = False
    while not ok:
        M = int(input("Введіть число М з інтервалу [M,N]"))
        N = int(input("Введіть число N з інтервалу [M,N]"))
        if N > M:
            ok = True
    acc = []
    final_max = 0
    div_max = 0
    for x in range(M,N+1):
        div_acc = find_d_a(x)
        acc.append(div_acc)
        if div_acc >= max(acc):
            final_max = x
            div_max = div_acc
    print("Число що має найбільшу кількість дільників в інтервалі [M,N]: ", final_max)
    print("Кількість його дільників: ", div_max)


# sixth task
# sixth task

# seventh task
# seventh task
# seventh task
# seventh task

# make a choice
ok = False
while not ok:
    task = int(input("Введіть номер завдання!"))
    if task == 0:
        ok = True
    elif task == 1:
        task1()
    elif task == 2:
        task2()
    elif task == 3:
        task3()
    elif task == 4:
        task4()
    elif task == 5:
        task5()
    elif task == 6:
        task6()
    elif task == 7:
        task7()
    elif task == 8:
        task8()