import re

def arithmetic_arranger(problems, solve = False):
    error_test = False
    if len(problems) > 5:
            error_test = True
            return "Error: Too many problems."

    for problem in problems:
        if (re.search("[/]", problem) or re.search("[*]", problem)):
            error_test = True
            return "Error: Operator must be '+' or '-'."
        elif (re.search("[^\s0-9.+-]", problem)):
            error_test = True
            return "Error: Numbers must only contain digits."

    if not error_test:
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""
        arranged_problems = ""

        for calc in problems:
            calc = calc.split(" ")
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
                sol = str(int(num1) + int(num2))
                if calc != problems[-1]:
                    line4 += f"{sol:>{bsc_length + 2}}" + "    "
                else:
                    line4 += f"{sol:>{bsc_length + 2}}"
                arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
            elif not solve:
                arranged_problems = f"{line1}\n{line2}\n{line3}"


    return arranged_problems
