import re

def arithmetic_arranger(problems, solve = False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if (re.search("[/]", problem) or re.search("[*]", problem)):
            return "Error: Operator must be '+' or '-'."
        elif (re.search("[^\s0-9.+-]", problem)):
            return "Error: Numbers must only contain digits."
    
    for problem in problems:
        problem = problem.split()
        for num in problem:
            if len(num) > 4:
                return "Error: Numbers cannot be more than four digits."
    

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    arranged_problems = ""

    for problem in problems:
        sol = str(eval(problem))
        calc = problem.split(" ")
        num1 = calc[0]
        operator = calc[1]
        num2 = calc[2]
        bsc_length = max(len(num1), len(num2))

        if calc != problems[-1]:
            line1 += " " + f"{num1:>{bsc_length + 1}}" + "    "
            line2 += operator + " " + f"{num2:>{bsc_length}}" + "    "
            line3 += (bsc_length + 2) * "-" + "    "
        else:
            line1 += " " + f"{num1:>{bsc_length + 1}}"
            line2 += operator + " " + f"{num2:>{bsc_length}}"
            line3 += (bsc_length + 2) * "-"

        if solve:
            if calc != problems[-1]:
                line4 += f"{sol:>{bsc_length + 2}}" + "    "
            else:
                line4 += f"{sol:>{bsc_length + 2}}"              
            arranged_problems = f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}\n{line4.rstrip()}"
        elif not solve:
            arranged_problems = f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"


    return arranged_problems
