# Функция кнопок да/нет
def ans():
    while "Ответ неприемлем":
        reply = str(input(' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

# Программа отгадывания компьютером числа от 1 до 100, загаданного пользователем

import random
print("\n\tЭта программа будет угадывать число от 1 до 100, загаданное пользователем\n")
user_numb=int(input("Введите число от 1 до 100 \n"))
up=100
lw=1
cnt=0
guess=random.randint(lw,up)
while guess!=user_numb:
    cnt+=1
    print("Загаданное число больше ",guess, " ?")
    #answer=int(input("1=yes/2=no "))
    answer = ans()
    #if answer == 1:
    if answer == True:
        lw=guess+1
        guess=random.randint(lw,up)
    #elif answer == 2:
    elif answer == False:
        up=guess-1
        guess=random.randint(lw,up)
print ("\nЗагаданное число = ",guess )
print("\nКомпьютер отгадал число за ", cnt," попыток")