Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

def SortDescending():

    global Animals

    ArrayLength = len(Animals)

    for x in range(0, ArrayLength):
        for y in range(0, (ArrayLength - x - 1)):
            if Animals[y][0] < Animals[y + 1][0]:
                temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = temp

SortDescending()
for x in range(10):
    print(Animals[x])
