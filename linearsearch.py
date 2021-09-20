def linearsearch(arr,n):
    m=len(arr)
    for i in range(m):
        if arr[i]==n:
            return i
    return -1
arr=[1,2,3,4,15,6,7]
n=int(input("entet the number"))
e=linearsearch(arr,n)
if arr[e]==n:
    print("element found")
elif e==-1:
    print("element not found")
