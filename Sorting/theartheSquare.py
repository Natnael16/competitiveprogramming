n = int(input("enter number of rows"))
m = int(input("enter number of columns"))
a = int(input("enter dimention of flagstone"))
def thearteSquare(row, col, sqr):
     addrow = row % sqr
     addcol = col % sqr
     newrow = row + addrow
     newcol = col + addcol
     grid = newrow*newcol
     flagstone = sqr * sqr
     required_tiles = grid // flagstone
     return required_tiles
print(thearteSquare(n,m,a))