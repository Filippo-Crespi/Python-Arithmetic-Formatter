from string import digits


def count_error(x: list[str], num: int) -> bool:
    return len(x) > num


def operator_error(x: list[str], *chars) -> bool:
    chars = set(chars)
    for y in x:
        if chars.intersection(y) != set():
            return True
    return False


def digits_error(x: list[str], substr: str) -> bool:
    for y in x:
        if not set(y).issubset(substr):
            return True
    return False


def number_digits_error(x: list[str], num: int):
    for y in x:
        c = 0
        for char in y:
            if char == " " or char == "+" or char == "-":
                c = 0
                continue
            else:
                if char.isnumeric():
                    c += 1
                if c > num:
                    return True
    return False


def arithmetic_arranger(problems, show_answers=False):
    def_chars = digits + "+" + "-" + " "
    if count_error(problems, 5):
        return 'Error: Too many problems.'
    if operator_error(problems, "*", "/"):
        return "Error: Operator must be '+' or '-'."
    if digits_error(problems, def_chars):
        return 'Error: Numbers must only contain digits.'
    if number_digits_error(problems, 4):
        return 'Error: Numbers cannot be more than four digits.'

    # List where the string will be created
    result: list[str] = []
    # List for the answers if required
    answer: list[str] = []
    # List with the number of "-" for each operation
    spaces: list[chr] = []
    # List of the number in the top line of the column
    top: list[str] = []
    # List of the number in the bottom line of the column
    bottom: list[str] = []
    # Finding all the operator in the strings
    operator = [char for problem in problems for char in problem if char == "+" or char == "-"]

    # Building all the list required for the formatter
    for problem in problems:
        # Separation of the 2 number from the string
        index = problem.find("+") if problem.find("+") != -1 else problem.find("-")
        n1 = problem[:index - 1]
        n2 = problem[index + 2:]

        # Adding the number to the list based on their position in the column
        top.append(n1)
        bottom.append(n2)

        # Calculating the answer only if required
        if show_answers:
            if operator[problems.index(problem)] == "+":
                answer.append(str(int(n1) + int(n2)))
            else:
                answer.append(str(int(n1) - int(n2)))

        # Calculating the number of "-" at the end of each column operation
        n_space = max(len(n1), len(n2)) + 2
        spaces.append(n_space)

    # Building the first line
    for _ in range(0, len(problems)):
        for space in range(0, spaces[_] - len(str(top[_]))):
            result.append(" ")
        result.append(top[_])
        if _ != len(problems) - 1:
            result.append("    ")
    result.append("\n")

    # Building the second line
    for _ in range(0, len(problems)):
        result.append(operator[_])
        for space in range(0, spaces[_] - len(str(bottom[_])) - 1):
            result.append(" ")
        result.append(bottom[_])
        if _ != len(problems) - 1:
            result.append("    ")
    result.append("\n")

    # Building the third line
    for _ in range(0, len(problems)):
        for __ in range(spaces[_]):
            result.append("-")
        if _ != len(problems) - 1:
            result.append("    ")

    # Add the fourth line with the result only if required
    if show_answers:
        result.append("\n")
        for _ in range(0, len(problems)):
            for space in range(0, spaces[_] - len(str(answer[_]))):
                result.append(" ")
            result.append(answer[_])
            if _ != len(problems) - 1:
                result.append("    ")

    # Join the whole list in a single string
    return "".join(result)


print(f'\n{arithmetic_arranger(["32 - 6698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
