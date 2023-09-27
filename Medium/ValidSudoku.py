# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
def isValidSudoku(board):
    rDict = defaultdict(set)
    cDict = defaultdict(set)
    sDict = defaultdict(set)
    for i in range (len(board)):
        for o in range (len(board[i])):
            if board[i][o] == ".":
                continue
            if (board[i][o] in rDict[i] or 
                board[i][o] in cDict[o] or 
                board[i][o] in sDict[(i // 3, o // 3)]): 
                return False
            rDict[i].add(board[i][o])
            cDict[o].add(board[i][o])
            sDict[(i // 3, o // 3)].add(board[i][o])
    return True


if __name__ == "__main__":

    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))