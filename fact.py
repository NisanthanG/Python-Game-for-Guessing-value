def Factorial(number):
    factorial = 1 # base value
    if number < 0 :
        factorial = 0
    elif number == 0: # == equal / = assigning value
        factorial = 1
    else:
        for num in range(1,number+1): # range(1,6) = [1,2,3,4,5]
            factorial *=  num
    return factorial # 5! = 1*2*3*4*5

def triangular(number):
    triangle = 0 # base value
    if number < 1 :
        triangle = 0
    else:
        for num in range(1,number+1): # range(1,6) = [1,2,3,4,5]
            triangle +=  num
    return triangle # triang(5) = 1+2+3+4+5
    
        


