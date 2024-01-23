# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

def evalRPN(tokens):
    stack = []
    finalResult = int(tokens[0])

    for t in tokens:
        stack.append(t)
        if t == "+" or t == "-" or t == "*" or t == "/":
            operator = stack.pop()
            op2 = int(stack.pop())
            op1 = int(stack.pop())

            if operator == "+":
                result = op1 + op2
            elif operator == "-":
                    result = op1 - op2
            elif operator == "*":
                    result = op1 * op2
            else:
                    result = int(float(op1) / op2)
            stack.append(result)
            finalResult = result

    return finalResult

if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    tokesn2 = ["4","13","5","/","+"]
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    print(evalRPN(tokens3))

        