""" 
WRITE A PROGRAM FOR CONSUCATIVE SUM OF A NUMBER TILL SUM
CONTAIN ONLY ONE DIGIT
"""

def input_number():
    """ 
    This function takes input of number from user
    """
    return int(input("Enter a number for consecutive sum : "))

def consecutive_sum(num):
    """ 
    This function  do consecutive sum of numbers like bellow
    123456
    1+2+3+4+5+6
    2+1
    3
    - Arguments : 
        - num : int (number to find consecutive sum)
    - returns:
        sum : int
    """
    sum = 0
    while num:
        rem = int(num % 10)
        sum = sum + rem
        num = int(num/10)
        if num == 0:
            if sum >= 10:
                num = sum
                sum = 0
            else:
                return sum

if __name__ == "__main__":
    num = input_number()
    print(consecutive_sum(num))
