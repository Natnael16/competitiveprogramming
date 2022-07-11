from collections import defaultdict , deque

neighbours = defaultdict(list)
file_name = input('Enter the file name: ')
vertices = input('Enter two verticies separated by comma to get the shorest path: ').split(',')
file = open(file_name , 'r').read().split('\n')
import turtle as tur


if not file:
    print('invalid input!')
    quit()
print('The number of vertices is',file[0])
for node in file[1:]:
    arr = list(map(int , node.split()))
    print("Vertex {}:".format(arr[0]), end=' ')
    for i in range(1,len(arr)):
        print('({} , {})'.format(arr[0], arr[i] ) , end=' ')
        neighbours[arr[0]].append(arr[i])
    print('\n')

def BFS(start , end):
    visited = set()
    queue = deque([(start,'{}'.format(start))])
    visited.add(start)
    while queue:
        cur_node , path = queue.popleft()
        visited.add(cur_node)

        if cur_node == end:
            return path

        for neighbour in neighbours[cur_node]:
            if neighbour not in visited:
                queue.append((neighbour , path + " " + str(neighbour)))
path = BFS(int(vertices[0]) , int(vertices[1]) )
print("The path is", path if path else "Unreachable")
tur.p
tur.dot(20)
tur.goto(tuple(map(int , path.split()))[:2])
tur.hideturtle()
tur.mainloop()