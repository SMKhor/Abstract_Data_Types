Groups = ["","",""]

NumberInQueue = 0
HeadIndex = 0
TailIndex = 0

def Enqueue(DataToInsert):
    global Groups, HeadIndex, TailIndex, NumberInQueue
    if NumberInQueue == 3:
        return print("Queue is full")
    else:
        Groups[TailIndex] = DataToInsert
        TailIndex += 1
    if TailIndex > 2:
        TailIndex = 0
    NumberInQueue += 1
    print(Groups)


def Dequeue():
    global Groups, HeadIndex, TailIndex, NumberInQueue
    print("Group to present next: ",Groups[HeadIndex])
    if NumberInQueue == 0:
        return -1
    else:
        value = Groups[HeadIndex-1]
        for val in range(len(Groups)-1):
            Groups[val] = Groups[val+1]
        Groups[len(Groups)-1] = ''
        NumberInQueue -= 1
        if TailIndex == 2 and NumberInQueue == 3: #Keep TailIndex the same, so it points to the free, recently dequeued space
            TailIndex = 2
        else: #Otherwise decrement TailIndex
            TailIndex -= 1
        return value

Enqueue("Penguins")
Enqueue("Dogs")
Enqueue("Lions")
Dequeue()
print(Groups)
Dequeue()
print(Groups)
Dequeue()
print(Groups)
