arr = []
with open("Universal Data.txt", "r") as file:
    arr = file.read().splitlines()


#Iterative Bubble Sort
def iterative_bubble_sort(array):
    NoSwaps = False
    Pass = len(array) - 1

    while not NoSwaps:
        #if no swaps take place, exits the loop
        NoSwaps = True
        for x in range(Pass):
            if array[x] > array[x + 1]:
                temp = array[x]
                array[x] = array[x + 1]
                array[x + 1] = temp
                NoSwaps = False
        Pass = Pass - 1
    return array

#Recursive Bubble Sort
def recursive_bubble_sort(Array, NumberOfItems):
    if NumberOfItems == 1:
        return Array
    
    # Perform a single pass through the array
    for i in range(NumberOfItems - 1):
        if Array[i] > Array[i + 1]:
            Temp = Array[i]
            Array[i] = Array[i + 1]
            Array[i + 1] = Temp
    return Array
    
    # Recursively sort the remaining elements
    recursive_bubble_sort(Array, NumberOfItems - 1)



