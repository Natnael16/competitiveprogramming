from heapq import *
from collections import defaultdict, Counter

word_count = []
huffman_table = defaultdict(list)

# to_encode = "This is his message"
to_encode = input("Enter the message to be encoded: ")
if not to_encode:
    print("Enter one or more letter to encode")
    quit()

counter = Counter(to_encode)

class HuffmanTree:
    def __init__(self , count = 0 ,  letter = '',left = None ,right = None):

        self.letter = letter
        self.count = count
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str([self.count ,self.letter , self.left , self.right])

    def __lt__(self, other):
        return self.count < other.count

for char in counter:
    heappush(word_count , HuffmanTree(counter[char] , char))
    huffman_table[char].append(counter[char])


def encode(heads):
    if len(heads) == 1: return heads[0]
    smallest , smaller , = heappop(heads) , heappop(heads)

    head = HuffmanTree(smaller.count + smallest.count , '' , smallest , smaller)

    heappush(heads , head)
    return encode(heads)

root = encode(word_count)

#Traversing the the binary tree we constructed, traversing left will result adding 0 and right adding 1
#when we reach to leaf nodes add the sring collected during traversal to huffman table
def fill_table(node , s = ''):
    if not node: return
    if not node.left or not node.right:
        huffman_table[node.letter].append(s)
        return
    left = s + '0'
    right = s + '1'
    fill_table(node.left , left)
    fill_table(node.right , right)


fill_table(root)
print(dict(huffman_table))
res = ''
for i in to_encode:
    res+= huffman_table[i][1]
if len(huffman_table) == 1:
    print('0' * len(to_encode))
print(res)
# expected = "00110111011110010111100011101111000010010111100000001010"
# print(len(expected) == len(res))