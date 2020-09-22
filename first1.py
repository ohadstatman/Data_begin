import re

file = open("actual-data-1.txt")
lst=list()
for line in file:
    if re.search("[0-9]+",line):
        x = re.findall("[0-9]+",line)
    lst.append(x)
numbers =[]
for l in lst:
    for num in l:
        numbers.append(int(num))
print(sum(numbers))

l = [2,3,5,6]
for i in l:
    print(i)


