#Made by Damir Zababuryn

import random

#created the Item class
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

#hash function that translates the integer into binary and counts the sum of numbers in it.
#Then assigning the initial bucket to that number.
def bin_Hash(item):
    count = 0
    bin_item = bin(item)
    binary_digits = bin_item[2:]
    for char in binary_digits:
        if (char == '1'):
            count += 1
    return count


#Insertion method for Binary function, that calculates the number
def HashInsertBin(hashTable, item, N):
    i = 0
    bucketsProbed = 0

    # Hash function determines initial bucket
    bucket = bin_Hash(item.key)


    while bucketsProbed < N:
        # Insert item in next empty bucket
        if hashTable[bucket] is None:
            hashTable[bucket] = item
            return bucketsProbed

        # Increment i and recompute bucket index
        i += 1
        bucket = (item.key + i + i ** 2) % N

        # Increment number of buckets probed
        bucketsProbed += 1

    return bucketsProbed

#Insertion method for Binary function, that calculates the number
def HashInsertMod(hashTable, item, N):
    i = 0
    bucketsProbed = 0

    # Hash function determines initial bucket
    bucket = item.key % 10



    while bucketsProbed < N:
        # Insert item in next empty bucket
        if hashTable[bucket] is None:
            hashTable[bucket] = item
            return bucketsProbed

        # Increment i and recompute bucket index
        i += 1
        bucket = (item.key + i + i ** 2) % N

        # Increment number of buckets probed
        bucketsProbed += 1

    return bucketsProbed


if __name__ == '__main__':
    key_pair_arr = []
    N = 100  # size of hash table
    hashTableBin = [None] * N  # create hash table as an array of N None values
    hashTableMod = [None] * N

    print("----------------------------------------------------------------------------------------")

    #create an array of random key-value pairs using seed
    for i in range(0, N):
        random.seed(i)
        item = Item(random.randint(0, 1000), i)
        key_pair_arr.append(item)
    random.seed()

    #printing the array of elements
    for i in range(0, N):
        print(f"{key_pair_arr[i].key}")

    print("----------------------------------------------------------------------------------------")
    #output the number of collision occured in Binary method
    collisions_Binary = 0
    for i in range(0, N):
        collisions_Binary += HashInsertBin(hashTableBin, key_pair_arr[i], N)
    print(f"Collisions using bin function: {collisions_Binary}")

    print("----------------------------------------------------------------------------------------")
    # output the number of collision occured in Module method
    collisions_Mod = 0
    for i in range(0, N):
        collisions_Mod += HashInsertMod(hashTableMod, key_pair_arr[i], N)
    print(f"Collisions using module function: {collisions_Mod}")

    print("----------------------------------------------------------------------------------------")
    # Print the contents of the Bin hash table
    i = 0
    for i in range(N):
        if hashTableBin[i] is not None:
            print(f"bucket {i}: {hashTableBin[i].key}")
        else:
            print(f"bucket {i}: empty")


    print("----------------------------------------------------------------------------------------")
    # Print the contents of the Module hash table
    for i in range(N):
        if hashTableMod[i] is not None:
            print(f"bucket {i}: {hashTableMod[i].key}")
        else:
            print(f"bucket {i}: empty")




