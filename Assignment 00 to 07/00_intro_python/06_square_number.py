def main():
    number = float(input(" \033[1;3m Put a number to see it's square: \033[0m"))
    square = number * number

    print(f"The square of the {number} is {square}")

if __name__ == "__main__":
    main()

