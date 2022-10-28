""" 
WRITE A PROGRAM TO FIND ALL PRIME NUMBERS UPTO INPUTED RANGE
"""

def define_range():
    """ 
    This function define range of prime numbers which we want
    - return:
        - start : starting range
        - end : end range
    """
    start,end = map(int,input("Enter Start and end range : ").split())
    return start,end

def get_all_prime(start,end):
    """ 
    This function gives all prime numbers  between given range
    - Arguments :
        - start : starting range
        - end : ending range
    return : 
        - primes : list of prime numbers between given range
    """
    primes = list()
    for i in range(start,end):
        if i >= 2:
            for j in range(2,i):
                if( (i%j) == 0):
                    break
            else:
                primes.append(i)
    return primes

def main():
    start,end = define_range()
    prime_numbers = get_all_prime(start,end)
    print(prime_numbers)

if __name__ == "__main__":
    """ 
    Execution Starts from here
    """
    main()
