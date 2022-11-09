""" WRITE A PROGRAM TO CHECK THE NUMBER IS PALINDROME OR NOT """

def reverse_number(num,rev=0):
    """ 
    This function reverse the number
    - Arguments : 
        - num : int (inputed number which we want to reverse)
        - rev : int (reverse number store here)
    """
    if not num:
        return rev
    else:
        rem = num %10
        rev = (rev*10)+rem
        return reverse_number(num//10,rev)

def check_palindrome(num1,revs):
    if num1 == revs:
        print("palindrome")
    else:
        print("Not palindrome")


def main():
    num1 = 121
    revs = reverse_number(num1)
    check_palindrome(num1,revs)

if __name__ == "__main__":
    """ 
    Execution starts from here
    """
    main()
