"""Check Armstrong number or not"""

def check_armstrong(num):
    """
    This function find the sum of all digits in number and
    make sum of all this numbers cube
    - Arguments : 
        - num : int
    - return :
        total : int
    """
    total = 0 
    while num:
        rem = int(num%10)
        total = total + (rem*rem*rem)
        num = int(num/10)
    return total
  
if __name__ == "__main__":
    """
    Execution starts from here
    take the number input from user to check  this number is armstrong or not
    """
    num = int(input("Enter number to check armstrong or not : "))
    res = check_armstrong(num)
    if res == num:
        print("YES")
    else:
        print("NO")

