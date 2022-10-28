""" 
WRITE A PROGRAM TO FIND FACTORIAL OF A NUMBER
"""
def input_number():
    """ 
    This function takes the input from user 
    - return :
        - inputed number (int)
    """
    return int(input("Enter Number to find Factorial : "))

def factorial(num):
    """ 
    This function find the factorial of a given number
    - Argument:
        - num : int
    return :
        - fact : factorial of a number 
    """
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

def recursion_factorial(num,fact=1):
    """ 
    Factorial of a number using recursion
    """
    return fact if num == 1 else  recursion_factorial(num-1,fact*num)
        
def main():
    num = input_number()
    # factorial_of_num = factorial(num)
    # print(factorial_of_num)
    factorial_of_num = recursion_factorial(num)
    print(factorial_of_num)

if __name__ == "__main__":
    """ 
    Execution of program starts from here
    """
    main()
