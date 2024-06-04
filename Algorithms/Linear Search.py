arr = []
with open("Universal Data.txt", "r") as file:
    arr = file.read().splitlines()

#with loop
def linear_search_loop(Array, DataToFind):
    found = False
    for x in range(len(Array)):
        if Array[x] == DataToFind:
            found = True
    if found:
        return True
    else:
        return False

#without a loop
def linear_search(Array, DataToFind):
    found = False
    if DataToFind in Array[0:]:
        found = True
    return found
print(arr)
print(linear_search_loop(arr, 2))