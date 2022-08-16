# tc  = int(input())
# for _ in range(tc):
#     cur = input()
#     print('YES') if cur.lower() == 'yes' else print("NO")


### 2

# tc = int(input())

# for _ in range(tc):
#     length = input()
#     problems = input()
#     seen = set()
#     res = 0
#     for problem in problems:
#         if problem in seen:
#             res += 1
#         else:
#             res += 2
#             seen.add(problem)
#     print(res)

## 3

# tc = int(input())
# for _ in range(tc):
#     key_leng = int(input())
#     cur_combination = list(map(int , input().split()))
   
#     for ind in range(key_leng):
#         change_leng , change = input().split()
#         for move in change:
#             if move == "D":
#                 cur_combination[ind] = (cur_combination[ind] + 1) % 10
#             elif move == "U":
#                 if cur_combination[ind] > 0:
#                     cur_combination[ind] -= 1
#                 else:
#                     cur_combination[ind] = 9
#     for i in cur_combination: print(i , end=' ')

### 4

# testcases = int(input())

# for _ in range(testcases):
#     str_set = set()
#     str_list = []
#     str_len = int(input())
#     for ind in range(str_len):
#         s = input()
#         str_set.add(s)
#         str_list.append(s)
#     res = ''
#     for string in str_list:
        
#         flag = False
#         for i in range(1 , len(string)):
#             if string[:i] in str_set and string[i:] in str_set: flag = True
#         res += '1' if flag else '0'
#     print(res)


### 5

tc = int(input())


for _ in range(tc):
    n = int(input())
    grid = []
    for size in range(n):
        row = input()
        row = [i for i in row]
        grid.append(row)
    visited = set()
    count = 0
    for row in range(n):
        for col in range(n):
            if (row, col) in visited: continue
            row1 = col
            col1= (n - 1) - row
            row2,col2 = col1 , (n - 1) - row1
            row3 , col3 = col2 , (n - 1) - row2
            visited.add((row ,col))
            visited.add((row1 ,col1))
            visited.add((row2 ,col2))
            visited.add((row3 ,col3))
            # print(row, col, row1, col1)
            tot = int(grid[row][col])+ int(grid[row1][col1])+ int(grid[row2][col2])+ int(grid[row3][col3])
            # print(tot)
            if tot == 1 or tot == 3: count += 1
            elif tot == 2: count += 2
    print(count)







    


