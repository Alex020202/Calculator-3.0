import math
def solve_primer(primer):
    operation = []
    numbers = []
    last_key = 0
    primer = primer

    for key in range(len(primer)):
        if primer[key] < "0" or primer[key] > "9":
            operation.append(primer[key])
            numbers.append(int(primer[last_key:key]))
            last_key = key + 1
    numbers.append(int(primer[last_key:len(primer)]))

    key = 0
    while key < len(operation):
        if operation[key] == "*" or operation[key] == "/":
            if operation[key] == "*":
                del operation[key]
                numbers[key] = numbers[key] * numbers[key+1]
                del numbers[key + 1]
                key -= 1
            elif operation[key] == "/":
                del operation[key]
                numbers[key] = numbers[key] / numbers[key+1]
                del numbers[key + 1]
                key -= 1
        key += 1
    key = 0
    while key < len(operation):
        if operation[key] == "+" or operation[key] == "-":
            if operation[key] == "+":
                del operation[key]
                numbers[key] = numbers[key] + numbers[key+1]
                del numbers[key + 1]
                key -= 1
            elif operation[key] == "-":
                del operation[key]
                numbers[key] = numbers[key] - numbers[key+1]
                del numbers[key + 1]
                key -= 1
        key += 1
    return numbers[0]


primer_full: str = input("Enter primer:")

while "(" in primer_full:
    pr = 1
    count = 0
    for i in range(len(primer_full)):
        if primer_full[i] == "(":
            count += 1
        if count == primer_full.count("("):
            for j in range(i, len(primer_full)):
                if primer_full[j] == ")":
                    pr = primer_full[i+1:j]
                    break
        if pr != 1:
            break
    x = solve_primer(pr)
    primer = primer_full[:i] + str(x) + primer_full[j+1:]
    print(primer)
    primer_full = primer
print(solve_primer(primer_full))

