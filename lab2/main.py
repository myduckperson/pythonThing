# first task
# first task
import math


def task1():
    n_1 = int(input("Введіть перше ціле число"))
    n_2 = int(input("Введіть друге ціле число"))
    n_3 = int(input("Введіть третє ціле число"))

    if n_1>=1 and n_1 <= 3 :
        print("Перше число входиться в інтервал [1,3]")
    elif n_2>=1 and n_2 <= 3 :
        print("Друге число входиться в інтервал [1,3]")
    elif n_3>=1 and n_3 <= 3 :
        print("третє число входиться в інтервал [1,3]")
# first task
# first task

# second task
# second task
def task2():
    ok = False
    while not ok:
        year_n = int(input("Введіть рік: "))
        if year_n>0:
            ok = True
    if year_n%4 == 0 and (year_n%400 == 0 or year_n%100 != 0):
        print("Ваш рік високосний")
    else:
        print("Ваш рік не є високосним")
# second task
# second task

# third task
# third task
def task3():
    ok = False
    while not ok:
        money = int(input("Введіть суму покупки для обчислення знижки"))
        if money>0:
            ok=True
    if money>500:
        money -= (money/100)*3
    elif money>1000:
        money -= (money/100)*5
    print("Фінальна ціна зі знижкою: ", money)
# third task
# third task

# fourth task
# fourth task
def task4():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    d = float(input("Введіть четверте число: "))
    print(f"Косинус мінімального ({min(a,b,c,d)}) числа: ", math.cos(min(a,b,c,d)))
# fourth task
# fourth task

# fifth task
# fifth task
def task5():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    print(f"Синус максимального ({max(a,b,c)}) числа: ", math.sin(max(a,b,c)))
# fifth task
# fifth task

# sixth task
# sixth task
def task6():
    ok = False
    while not ok:
        a = float(input("Введіть першу (рівносторонню) сторону рівнобедреного трикутника"))
        b = float(input("Введіть другу (рівносторонню) сторону рівнобедреного трикутника"))
        c = float(input("Введіть третю (основу) сторону рівнобедреного трикутника"))
        if a + b > c and a + c > b and b + c > a and a == b and a > 0 and b > 0 and c > 0:
            ok = True
    p_small = (a+b+c)/2
    area = math.sqrt(p_small * (p_small-a) * (p_small - b) * (p_small -c))
    if area%2 == 0:
        print("Площа парна, поділено на 2, результат: ", area/2)
    else:
        print("Площа не парна, не можу поділити на два, площа: ", area)
# sixth task
# sixth task


# seventh task
# seventh task
def task7():
    ok = False
    while not ok:
        monthN = int(input("Введіть номер місяця"))
        if monthN>0 and monthN<13:
            ok = True
        else:
            print("спробуйте ще!")
    if monthN == 1:
        print("January")
    elif monthN == 2:
        print("February")
    elif monthN == 3:
        print("March")
    elif monthN == 4:
        print("April")
    elif monthN == 5:
        print("May")
    elif monthN == 6:
        print("June")
    elif monthN == 7:
        print("July")
    elif monthN == 8:
        print("August")
    elif monthN == 9:
        print("September")
    elif monthN == 10:
        print("October")
    elif monthN == 11:
        print("November")
    elif monthN == 12:
        print("December")
# seventh task
# seventh task

# eighth task
# eighth task
def task8():
    a = float(input("Введіть перше число"))
    b = float(input("Введіть друге число"))
    c = float(input("Введіть третє число"))
    arr = [a, b, c]
    pN = 0
    for number in arr:
        if number>0:
           pN+= 1
    print("Кількість позитивних чисел", pN)
# eighth task
# eighth task

# ninth task
# ninth task
def task9():
    ok = False
    while not ok:
        A = float(input("Введіть А (А<B)"))
        B = float(input("Введіть B (А<B)"))
        if A < B:
            ok = True
    lmao = range(int(A),int(B))
    acc = 0
    for n in lmao:
        acc += n
    print("Сума всіх цілих чисел від А до В", acc)

# ninth task
# ninth task

# tenth task
# tenth task
def task10():
    ok = False
    while not ok:
        A = float(input("Введіть А (А<B)"))
        B = float(input("Введіть B (А<B)"))
        if A < B:
            ok = True
    lmao = range(int(A),int(B))
    acc = 0
    for n in lmao:
        acc += n**2
    print("Сума всіх квадратів цілих чисел від А до В", acc)
# tenth task
# tenth task

# eleventh task
# eleventh task
def task11():
    ok = False
    while not ok:
        A = float(input("Введіть А (А<B)"))
        B = float(input("Введіть B (А<B)"))
        if A < B and A <= 200:
            ok = True
    lmao = range(int(A),int(B))
    acc = 0
    for n in lmao:
        acc += n

    print("Cереднє арифметичне всіх цілих чисел від a до b", acc/len(lmao))
# eleventh task
# eleventh task

# twelfth task
# twelfth task
def task12():
    ok = False
    while not ok:
        A = float(input("Введіть А (А<=B)"))
        B = float(input("Введіть B (А<=B)"))
        if A <= B:
            ok = True
    # lmao = range(int(A),int(B))
    acc = 0
    ok = int(A)
    while not ok == int(B):
        acc += ok
        ok+=1

# twelfth task
# twelfth task

# thirteenth task
# thirteenth task
def task13():
    ok = False
    while not ok:
        A = int(input("Введіть А (0<=А<=50)"))
        if A <= 50 and 0 <= A:
            ok = True
    lmao = range(A, 50)
    sum = 0
    for n in lmao:
        sum += n**2
    print("Сума квадратів усіх ціл від А до 50 = ",  sum)

# thirteenth task
# thirteenth task

# fourteenth task
# fourteenth task
def task14():
    ok = False
    while not ok:
        N = int(input("Введіть ціле число більше за 1"))
        if N > 1:
            ok = True
    K = 1
    while not K**5>N:
        K+=1
    print("Найменше ціле число, при якому виконується нерівність 5^K>N", K)
# fourteenth task
# fourteenth task

# fifteenth task
# fifteenth task
def task15():
    n = float(input("Введіть число n"))
    very_big_number = 999999
    for number in range(very_big_number):
        if number**2 > n:
            print("Перше, більше за n, число серед 1,4,9,16,25,...", number**2)
            break

# fifteenth task
# fifteenth task

# sixteenth task
# sixteenth task
def task16():
    n = float(input("Введіть число n"))
    acc = 1
    inc = 1
    while not acc > n:
        inc += 1
        acc+= inc*2-1
#       1*2 -1 = 1, 2*2 -1 =3 ...
    print("Перше, більше за n, число серед 1,2,5,10,17,26")

# sixteenth task
# sixteenth task

# make a choice
ok = False
while not ok:
    task = int(input("Введіть номер завдання!"))
    if task == 0:
        ok = True
    elif task == 2:
        task2()
    elif task == 7:
        task7()
    elif task == 8:
        task8()
    elif task == 9:
        task9()
    elif task == 10:
        task10()
    elif task == 11:
        task11()
    elif task == 12:
        task12()
    elif task == 13:
        task13()
    elif task == 14:
        task7()
    elif task == 15:
        task7()
    elif task == 16:
        task7()