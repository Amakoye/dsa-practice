def plusOne(digits):
    for i in range(len(digits)):
        digits[i] = str(digits[i])

    plus_one = str(int("".join(digits)) + 1)

    new_digits = []

    for i in range(len(plus_one)):
        new_digits.append(int(plus_one[i]))

    return new_digits


print(plusOne([4, 3, 2, 1]))
