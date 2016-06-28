


if __name__ == "__main__":
    from random import shuffle
    myList = [i for i in range(50)]
    shuffle(myList)
    quicksort(myList)
    print(myList)
