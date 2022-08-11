class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         column_map = defaultdict(set)
#         row_map = defaultdict(set)
        
#         {
#             0 : {5 , 6 , 8 , 4 ,7}
#         }
#         box_map = defaultdict(set)
        
#         1 : {
#             5 , 3 , 6 ,9 , 8 , 
#         }
        
        
#         box 1 { row (0 , 1 , 2) , col (0 , 1 , 2)}
#         box 2 { row (0 1 , 2) , (3 , 4 ,  5) }
#         box 3 row (0 1 , 2) , column (6 , 7 , 8)
        
#         box 4 { row (3 , 4 , 5) , col (0 , 1 , 2)}
#         box 5 { row (3 , 4 , 5) , (3 , 4 ,  5) }
#         box 6 row (3 , 4 , 5) , column (6 , 7 , 8)
        
#         box 1 { row (6 , 7 , 8) , col (0 , 1 , 2)}
#         box 2 { row (6 ,  7 , 8) , (3 , 4 ,  5) }
#         box 3 row (6 ,  7 , 8) , column (6 , 7 , 8)
        
#         O(81 + 81 + 9 * 6 + 81) space
#         O ( 81 * 9) time
        col_map = defaultdict(set)
        row_map = defaultdict(set)
        box_map = defaultdict(set)
        
        check_box = [({0 , 1 , 2 } ,{0 , 1 , 2 } ) , ({0 , 1 , 2 } ,{3 , 4 , 5 } ), ({0 , 1 , 2 } ,{6 , 7 , 8 } ), 
                     ({3 , 4 , 5 } ,{0 , 1 , 2 } ) , ({3 , 4 , 5 },{3 , 4 , 5 }), ({3 , 4 , 5 } ,{6 , 7 , 8 } ), 
                     ({6 , 7 , 8 } , {0 , 1 , 2 } ) , ({6 , 7 , 8 },{3 , 4 , 5 } ), ({6 , 7 , 8 } ,{6 , 7 , 8 } ), 
                    ]
        
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '.':
                    set_length = len(row_map[row])
                    row_map[row].add(board[row][col])
                    after = len(row_map[row])
                    if set_length == after:
                        print("here1")
                        return False
                        
                    set_length = len(col_map[col])
                    col_map[col].add(board[row][col])
                    after = len(col_map[col])
                    if set_length == after:
                        print("here2")
                        return False
                        
                    box_num = -1
                    for ind ,  box in enumerate(check_box):
                        if row in box[0] and col in box[1]:
                            box_num = ind
                            
                    set_length = len(box_map[box_num])
                    box_map[box_num].add(board[row][col])
                    after = len(box_map[box_num])
                    if set_length == after:
                        print("here3")
                        return False
        return True
                    
                    
                    
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        
            
        