# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

def maxArea(height):
    greatestArea = -1
    L = 0
    R = len(height) - 1
    while L < R:
        currentArea = (R - L) * (min(height[L], height[R]))
        greatestArea = max(currentArea, greatestArea)
        if (height[L] <= height[R]):
            L += 1
        else:
            R -= 1
    return greatestArea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height2 = [1,1]
    height3 = [0,0]
    height4 = [1,2,3,4,20,20,4,3,2,1]
    print(maxArea(height4))