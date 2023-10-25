# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles, h):
    import math
    l = 1
    r = minK
    while l <= r:
        midK = l + (r-l) // 2
        hrs = 0
        # p[i] / midK 
        # bananas-inthis-pile / rate-of-banana-eating per hour
        # = number-of-hours-to-eat-this-pile
        # the sum of the hours eat every pile should add up to h (the total)
        # which is the total time that Koko has to eat 
        for p in piles:                
            hrs += math.ceil(p / midK)
        if hrs <= h:                    # if total hrs <= h then a valid k has been
            minK = min(midK, minK)      # found, save it and check the lower half of
            r = midK - 1                # k values b/c we want to find the smallest 
        else:                           # possible k value
            l = midK + 1   # k value invalid --> check upper half of k values
    return minK

if __name__ == "__main__":
    piles = [3,6,7,11]
    piles2 = [30,11,23,4,20]
    piles3 = [30,11,23,4,20]
    print(minEatingSpeed(piles3, 6))
