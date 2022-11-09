""" WRITE A PROGRAM TO CONVERT DECIMAL NUMBER TO BINARY  """

def reverse_num(num):
    """ 
    This functino reverse the string
    - Arguments : 
        -num : str (string which we want to reverse)
    """
    return num[::-1]

def decimal_to_binary(bin,num):
    """ 
    This function convert the decimal number to Binary number in reverse order
    - Arguments : 
        - bin : str
        - num : int
    """
    if num == 0:
        return bin
    else:
        return decimal_to_binary( (bin+str(num % 2)),num//2)
        
res = decimal_to_binary("",4)
print(reverse_num(res))



# num = 27
# bin = 0
# while num:
#     rem = num%2
#     bin = (bin*10) + rem 
#     num = num/2

# print(bin)



