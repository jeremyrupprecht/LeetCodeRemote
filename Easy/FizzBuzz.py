class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list1 = list(map(str, range(1, n + 1)))

        for x in range(1, n + 1):
            
            if (x % 5 == 0) and (x % 3 == 0):
                list1[x - 1] = "FizzBuzz"
            elif (x % 3 == 0):
                list1[x - 1] = "Fizz"
            elif (x % 5 == 0):
                list1[x - 1] = "Buzz"
        
        return list1