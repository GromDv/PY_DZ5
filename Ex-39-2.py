# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

import random

size = 4
array = [['.'] * size for i in range(size)]
array[0][0] = ' '
array[1][0] = 'a'
array[2][0] = 'b'
array[3][0] = 'c'
array[0][1] = '1'
array[0][2] = '2'
array[0][3] = '3'

pl = lambda x: 2 if x == 1 else 1
cGreen = lambda y: esc('32')+y+esc('0')
cRed = lambda y: esc('31')+y+esc('0')
cYel = lambda y: esc('33')+y+esc('0')

def print_scr():
    print()
    for i in array:
        print(cYel(' '.join(list(map(str, i)))))
    print()

esc = lambda code: f'\033[{code}m'

def NumFromABC(a):
    if a == 'a':
        return 1
    elif a == 'b':
        return 2
    else:
        return 3

def CheckWin():
    global array
    if array[1][1] == array[2][2] == array[3][3] and array[2][2] != '.':
        return True
    elif array[3][1] == array[2][2] == array[1][3] and array[2][2] != '.':
        return True
    elif array[1][1] == array[1][2] == array[1][3] and array[1][2] != '.':
        return True
    elif array[2][1] == array[2][2] == array[2][3] and array[2][2] != '.':
        return True
    elif array[3][1] == array[3][2] == array[3][3] and array[3][2] != '.':
        return True
    elif array[1][1] == array[2][1] == array[3][1] and array[2][1] != '.':
        return True
    elif array[1][2] == array[2][2] == array[3][2] and array[2][2] != '.':
        return True
    elif array[1][3] == array[2][3] == array[3][3] and array[2][3] != '.':
        return True
    else:
        return False

def CheckEnd():
    global array
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '.':
                return False
    return True

player = random.randint(1,2)
print()
print(cGreen('Игра "Крестики-Нолики". Играют два игрока. Кто начинает - определяется случайно. Первый игрок играет Х, второй - 0.'))

print_scr()

while True:
    turn = input('Играет игрок №{}. Укажите желаемое поле в виде a1,b3 и т.д. : '.format(player))
    if array[NumFromABC(turn[0])][int(turn[1])] != '.':
        print(cRed('Это поле занято! Попробуйте иначе!'))
        continue
    if player == 1:
        array[NumFromABC(turn[0])][int(turn[1])] = 'X'
    else:
        array[NumFromABC(turn[0])][int(turn[1])] = '0'
    print_scr()
    if(CheckWin()):
        print(cRed('Выиграл игрок №{}'.format(player)))
        break
    if(CheckEnd()):
        print(cRed('Ничья!'+esc('0')))
        break
    player = pl(player)