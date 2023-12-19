# first task
# first task
import math
import random


def task1():
    ok = False
    while not ok:
        N = int(input("Введіть число N"))
        if N > 0:
            ok = True
    list = []
    for itr in range(N):
        list.append(int(input(f"Введіть число під індексом [{itr}]: ")))
    print(f"Максимальний елемент: {max(list)}")
    list.reverse()
    print("Список в зворотньому порядку: ", list)
# first task
# first task

# second task
# second task
def task2():
    ok = False
    while not ok:
        N = int(input("Введіть число N"))
        if N > 0:
            ok = True
    list = []
    for itr in range(N):
        list.append(int(input(f"Введіть число під індексом [{itr}]: ")))
    pos_list = []
    nig_list = []
    for n in list:
        if  n >0:
            pos_list.append(n)
        else:
            nig_list.append(n)
    print("Ваш лист: ", list)
    print("Позитивний лист (без негативу): ", pos_list)
    print("Негативний лист: ", nig_list)
# second task
# second task

# third task
# third task
def task3():
    N = 20
    for itr in range(N):
        list.append(int(input(f"Введіть число під індексом (всього 20 чисел) [{itr}]: ")))

    print(f"Сума елементів з непарними індексами: {sum(list[1::2])}")
    print("Список з непарних індексів: ", list[1::2])
# third task
# third task

# fourth task
# fourth task
def task4():
    N = 30
    list = []
    for itr in range(N):
        list.append(random.randrange(-100,101))
    print("Максимальний елемент списку та його порядковий номер: ", max(list), list.index(max(list)))
    odd_list = []
    for n in list:
        if not n % 2 == 0:
            odd_list.append(n)
    if not odd_list:
        print("В початковому списку немає непарних чисел")
    else:
        print("Список непарних чисел з початковго списку в порядку зменшення елементів: ", odd_list.sort(reverse=True))

# fourth task
# fourth task

# fifth task
# fifth task
def task5():
    N = 30
    list = []
    for itr in range(N):
        list.append(random.randrange(-100,101))
    pair_of_nig = []
    itr=0
    for n in list:
        if not itr == 0 and n < 0 and (list[itr+1] < 0 or list[itr-1] < 0):
            pair_of_nig.append(n)
        itr += 1
    print("Початковий список: ", list)
    print("Список пар від'ємних чисел, що стоять поруч: ", pair_of_nig)
# fifth task
# fifth task

# sixth task
# sixth task
def task6():
    N = 10
    for itr in range(N):
        list.append(int(input(f"Введіть число під індексом (всього 10 чисел) [{itr}]: ")))
    max_element_for_the_h = max(list)
    max_element_for_the_o_rooted = math.sqrt(max(list))
    list.append(math.sqrt(max(list)))
    list.pop(list.index(max(list)))
    max_element_for_the_e_compared = max(list)
    new_list = []
    for n in list:
        if n**2 < max_element_for_the_o_rooted:
            new_list.append(n**2)
    new_list.sort(reverse=True)
    print("Максимальний елемент вхідного списку: ", max_element_for_the_h)
    print("Новий максимум, після заміни максимуму на його корінь: ", max_element_for_the_e_compared)
    print("Список квадратів менших чисел: ", new_list)
# sixth task
# sixth task

# seventh task
# seventh task
def task7():
    N = 30
    list = []
    for itr in range(N):
        list.append(random.randrange(-100,101))
    print("Мінімальний по модулю елемент списку: ", abs(min(list, key=abs)))
    print("Список в порядку збільшення значення: ", list.sort())
# seventh task
# seventh task

# eighth task
# eighth task
def sortF(list):
    return
def task8():
    N = 30
    list = []
    for itr in range(N):
        list.append(random.randrange(-100,101))
    sub_lists = []
    for itr in range(10):
        temp_list = []
        for sub_itr in range(3):
            temp_list.append(list[itr*3 + sub_itr])
        sub_lists.append(temp_list)
    sub_lists.sort(key=lambda list: sum( [abs(ele) for ele in list]))
    print("Отримані списки в порядку зростання за сумою абсолютних значень окремих елементів: ", sub_lists)
# eighth task
# eighth task

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