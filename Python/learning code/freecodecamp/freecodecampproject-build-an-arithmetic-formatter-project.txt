def arithmetic_arranger(problems, show_answers=False):
    # check for number of problems, return error message if more than 4 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # create a new list to store split list
    decomposed_problems = [
        problems[index].split()
        for index in range(len(problems))
    ]
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for index in range(len(decomposed_problems)):
        # check for operator. Only + and - are allowed, else return error
        if decomposed_problems[index][1] != "+" and decomposed_problems[index][1] != "-":
            return "Error: Operator must be '+' or '-'."

        # check for alphabet characters, return error message if found.
        if decomposed_problems[index][0].isdigit() == False or decomposed_problems[index][2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'

        # check number of digits in the problem, only a max of 4 digits allowed
        if len(decomposed_problems[index][0]) > 4 or len(decomposed_problems[index][2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # check problem operator to solve problem
        numerator = decomposed_problems[index][0]
        denominator = decomposed_problems[index][2]
        if decomposed_problems[index][1] == "+":
            answer = str(int(numerator) + int(denominator))
            decomposed_problems[index].append(answer)
        elif decomposed_problems[index][1] == "-":
            answer = str(int(numerator) - int(denominator))
            decomposed_problems[index].append(answer)

        # Generate and format dashes
        dashes = max(len(decomposed_problems[index][0]), len(decomposed_problems[index][2])) + 2
        dash_str = ""
        for i in range(dashes):
            dash_str += "-"
        decomposed_problems[index].append(dash_str)

        # Format numerator and denominator
        gaps = max(len(decomposed_problems[index][0]), len(decomposed_problems[index][2])) - min(
            len(decomposed_problems[index][0]), len(decomposed_problems[index][2]))
        gap_str = ""
        for _ in range(gaps):
            gap_str += " "
        if len(decomposed_problems[index][0]) > len(decomposed_problems[index][2]):
            decomposed_problems[index][2] = gap_str + decomposed_problems[index][2]

        elif len(decomposed_problems[index][0]) < len(decomposed_problems[index][2]):
            decomposed_problems[index][0] = gap_str + decomposed_problems[index][0]

        if index == len(decomposed_problems) - 1:
            line1 += "  " + decomposed_problems[index][0]
            line2 += decomposed_problems[index][1] + " " + decomposed_problems[index][2]
            line3 += decomposed_problems[index][4]
            line4 += decomposed_problems[index][3].rjust(len(decomposed_problems[index][4]))
        else:
            line1 += "  " + decomposed_problems[index][0] + "    "
            line2 += decomposed_problems[index][1] + " " + decomposed_problems[index][2] + "    "
            line3 += decomposed_problems[index][4] + "    "
            line4 += decomposed_problems[index][3].rjust(len(decomposed_problems[index][4])) + "    "

    if show_answers == False:
        problems = f"{line1}\n{line2}\n{line3}"
        
    elif show_answers == True:
        problems = f"{line1}\n{line2}\n{line3}\n{line4}"
    
    return problems


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
