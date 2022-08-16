
# leng , k = list(map(int , input().split()))
# count = 0 
# for _ in range(leng):
#    num = input()
#    s = set()
#    for i in num:
#         if int(i) <= k:
#             s.add(i)
#    if len(s) == k + 1:
#         count += 1

# print(count)
    
# tc = int(input())
# for _ in range(tc):
#     s_len  = int(input())
#     arr = input()

#     count = 0
#     res = 0
#     for b in arr:
#         if b == ")":
#             count -= 1
#             if count < 0:
#                 res += 1
#                 count += 1
            
#         if b == "(":
#             count += 1
#     print(res)


# from collections import defaultdict, deque


# num_nodes = int(input())
# tree = defaultdict(list)
# level_len = [1]
# level_map = defaultdict(set)


# level_map[1].add(1) 

# for _ in range(num_nodes - 1):
#     one , two = tuple(map(int , input().split()))
#     tree[one].append(two)
#     tree[two].append(one) # notice

# q = deque([1])
# visited = set()
# level = 1
# while q:
#     for i in range(len(q)):
#         cur = q.popleft()
#         visited.add(cur)
#         for node in tree[cur]:
#             if node not in visited:
#                 q.append(node)
#                 level_map[level + 1].add(node)
#     level += 1
#     level_len.append(len(q))

# to_check = list(map(int , input().split()))

# flag = True
# i = 0
# for ind , printed in enumerate(level_len):
#     while level_len[ind] != 0:
        
#         if to_check[i] in level_map[ind + 1]:
#             i += 1
#         else:
#             flag = False
#             break
#         level_len[ind] -= 1

# print("Yes") if flag else print("NO")

    