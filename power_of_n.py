""" WRITE A PROGRAM TO FIND Nth  POWER OF GIVEN NUMBER """

def power_of_n(num,power):
    """ 
    This function calculate the nth power of a given number
    - Arguments : 
        - num : int
        - power : int
    """
    if power==0:
        return 1
    else:
        return int(num) * power_of_n(num,power-1)

print(power_of_n(10,4))



# num = 10
# power = 2
# ans = 1
# for i in range(power):
#     ans = ans * num
# print(ans)