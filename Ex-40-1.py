# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

input = "AAAAAA888888888FDDCCCCCCC555555555A4444444444EEEEEEEEEEEEEEEEE"
output = ""

print("Исходная строка: ",input)
i = 0
while i < len(input):
    j = 1
    if i+j < len(input):
        while input[i] == input[i+j]:
            if j+i < len(input)-1:
                j += 1
            else:
                j += 1
                break
        output += str("{0:02d}".format(j)) + str(input[i])
        i += j
        
    else:
        output += str("{0:02d}".format(j)) + str(input[i])
        i += j
        break
print("После сжатия: ",output)
# запишем итоговую строку в файл
f = open("res_RLE.txt", "w")
f.write(output)
f.close
