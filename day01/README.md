# Day 1: Historian Hysteria

## Problem Description

The challenge involves processing two lists of location IDs to help the Elvish Senior Historians find the Chief Historian. Two computational tasks were presented:
1. Calculate the total distance between sorted lists of location IDs
2. Compute a similarity score based on occurrence frequencies of list elements

## Approach

### Part 1: Distance Calculation
```python
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
```
- Read input file and split each line into two lists
- Sort both lists to enable pair-wise distance calculation
- Iterate through sorted lists and calculate absolute difference between corresponding elements
- Sum these differences to get total distance

### Part 2: Similarity Score Calculation
```python
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
```
- Read input file and split each line into two lists
- Create a frequency dictionary for the right-side list
- Calculate similarity score by multiplying each left-side number with its frequency in the right-side list

## Notes

- Input parsing required careful handling of three-space separated values
- Sorting was crucial for accurate distance calculation
- Frequency counting method allows efficient similarity score computation
- Solutions leverage Python's dictionary and list manipulation capabilities

## Performance

- Part 1: 1.72 ms
- Part 2: 1.59 ms