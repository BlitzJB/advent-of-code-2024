f = open("./day01/input.txt", "r")

list1, list2 = [], []

for line in f.readlines():
    list1.append(int(line.split('   ')[0]))
    list2.append(int(line.split('   ')[1]))

counts = {}

for num in list2:
    counts[num] = counts.get(num, 0) + 1

similarity = 0

for num in list1:
    if num in counts:
        similarity += num * counts[num]

print(similarity)