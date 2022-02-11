"""
9. Write a simple calculator program that performs arithmetic operation on 2 numbers. Input consists of 3 values, separated by an arithmetic operator, in the following format:    float operator float

where float is any decimal number and operator is either +, -, *, /.

    Run 1
    Enter arithmetic expression: 23.6 + 33.2
    Result: 56.8

    Run 2
    Enter arithmetic expression: 85 % 15
    Invalid arithmetic operator

Assume that the numeric values are valid, but the operator may be invalid.
"""
def lab2_q9():
    # get the expression from user in format (float operator float)
    # use split to break in 3 strings
    num1, operator, num2 = input("Enter arithmetic expression: ").split()
    num1, num2 = float(num1), float(num2)   # convert the 2 num into float

    # check if operator is one of these + - * /
    if len(operator) != 1 or operator not in "+-*/":
        print("Invalid arithmetic operator")
    elif operator == "+":
        print("Result: {}".format(num1+num2) )
    elif operator == "-":
        print("Result: {}".format(num1-num2) )
    elif operator == "*":
        print("Result: {}".format(num1*num2) )
    else:
        print("Result: {}".format(num1/num2) )

    expression = input("Enter arithmetic expression: ")
    num1, operator, num2 = expression.split()

    if len(operator) != 1 or operator not in "+-*/":
        print("Invalid arithmetic operator")
    else:
        print("Result: {}".format(eval(expression)) )

lab2_q9()