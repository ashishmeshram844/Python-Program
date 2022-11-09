""" WRITE A PROGRAM TO FIND GCD OF TWO NUMBERS  """

def find_gcd(num1,num2):
    """ 
    This function find the gcd (greatest common divisor) of two numbers
    """
    return find_gcd(num2,num1%num2) if num1%num2 else  num2
    
print(find_gcd(2,12))


# num1,num2 = 48,18
# if num1 < num2:
#     num1,num2 = num2,num1

# while num2 != 0:
#     rem = num1%num2 
#     if rem == 0:
#         break
#     num1 = num2
#     num2 = rem
# print(num2)

