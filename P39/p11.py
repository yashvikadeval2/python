# 11. Find common elements between two lists.

l = [10, 20, 30, 40, 50]
l1 = [30, 40, 60, 70, 80]

for i in l:
    for j in l1:
        if i == j:
           print(i)
