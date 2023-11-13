import random
import unittest

class IntegerRequireException(Exception):
    print("Please provide integer value ")
    pass


def getRandomIntFromRange(min, max):
    """
    Random integer.

    :param min: min value 
    :param max: max value

    :returns: random integer value from min and max
    :rtype: int

    """
    return random.randint(min, max)


def operatorSelection():
    """
    Operator selection.

    :returns: random choice of from operations 
    :rtype: str
    """
    return random.choice(['+', '-', '*'])


def performOperation(firstNumber, secondNumber, operation):
    """
    Perform operation with the selected operator

    :param firstNumber: first number for the operation
    :param secondNumber: second number for the operation
    :param operation: operation to be use on first and second number

    :returns: string of problem, result on operation
    :rtype: str, int
    """
    problem = f"{firstNumber} {operation} {secondNumber}"
    if operation == '+':
        result = firstNumber + secondNumber
    elif operation == '-': 
        result = firstNumber - secondNumber
    else: 
        result = firstNumber * secondNumber
    return problem, result

def math_quiz():
    score = 0
    rounds = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    try:
        for _ in range(rounds):
            first_number = getRandomIntFromRange(1, 10);
            second_number = getRandomIntFromRange(1, 5); 
            operation = operatorSelection()

            PROBLEM, ANSWER = performOperation(first_number, second_number, operation)
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

        print(f"\nGame over! Your score is: {score}/{rounds}")
    except IntegerRequireException as ie:
        print(f"Error {ie}")
    finally:
        print(f"\nRestart with accepted values")


if __name__ == "__main__":
    math_quiz()
