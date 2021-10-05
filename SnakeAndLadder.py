s = input().split(',')
l = list(map(int,input().split(',')))
D = {}
count = 0
for i in s:
    t = i.split(':')
    D[int(t[0])] = int(t[1])
for val in l:
    count += val
    if count in D:
        count = D[count]
        
if count >= 100:
    print("Yes", end='')
else:
    print("No", end='')
    
# Input:
# 6:14, 11:28, 17:74, 22:7, 38:59, 49:12, 57:76, 61:54, 81:98, 88:4
# 6, 3, 4, 3, 5
# Output:
# Yes
