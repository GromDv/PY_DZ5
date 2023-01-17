# Модуль восстановления

# читаем файл
f1 = open("res_RLE.txt", "r")
in_rle = f1.readline()
f1.close

a = lambda x,y: int(str(x[y]) + str(x[y+1]))

print("Исходная строка: ",in_rle)
reinput = ""
for i in range(0,len(in_rle), 3):
    nums  = a(in_rle,i)
    for j in range(nums):
        reinput += in_rle[i+2]
print("После восстановления: ",reinput)