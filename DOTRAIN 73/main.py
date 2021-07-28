read = open("context.txt", "rt")
list = read.read().split()
read.close()
listMin = []

#loc ra cac tu khong trung lap luu vao listMin
l = len(list)
i = 0
while i < l:
    check = 1
    for x in listMin:
        if str(list[i]) == str(x):
            check = 0
        if check == 0:
            break
    if check == 1:
        listMin.append(list[i])
    i+=1
#print(listMin)

# Dem so lan xuat hien cua moi tu trong listMin
wr = open("out.txt", "w")
for x in listMin:
    count = 0
    for y in list:
        if x == y:
            count+=1
    wr.write(x + ":" + str(count) + "\n")

wr.close()