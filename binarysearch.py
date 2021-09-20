def binarysearch(arr,s,e,n):
   
   if e>=s:
    m=(s+e)//2
   if arr[m]==n:
      return m;
   elif arr[m]>n:
        return binarysearch(arr,s,m-1,n)
   else:
        return binarysearch(arr,m+1,e,n)

arr=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(arr)):
    print(arr[i],end=" ")
print()
n=int(input("enter the number"))
k=binarysearch(arr,0,len(arr),n)
print("element",arr[k],"present at index",k)
