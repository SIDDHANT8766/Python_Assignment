def ChkPrime(No):

    Result = 0
    
    for i in range(2,No):
        if(No % i == 0):
            return False
        else:
            Result = No

    return Result   
   