import array as arr
arr=[10,20,30,40,50]
x=40
for i in range(len(arr)):
    if arr[i]==x:
        print("found at index",i)
        break
    else:
        print("not found")