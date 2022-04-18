import itertools
tc = input()
for _ in range(int(tc)):
     str_leng = input()

     red = list(input())
     blue = list(input() )

     red = sorted(list(itertools.permutations([int(i) for i in red])) , reverse=True)
     blue = sorted(list(itertools.permutations([int(j) for j in blue])), reverse= True)
     print(red,blue)
     f1 = 0
     f2 = 0
     for i in range(len(red)):
          for j in blue:
               if red[i] > j:
                    f1 += 1
               else:
                    f2 += 1
     print(f1 , f2)
     if f1 > f2:
          print('RED')
     elif f2 > f1:
          print("BLUE")
     else:
          print('EQUAL')
# leng = input()
# nums = list(map(int, input().split()))
# countneg = 0
# count0 = 0
# ans = 0
# for i in nums:
#      if i == 0:
#           count0 += 1
#      elif i < 0:
#           countneg += 1
#           ans += (abs(i) - 1)
#      elif i > 0:
#           ans += (i - 1)
# if countneg % 2 != 0 and count0 > 0:
#      count0 -= 1
#      ans += 1
#      ans += count0
     
# elif countneg % 2 != 0 and count0 == 0:
#      ans += 2
# else:
#      ans += count0

# print(ans)

