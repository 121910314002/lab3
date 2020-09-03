#program to copy the contents from one array to another array.

arr1 =[1,2,3,4,5]  # initialization of an array
arr2 = [None] * len(arr1)  # initialize another array to copy the contents into it 

for i in range(0,len(arr1)):
    arr2[i]=arr1[i]     # copying contents from one array to another array
    
print("contents in original array: ")
for i in range(0,len(arr1)):
    print(arr1[i])
    
print("contents in new array: ")
for i in range(0,len(arr2)):
    print(arr2[i])    #displaying the contents after being copied from arr1
    
    
output:
contents in original array:
1
2
3
4
5
contents in original array:
1
2
3
4
5
