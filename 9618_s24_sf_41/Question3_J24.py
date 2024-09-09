QueueData = ['' for x in range(20)]
QueueHead = -1
QueueTail = -1

def Enqueue(DataToAdd):
    global QueueData, QueueHead, QueueTail
    QueueSize = len(QueueData)
    if QueueTail < QueueSize - 1:
        QueueTail += 1
        QueueData[QueueTail] = DataToAdd
        if QueueTail == 0:
            QueueHead += 1
        return True
    else:
        return False

def Dequeue():
    global QueueData, QueueHead, QueueTail
    if QueueHead == -1:
        return "false"
    else:
        DequeuedData = QueueData[QueueHead]
        QueueHead += 1
        return DequeuedData

def StoreItems():
    global QueueData, QueueHead, QueueTail
    incorrect_inp = 0
    ctd = "yes"
    while ctd == "yes":
        user_digit = input("Enter the 7 character string: ")
        temp_array = []
        sum = 0
        
        for x in range(0,6):
            if x % 2 == 0:
                temp = int(user_digit[x]) * 1
                temp_array.append(temp)
            else:
                temp = int(user_digit[x]) * 3
                temp_array.append(temp)
        for items in temp_array:
            sum = sum + items
        check_digit = str(sum // 10)
        if check_digit == "10":
            check_digit = "X"
        if check_digit == user_digit[6]:
            Enqueue(str(user_digit))
        else:
            print("Check digit error")
            incorrect_inp += 1
        ctd = input('To continue type "yes": ')
    print("No. of check-digit errors: ", incorrect_inp)

StoreItems()
print(Dequeue())