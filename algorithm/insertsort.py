def insert_sort(numbs):
    for i in range(len(numbs)):
        for j in range(i - 1, -1, - 1):
            if numbs[j] > numbs[j + 1]:
                numbs[j], numbs[j + 1] = numbs[j + 1], numbs[j]

    return numbs


def Insert(numbs):
    for i in range(len(numbs)):
        for j in range(i - 1, -1, -1):
            if numbs[j] > numbs[j + 1]:
                numbs[j], numbs[j + 1] = numbs[j + 1], numbs[j]

    return numbs
