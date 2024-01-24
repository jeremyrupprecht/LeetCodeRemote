# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

def dailyTemperatures(temperatures):
    output = [0] * len(temperatures)
    stack = []
    i = 0
    while i < len(temperatures):
        while stack and temperatures[i] > stack[len(stack)-1][0]:
            head = stack.pop()
            indexDiff = i - head[1]
            output[head[1]] = indexDiff
        
        stack.append([temperatures[i], i])
        i += 1
    return output

if __name__ == "__main__":
    temps = [73,74,75,71,69,72,76,73]
    temps2 = [30,40,50,60]
    temps3 = [30,60,90]
    temps4 = [89,62,70,58,47,47,46,76,100,70]
    print(dailyTemperatures(temps))
    print(dailyTemperatures(temps2))
    print(dailyTemperatures(temps3))
    print(dailyTemperatures(temps4))
