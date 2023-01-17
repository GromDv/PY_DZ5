# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

input = 'фывабвщшг лорпабворпо орпора ячсабвнгш йцушгплоп'
toRemove = 'абв'

print("Входящий текст: {}".format(input))
input = input.split(' ')
output = " ".join(list(filter(lambda wd: not(toRemove in wd), input)))
print("После удаления: {}".format(output))