# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    stackList = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stackList.append(char)
        else:
            if stackList:
                if (char == ")" and stackList[-1] == "("
                    or char == "]" and stackList[-1] == "["
                    or char == "}" and stackList[-1] == "{"):
                    stackList.pop()
                else:
                    return False
            else:
                return False #stackList.append(char)

    if stackList:
        return False
    else:
        return True
        

if __name__ == '__main__':

    s = "{}()()[]"
    print(isValid(s))