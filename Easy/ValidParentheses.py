# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses

def isValid(s):
    stackList = []
    # inputs w/ length 1 automatically have no opening 
    # and closing tag (would need a length of at least 2)
    if len(s) < 2:
        return False
    for char in s:
        stackList.append(char)

        # compare the last and second last elements in the list (which is
        # represented in the stack) and remove them if they are a matching
        # pair, fulfilling the LIFO nature of a stack
        # 
        # also consider the case with only a single element in the stack
        # lastElem and secondLastElem default to the same element, b/c 
        # negative indices in python loop around, (in this case to the 
        # same element) and the stack pop doesn't trigger as the same
        # element is being compared to itself

        lastElem = stackList[len(stackList)-1]
        secondLastElem = stackList[len(stackList)-2]
        if (secondLastElem == "(" and lastElem == ")" 
        or secondLastElem == "[" and lastElem == "]" 
        or secondLastElem == "{" and lastElem == "}"):
            stackList.pop()
            stackList.pop()

    if len(stackList) == 0:
        return True
    else:
        return False

if __name__ == "__main__":

    s = "()[]{}"
    s1 = "()"
    s2 = "("
    s3 = "(])"
    s4 = "(]"
    s5 = "([])"
    s6 = "([]{})"
    s7 = "([]{))"
    s8 = "((((()))))"
    print("s",isValid(s))
    print("s1",isValid(s1))
    print("s2",isValid(s2))
    print("s3",isValid(s3))
    print("s4",isValid(s4))
    print("s5",isValid(s5))
    print("s6",isValid(s6))
    print("s7",isValid(s7))
    print("s8",isValid(s8))
