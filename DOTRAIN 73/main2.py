read = open("context.txt", "rt")
list = read.read().split()
list.sort()
l = len(list)
read.close()
wr = open("out.txt", "w")
#print (list)
i = 0
count = 1
while i < l-1:
    if list[i] != list[i+1]:
        wr.write(str(list[i])+ ": " + str(count) + "\n")
        count = 1
    else: 
        count+=1
    i+=1
