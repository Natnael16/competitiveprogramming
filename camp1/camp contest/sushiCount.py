arr = [2,2,2,1,2,1,1,2,1,1,2,2,2,1]
f_type = arr[0]
count = 1
zip_count = []
i = 1
while i < len(arr):
    if arr[i] == f_type:
        count += 1
    else:
        zip_count.append((f_type,count))
        f_type = arr[i]
        count = 1
    i += 1
    if i == len(arr):
        zip_count.append((f_type,count))
max_leng = -float('inf')
for i in range(1,len(zip_count)):
    max_leng = max(max_leng,min(zip_count[i][1],zip_count[i-1][1])*2)

print(max_leng)