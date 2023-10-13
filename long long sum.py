//Code
def aVeryBigSum(ar):
    # Use the sum() function to calculate the sum of elements in the array
    return sum(ar)

# Input the number of elements
n = int(input())

# Input the array of integers
ar = list(map(int, input().split()))

result = aVeryBigSum(ar)
print(result)
