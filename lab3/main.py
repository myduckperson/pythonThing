
# first task
# first task
def task1():
    the_string = input("Введіть рядок тексту")
    acc = 0
    ok = False
    while not ok:
        the_letter = input("Введіть букву")
        if len(the_letter) == 1:
            ok = True
    split_string = the_string.split()
    for word in split_string:
        if word[0] == the_letter:
            acc+=1
    print(f"Кількість слів в вашому тексті, що починаються на {the_letter}: ", acc)

# first task
# first task

# second task
# second task
def task2():
    the_string = input("Введіть ваш текст")
    acc = 0
    for symbol in the_string:
        if symbol == ":":
            acc += 1
    the_string.replace(":","%")
    print("Видозмінений текст: ", the_string)
    print("Кількість замін : => %: ", acc)

# second task
# second task

# third task
# third task
def task3():
    the_string = input("Введіть ваш текст")
    acc = 0
    for symbol in the_string:
        if symbol == ".":
            acc += 1
    the_string.replace(".","")
    print("Видозмінений текст: ", the_string)
    print("Кількість видалень крапки: ", acc)
# third task
# third task

# fourth task
# fourth task
def task4():
    the_string = input("Введіть ваш текст")
    acc = 0
    for symbol in the_string:
        if symbol == "a":
            acc += 1
    the_string.replace("a","о")
    print("Видозмінений текст: ", the_string)
    print("Кількість замін а => о ", acc)
    print("Кількість символів в тексті: ", len(the_string))
# fourth task
# fourth task

# fifth task
# fifth task
def task5():
    the_string = input("Введіть ваш текст")
    print("Ваш текст з заміненими великими літерами на малі",the_string.lower())
# fifth task
# fifth task

# sixth task
# sixth task
def task6():
    the_string = input("Введіть ваш текст")
    acc = 0
    for symbol in the_string:
        if symbol == "о":
            acc += 1
    the_string.replace("о","")
    print("Видозмінений текст: ", the_string)
    print("Кількість видалених 'o' ", acc)
# sixth task
# sixth task

# seventh task
# seventh task
def task7():
    the_string = input("Введіть ваш текст")
    the_middle = len(the_string)//2
    f_half_string = the_string[:the_middle]
    f_half_string.replace("п", "*")
    the_result = f_half_string + the_string[the_middle:]
    print("Видозмінений текст: ", the_result)
# seventh task
# seventh task

# eighth task
# eighth task
def task8():
    the_string = input("Введіть ваш текст")
    the_word = input("Введіть ваше слово")
    acc = (the_string.split()).count(the_word)
    print("Кількість заданих вами слів у вашому тексті: ", acc)
# eighth task
# eighth task

# ninth task
# ninth task
def task9():
    the_string = input("Введіть текст на англійській мові")
    print("Видозмінений текст : ", the_string.title())
# ninth task
# ninth task

# tenth task
# tenth task
def task10():
    the_string = input("Введіть текст на англійській мові")
    the_N_letter = input("Введіть вашу першу обрану букву")
    the_P_letter = input("Введіть вашу другу обрану букву")
    the_result = ""
    for word in the_string.split():
        if word[0] == the_N_letter and word[len(word)-1] == the_P_letter:
            the_result += " " + word
    print(f"Усі слова, що починаються на {the_N_letter} та закінчуються на {the_P_letter} у вашому тексті : ",the_result)
# tenth task
# tenth task


# eleventh task
# eleventh task
def task11():
    the_string = input("Введіть текст на англійській мові")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    acc = 0
    for letter in the_string:
        if letter in vowels:
            acc += 1
    print("Кількість голосних літер у вашому тексті: ", acc)
# eleventh task
# eleventh task

# twelfth task
# twelfth task
def task12():
    the_string = input("Введіть текст на англійській мові")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    acc = 0
    for letter in the_string:
        if not letter in vowels:
            acc += 1
    print("Кількість голосних літер у вашому тексті: ", acc)

# twelfth task
# twelfth task

# thirteenth task
# thirteenth task
def task13():
    the_string = input("Введіть текст на англійській мові")
    consonants_l = "bcdfghjklmnpqrstvwxyz"
    consonants = consonants_l + consonants_l.upper()
    acc = 0
    for letter in the_string:
        if letter in consonants:
            acc += 1
    print("Кількість приголосних літер у вашому тексті: ", acc)

# thirteenth task
# thirteenth task

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
