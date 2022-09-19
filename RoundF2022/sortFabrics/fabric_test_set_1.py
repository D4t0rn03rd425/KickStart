import collections

t = int(input())

for i in range(t):
    n = int(input())
    
    fabrics = []
    for j in range(n):
        fabrics.append(input())

    doubleList = []
    for j in range(len(fabrics)):
        doubleList.append(fabrics[j].split(' '))

    sortedDoubleList = sorted(doubleList, key=lambda x: int(x[2]))

    # Ada
    adaDoubleList = sorted(sortedDoubleList, key=lambda x: x[0])

    # Charles
    charlesDoubleList = sorted(sortedDoubleList, key=lambda x: x[1])

    k = 0

    for j in range(len(doubleList)):
        if adaDoubleList[j] == charlesDoubleList[j]:
            k += 1    

    print(f"Case #{i + 1}: {k}")