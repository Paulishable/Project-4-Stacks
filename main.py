"""main routine for Project number 4"""
from stack import Stack


def stack_is_equal_or_higher(stack_top, next_in):
    """check operators to find comparisons (used in in2post)"""
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

    return False

def eval_postfix_expression(expr):
    """check a postfix expression for syntax (used by eval_postfix)"""
    parens = 0
    digits = 0
    operators = 0
    for char in expr:
        if char in["(", ")"]:
            parens += 1
        if char.isdigit():
            digits += 1
        if char in ["+", "-", "*", "/"]:
            operators += 1
    if parens != 0 or digits - operators != 1:
        return False
    return True

def eval_infix_expression(expr):
    """checks an INFIX expression for syntax error (used by in2post"""
    left_paren = 0
    right_paren = 0
    for char in expr:
        if char == "(":
            left_paren += 1
        if char == ")":
            right_paren += 1
    return bool(left_paren == right_paren)


def in2post(expr):
    """converts an infix expression to a postfix one"""
    try:
        isinstance(expr, str)
    except ValueError as val_err:
        raise ValueError("ValueError exception thrown") from val_err
    if expr is None:
        raise ValueError("ValueError exception thrown") from val_err
    if not eval_infix_expression(expr):
        raise SyntaxError("SyntaxError exception thrown")

    the_post_expr = ""
    convert_stack = Stack()
    for next_input in expr:

        if next_input == "(":
            convert_stack.push(next_input)
        elif next_input.isdigit():
            the_post_expr += " " + next_input
        elif next_input in ["+", "-", "*", "/"]:
            while convert_stack.size() > 0 and convert_stack.top() != "(" and \
                    stack_is_equal_or_higher(
                    convert_stack.top(), next_input):
                the_post_expr += " " + convert_stack.top()
                convert_stack.pop()
            convert_stack.push(next_input)
        else:
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


def open_and_read_data():
    """main driver function - reads file and does all for each line in the file"""
    with open("data.txt", "r", encoding="utf-8") as data_file:
        for line in data_file:
            line = line.strip()
            print(f"infix: {line}")
            post_fix_expr = in2post(line)
            print(f"postfix: {post_fix_expr}")
            print(f"answer: {eval_postfix(post_fix_expr)}\n")

        data_file.close()


def eval_postfix(expr):
    """takes a postfix expression and calculates it"""
    try:
        isinstance(expr, str)
    except ValueError as val_err:
        raise ValueError("ValueError exception thrown") from val_err
    if expr is None:
        raise ValueError("ValueError exception thrown")
    if not eval_postfix_expression(expr):
        raise SyntaxError("SyntaxError exception thrown")


    calc_stack = Stack()

    for next_input in expr:

        if next_input not in ["", " "]:
            if next_input.isdigit():
                calc_stack.push(float(next_input))
            else:
                if calc_stack.top() != "":
                    if calc_stack.top():
                        second_number = calc_stack.top()
                    calc_stack.pop()
                    if calc_stack.top():
                        first_number = calc_stack.top()
                    calc_stack.pop()
                    if next_input == "+":
                        calc_stack.push(first_number + second_number)

                    if next_input == "-":
                        calc_stack.push(first_number - second_number)

                    if next_input == "*":
                        calc_stack.push(first_number * second_number)

                    if next_input == "/":
                        calc_stack.push(first_number / second_number)

    return calc_stack.top()


# this one line does all that is asked for in project 4:
open_and_read_data()
