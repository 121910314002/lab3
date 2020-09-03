# to remove the duplicate elements in an array

def remove(arr):
    final = []
    for num in arr:
        if num not in final:
            final.append(num)
    return final
    
arr=(int(input("enter the number of elements in the list"))
for b in range(0,arr):
    element=int(input("enter element"+str(b+1)+":"))
print(arr)
final=remove(arr)
for i in range(0,len(final)):
    print(final[i])
