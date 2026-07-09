n= int(input("Enter the size of array:"))
arr=[]
for i in range (n):
    element=int(input(f" Enter Array element {i+0}:"))
    arr.append(element)
print("\n Array in elements :")
for i in range(n):
    print(arr[i],end= " ")