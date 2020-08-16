# Python 3 program to find index
# of first occurrence of x when
# array is sorted.

def findFirst(arr, n, x):
    count = 0
    isX = False
    for i in range(n):
        if (arr[i] == x):
            isX = True
        elif (arr[i] < x):
            count += 1

    return -1 if (isX == False) else count


# Driver Code
if __name__ == "__main__":
    x = 50
    arr = [10, 30, 20, 50, 20]
    n = len(arr)
    print(findFirst(arr, n, x))

# This code is contributed
# by ChitraNayal

