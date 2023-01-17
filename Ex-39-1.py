# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

import random

spr3 = lambda nums,max: max-1 if nums%max==0 else nums%max - 1
spr2 = lambda nums,max: random.randint(1,max) if nums%max==1 else spr3(nums,max)
spr = lambda nums,max: spr2(nums,max) if nums > max else nums

esc = lambda code: f'\033[{code}m'

def numsWord(nums):
    if nums > 10 and nums < 20 :
        return 'конфет'
    elif nums == 1 or nums%10 == 1:
        return 'конфета'
    elif nums > 1 and nums < 5 or nums%10 > 1 and nums%10 < 5:
        return 'конфеты'
    else :
        return 'конфет'

vsego = 221
maxHod = 28

print()
print(esc('32') + 'На столе лежит {} {}. Играют два игрока делая ход друг за другом. Первый ход определяется случайно. За один ход можно забрать не более чем {} {}. Все конфеты оппонента достаются сделавшему последний ход.'.format(vsego, numsWord(vsego), maxHod, numsWord(maxHod)) + esc(0))


nc = lambda x: x if x != '' else '1'

while True:
    print()
    typePlaer = int(nc(input('С кем будете играть? (1 - с другом, 2 - с глупым ботом, 3 - с умным ботом, 4 - закончить игру): ')))

    vsego = 221
    maxHod = 28
    player = random.randint(1,2)

    if typePlaer == 4:
        break

    if typePlaer == 1:
        print(esc('31')+'Начинает игрок №{}!'.format(player)+esc('0'))
        while vsego > 0:
            n = int(nc(input('Игрок {}, На столе {} {}. Сколько хотите взять? (от 1 до {} {}): '.format(player, vsego, numsWord(vsego), maxHod, numsWord(maxHod)))))
            if n > maxHod:
                print('Можно брать не более {}, попробуйте снова!'.format(maxHod))
                continue
            if vsego >= n:
                vsego -= n
            else:
                print('Есть только {}, попробуйте снова!'.format(vsego))
                continue

            if vsego > 0:
                if player == 1:
                    player = 2
                else:
                    player = 1
            
        print(esc('31') + 'Выиграл игрок №{}'.format(player) + esc('0'))

    elif typePlaer == 2:
        if player == 1:
            print(esc('31')+'Начинаете вы!'+esc('0'))
        else:
            print(esc('31')+'Начинает бот!'+esc('0'))
        while vsego > 0:
            if player == 1:
                n = int(nc(input('Ваш ход. На столе {} {}. Сколько хотите взять? (от 1 до {}): '.format(vsego,numsWord(vsego), maxHod))))
                if n > maxHod:
                    print('Можно брать не более {}, попробуйте снова!'.format(maxHod))
                    continue
                if vsego >= n:
                    vsego -= n
                else:
                    print('Есть только {}, попробуйте снова!'.format(vsego))
                    continue
                
            if vsego > 0:
                player = 2
                if vsego >= maxHod:
                    n_bot = random.randint(1,maxHod)
                else:
                    n_bot = random.randint(1,vsego)
                vsego -= n_bot
                print('Бот взял {} {}.'.format(n_bot,numsWord(n_bot)))
                if vsego == 0: break
                player = 1

        if player == 1:
            print(esc('31')+'Вы выиграли!'+esc('0'))
        else:
            print(esc('33')+'Вы проиграли!'+esc('0'))

    elif typePlaer == 3:
        if player == 1:
            print(esc('31')+'Начинаете вы!'+esc('0'))
        else:
            print(esc('31')+'Начинает бот!'+esc('0'))
        
        while vsego > 0:
            if player == 1:
                # print('Подсказка: если хотите выиграть, надо взять {}'.format(spr(vsego, maxHod)))
                n = int(nc(input('Ваш ход. На столе {} {}. Сколько хотите взять? (от 1 до {}): '.format(vsego,numsWord(vsego),maxHod))))
                if n > maxHod:
                    print('Можно брать не более {}, попробуйте снова!'.format(maxHod))
                    continue
                if vsego >= n:
                    vsego -= n
                else:
                    print('Есть только {}, попробуйте снова!'.format(vsego))
                    continue

            if vsego > 0:
                player = 2
                n_bot = spr(vsego, maxHod)

                print('На столе {} {}. Бот взял {}.'.format(vsego,numsWord(vsego), n_bot))
                vsego -= n_bot
                if vsego == 0: break
                player = 1

        if player == 1:
            print(esc('31')+'Вы выиграли!'+esc('0'))
        else:
            print(esc('31')+'Вы проиграли!'+esc('0'))