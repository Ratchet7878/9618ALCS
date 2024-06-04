def IterativeVowels(Value):
    total = 0
    lengthstring = len(Value)

    for x in range(0, lengthstring):
        firstcharacter = Value[0:1]
        if firstcharacter == "a" or firstcharacter == "e" or firstcharacter == "i" or firstcharacter == "o" or firstcharacter == "u":
            total = total + 1
        Value = Value[1:lengthstring]
    return total

x = IterativeVowels("house")
print(x)

def RecursiveVowels(Value):
    lengthstring = len(Value)
    if lengthstring == 0:
        return 0
    firstcharacter = Value[0]
    if firstcharacter == "a" or firstcharacter == "e" or firstcharacter == "i" or firstcharacter == "o" or firstcharacter == "u":
        return 1 + RecursiveVowels(Value[1:len(Value)])
    else:
        return RecursiveVowels(Value[1:len(Value)])

y = RecursiveVowels("imagine")
print(y)