# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/
   
def totalFruit(fruits):
    highest = 0
    Dict = {}
    l = 0
    for r in range(len(fruits)):
        Dict[fruits[r]] = Dict.get(fruits[r], 0) + 1
        while len(Dict) >= 3:
            if Dict[fruits[l]] > 1:
                Dict[fruits[l]] -= 1
            else:
                Dict.pop(fruits[l])
            l += 1
        highest = max(highest, r - l + 1)
    return highest

if __name__ == "__main__":
    fruits = [1,2,1]            #3
    fruits2 = [0,1,1,1,0,2,2,2] #5
    fruits3 = [1,2,3,2,2]
    print(totalFruit(fruits))