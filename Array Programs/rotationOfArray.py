arr = [1,2,3,4,5,6,7]
n = len(arr)
k = int(input("Enter Number Of Rotation: "))
temp = [0]*n

# below does same as temp_arr = arr[k:]
for i in range(n - k):
    temp[i] = arr[k+i]
# print(temp)

# below one adds starting to last
for i in range(k):
    temp[n-k+i] = arr[i]
# print(temp)

for i in range(n):
    arr[i] = temp[i]
print(arr)