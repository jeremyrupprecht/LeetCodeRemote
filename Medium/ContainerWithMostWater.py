# 11 Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    l = 0
    r = len(height)-1
    maxArea = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        if height[l] < height[r]:   
            l += 1
        elif height[l] > height[r]:   
            r -= 1
        else: 
            l += 1
            while height[l] == height[r] and l < r: 
                l += 1
        maxArea = max(maxArea, area)
    return maxArea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height1 = [1,1]
    print(maxArea(height))