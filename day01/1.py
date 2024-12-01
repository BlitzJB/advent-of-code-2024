f = open("./day01/input.txt", "r")

list1, list2 = [], []

for line in f.readlines():
    list1.append(int(line.split('   ')[0]))
    list2.append(int(line.split('   ')[1]))

list1 = sorted(list1)
list2 = sorted(list2)

difference = 0

for i in range(len(list1)):
    difference += abs(list1[i] - list2[i])

print(difference)