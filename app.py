import random

random_number = [random.randint(1, 9) for i in range(4)]

while True:
    input_numbers = input("Guess a 4 digit number: ")
    user_numbers = []
    for i in input_numbers:
        if i not in "1234567890":
            continue
        user_numbers.append(int(i))
    cows = 0
    bulls = 0
    for index in range(4):
        if user_numbers[index] == random_number[index]:
            cows += 1
        elif user_numbers[index] in random_number:
            bulls += 1

    if cows == 4:
        print("cg dudz")
        break

    print(f"{cows} cows, {bulls} bulls")
    print(f"Last guess: {input_numbers}")