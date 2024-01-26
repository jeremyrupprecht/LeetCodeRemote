# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/description/

def carFleet(target, position, speed):
    import math
    timeToTarget = [0] * len(position)
    for i in range(len(position)):
        timeToTarget[i] = (target - position[i]) / speed[i]

    zipped = zip(position, speed, timeToTarget)
    zipped = sorted(zipped, key=lambda x: x[0])

    stack = []
    for car in zipped:
        if stack and car[2] >= stack[len(stack)-1][2]:
            while stack and car[2] >= stack[len(stack)-1][2]:
                stack.pop()

        stack.append(car)

    return len(stack)

if __name__ == "__main__":
    # THERE ARE DIFFERENCES BETWEEN THE PYTHON AND PYTHON 3 VERSION OF THIS...i think
    print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))