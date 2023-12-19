# first task
a = int(input("Введіть ціле число: "))
b = int(input("Введіть ціле число: "))
c = float(input("Введіть десятковий дріб: "))
d = float(input("Введіть десятковий дріб: "))

# second task
action_1 = a + b
action_2 = c - d
action_3 = b * c
action_4 = d / a
action_5 = a ** c
action_6 = b // d
action_7 = d % b

list = [action_1, action_2, action_3, action_4, action_5, action_6, action_7]
print("Список з результатами: ", list)

# third task

print("Кількість елементів списку: ", len(list))
print("Список парних елементів: ", list[1::2])

# fourth task

temp = list[1]
list[1] = list[4]
list[4] = temp
print("Змінений список: ", list)

# fifth task
name = input("Введіть ім'я: ")
group = input("Введіть групу: ")
print(f"Лабораторну роботу номер 1 виконав {name}, студент групи {group}. \n Висновок на даній роботі було")
print("проведено повторення та\n ознайомлення з основами мови програмування Python.")
print("Виковано 'базові дії над операторами та функція даної\nмови програумванн.\nРоботу виконано в повному обсязі")

