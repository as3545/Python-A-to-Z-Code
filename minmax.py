def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minsum=sum(arr[:4])
    maxsum=sum(arr[1:])
    print(minsum, maxsum)
