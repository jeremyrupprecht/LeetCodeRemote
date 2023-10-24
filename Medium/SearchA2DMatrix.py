# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Trick --> if you map/transform the 1d midpoint index to 2d X and Y coordinates
# (which you use to find midpoints within the matrix), this literally be comes 
# the regular binary search question

def searchMatrix(matrix, target):
    numCols = len(matrix[0])
    l = 0
    r = len(matrix) * numCols - 1
    while l <= r:
        mid = l + (r - l) // 2
        midX = mid // numCols
        midY = mid % numCols
        if matrix[midX][midY] == target:     # found the target
            return True
        elif matrix[midX][midY] < target:    # target is above the midpoint, check top half of array
            l = mid + 1
        else:                              # target is below the midpoint, check bottom half of array
            r = mid - 1         
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(matrix1, 13))

