def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        number = int(input("Enter a number: "))
        while number != 1:
            number = collatz(number)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
