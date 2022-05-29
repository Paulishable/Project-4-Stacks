import re
from stack import *

infix_expressions = []
my_stack = Stack()


def stack_is_equal_or_higher(stack_top, next_in):
    stack_top_is_high = False
    next_in_is_high = False
    if stack_top in ["*", "/"]:
        stack_top_is_high = True
    if next_in in ["*", "/"]:
        next_in_is_high = True

    if stack_top_is_high and not next_in_is_high:
        return True

    if stack_top_is_high and next_in_is_high:
        return True

    if not stack_top_is_high and not next_in_is_high:
        return True


def in2post(expr):
    the_post_expr = ""
    convert_stack = Stack()
    for index in range(len(expr)):
        next_input = expr[index]

        if next_input == "(":
            convert_stack.push(next_input)
        elif next_input.isdigit():
            the_post_expr += " " + next_input
        elif next_input in ["+", "-", "*", "/"]:
            while convert_stack.size() > 0 and convert_stack.top() != "(" and stack_is_equal_or_higher(
                    convert_stack.top(), next_input):
                the_post_expr += " " + convert_stack.top()
                convert_stack.pop()
            convert_stack.push(next_input)
        else:
            the_post_expr += " " + convert_stack.top()
            convert_stack.pop()

            while convert_stack.size() > 0 and convert_stack.top() != "(":
                the_post_expr += " " + convert_stack.top()
                convert_stack.pop()

    while convert_stack.size() > 0:
        if convert_stack.top() != "(":
            the_post_expr += " " + convert_stack.top()
            convert_stack.pop()
        else:
            convert_stack.pop()

    return the_post_expr


def get_data():
    with open("data.txt", "r", encoding="utf-8") as data_file:
        for line in data_file:
            line = line.strip()
            infix_expressions.append(line)
        data_file.close()


def display_infix(index):
    expr = infix_expressions[index]
    print(expr)
    return expr


def display_postfix():
    pass


def eval_postfix(expr):
    calc_stack = Stack()
    running_total = 0.0

    for index in range(len(expr)):
        next_input = expr[index]
        print(next_input, running_total)

        if next_input not in ["", " "]:
            if next_input.isdigit():
                calc_stack.push(float(next_input))
            else:
                if calc_stack.top() != "":
                    print("here is the top")
                    print(calc_stack.top())
                    if calc_stack.top() not in ["", " "]:
                        second_number = float(calc_stack.top())
                    calc_stack.pop()
                    if calc_stack.top() not in ["", " "]:
                        first_number = float(calc_stack.top())
                    calc_stack.pop()
                    if next_input == "+":
                        running_total += first_number + second_number

                    if next_input == "-":
                        running_total += first_number - second_number

                    if next_input == "*":
                        running_total += first_number + second_number

                    if next_input == "/":
                        running_total += first_number / second_number

    calc_stack.push(running_total)
    return running_total

def display_result():
    pass


exp = 13

get_data()

# in2post(infix_expressions[exp])

# print(f"top of my stack: is {my_stack.top()}")
print("the in_fix expression is    ")
display_infix(exp)
print()
print(f"the post_fix expression is  ")
print(in2post(infix_expressions[exp]))

answer = eval_postfix(in2post(infix_expressions[exp]))

print(f"answer is : {answer}")
# my_stack.__str__()
