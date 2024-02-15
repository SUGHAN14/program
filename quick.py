def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    right= [x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    left=[x for x in arr if x>pivot]
    return quick(left)+mid+quick(right)
if __name__=="__main__":
    arr=[2,4,5,3,1]
    arr1=quick(arr)
    print(arr1)


