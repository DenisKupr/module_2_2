    ### Условная конструкция. Операторы if, elif, else. ###

first = int(input('Число №1 - '))
second = int(input('Число №2 - '))
third = int(input('Число №3 - '))

if first == second !=third or second == third != first or first == third != second:
    print(2)   # Если частичное совподение

elif first != second != third:
    print(0)    # Если все числа не равны

elif first == second == third:
    print(3)    # Если все числа равны