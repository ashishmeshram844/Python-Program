""" WRITE A PROGRAM TO FIND SUM OF DIGIT OF A GIVEN NUMBER """

def find_sum_of_digit(sum,num):
    """ 
    This function calculate the sum of digit of given numbers .
    - Arguments : 
        - sum : int
        - num : int
    """
    if num == 0:
        return sum
    else:
        return find_sum_of_digit(sum =sum+(num%10),num = num//10)


print(find_sum_of_digit(0,1235465458454545))

