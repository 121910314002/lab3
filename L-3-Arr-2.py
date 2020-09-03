#program to copy the contents from one array to another array in reverse order

arr1 =[1,2,3,4,5]   # initialization of an array
arr2 = [None] * len(arr1)
length=len(arr1)

for i in range(0,len(arr1)):
    arr2[i]=arr1[length-i-1]   # to copy the array in a reverse order
    
print("contents in original aorder: ")
for i in range(0,len(arr1)):
    print(arr1[i])         # to display the original order of arr1
    
print("contents in reverse order: ")
for i in range(0,len(arr2)):
    print(arr2[i])        # to display the reverse order of arr1
    
    
output:
contents in original order:
1
2
3
4
5
contents in reverse order:
5
4
3
2
1
