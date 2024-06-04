def Unknown(x, y):
    if x < y:
        print(x + y)
        return (Unknown(x + 1, y) * 2)
    elif x == y:
        return 1 # base case case
    else:
        print(x + y)
        return (Unknown(x - 1, y) // 2)

y = Unknown(10, 15)
print(y)


def IterativeUnknown(x, y):
    result = 1
    if x == y:
        return result
    else:
        while x != y:
            if x < y:
                print(x + y)
                x = x + 1
                result = result * 2
            else:
                print(x + y)
                x = x - 1
                result = result // 2
        return result


print("Iterative func")
print(str(IterativeUnknown(10, 15)))
