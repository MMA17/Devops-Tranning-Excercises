import random

list1 = []
list2 = []
i = 100
while i > 0:
    list1.append(random.randint(1,100))
    i-=1
print(list1)

for x in list1:
    if x >= 10:
        continue
    elif x % 2 == 0:
        list2.append("chẵn")
    elif x % 2 == 1:
        list2.append("lẻ")
    else:
        continue

print (list2)
