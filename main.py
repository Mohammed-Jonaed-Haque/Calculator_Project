import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


calculator_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,        #<--- here the function are stored in the dictionary,
    "/":divide           #<--- notice the functions has no "()" at the end ,therefore it is not triggered
}


def calculator():
    """" this function operates like a basic calculator,
     it does all the primary operations like --> '+' , '-' , '*' , '/' ."""

    print(art.logo)   #<--- prints out the imported logo
    user_still_wants_to_input=True
    first_number = float(input("Enter the first number you want to calculate: "))
    while user_still_wants_to_input:
        for symbol in calculator_dictionary:
            print(symbol)   #<--- prints out the "keys" in the dictionary.
        input_sign = input("Enter  the operation sign you want to do --> '+',  '-',  '*',  '/': ")
        second_number = float(input("Enter the second number you want to calculate: "))
        answer = calculator_dictionary[input_sign](first_number, second_number) #<--- it does the main calculations
        print(f"The answer is: {answer}")
        user_want_to_continue = input(f"enter 'y' if you want to continue the calculation with {answer}, or type 'n' to start a new calculation: ")
        if user_want_to_continue == 'y':
            first_number=answer  #<--- the answer of the previous calculation, acts as the first number here
        else:
            user_still_wants_to_input=False
            print("\n"*100)  #<--- it imitates a new page.
            calculator()  #<--- function called to keep the calculator running continuously.

calculator()  #<--- the function is called for the first time here

