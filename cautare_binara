def binarySearch(array, x):
    low=1
    high=len(array)
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[1,2,3,4,5,6,7,8,9,10]
x=5
result=binarySearch(array,x)
if result!=-1:
    print("Elementul se afla pe pozitia: ", result)
else:
    print("Elementul nu se afla in lista")
