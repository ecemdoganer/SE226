import math_utils
def main():
    x = float(input("Type the first number: "))
    y = float(input("Type the second number: "))

    operator = input("Which operation to perform? (+,-,*,/,**,%): ")
    operations = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '**': math_utils.power,
        '%': math_utils.mod
    }

    if operator in operations:
        result = operations[operator](x,y)
        print("Result: ", result)
    else:
        print("Invalid operation. ")

if __name__ == "__main__":
    main()
