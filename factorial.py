def FindFactorial(num,fact = 1):
    """ 
    This function finds the factorial of a number
    """
    if num == 1:
        return fact
    else:
        return FindFactorial(num-1,fact*num)

res = FindFactorial(5)
print(res)