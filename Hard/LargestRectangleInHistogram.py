# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

def largestRectangleArea(heights):
    maxArea = 0
    stack = []
    i = 0
    while i < len(heights):
        start = i
        while stack and heights[i] < stack[len(stack) - 1][1]:
            stackHead = stack.pop()
            poppedArea = stackHead[1] * (i - stackHead[0])
            maxArea = max(maxArea, poppedArea)
            start = stackHead[0]

        stack.append((start, heights[i]))
        i += 1

    endOfListIndex = len(heights)
    while stack:
        stackHead = stack.pop()
        poppedArea = stackHead[1] * (endOfListIndex - stackHead[0])
        maxArea = max(maxArea, poppedArea)

    return maxArea

if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))