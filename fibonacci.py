""" 
write a program to print fibonacci series upto given number
"""

def input_number():
    """ 
    This function takes the input from user 
    - return :
        - inputed number (int)
    """
    return int(input("Enter Number to find Factorial : "))

def generate_fibonacci_series(num:int):
    """ 
    This function returns the fibonacci series upto the given number
    - Arguments :
        num : int
    - return : 
        - fib : list
    """
    fib = [0,1]
    if num > 2:
        for i in range(1,num-1):
            fib.append(fib[-1]+fib[-2])
        return fib
    return "Make sure input is greate than 2 "

def recursive_fibonacci(num,fibs):
    """ 
    This function gives the fibonacci series 
    - Arguments : 
        - num : number we need fibonacci series
        - fibs : fibonacci series
    - returns : 
        - fibs : final fibonacci series 
    """
    if len(fibs) >= num:
        return fibs
    else:
        fibs.append(fibs[-1]+fibs[-2])
        return recursive_fibonacci(num,fibs)

def main():
    num = input_number()
    fibonacci_list = generate_fibonacci_series(num)
    print(fibonacci_list)
    fibs = [0,1]
    fibonacci_list = recursive_fibonacci(num,fibs)
    print(fibonacci_list)

if __name__ == "__main__":
    """ 
    Execution of program starts from here
    """
    main()
