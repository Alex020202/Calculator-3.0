import math
operation = []
numbers = []
last_key = 0
primer = input("Enter primer:")
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


print(numbers)
