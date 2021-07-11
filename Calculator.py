# Update V1.5 or something idk
# Date - 28/08/2021
# Update includes-
#   More detailed doc strings / Detailed explaination
#   Removing unnecessary code / Making it shorter
#   A bit more organised, I guess
#   And added some very bad jokes cuz i'm bored and there is no internet and this pc sucks

# Update V1.5.1
# Date - 04/07/2021
# Newly Added feature-
#   Finding area of triangle through Heron's Formula

# Update V1.5.2
# Date - 11/07/2021
# Newly Added features-
#   Km/h to M/s
#   M/s to Km/h

from math import sqrt

# Operations
def add(nums):
    '''
    It will take a list or tuple as argument
    Then it will add all the items in the argument
    '''
    ans = 0
    for i in nums:
        ans = i + ans
    print(ans)
def sub(nums):
    '''
    It will take number(s) as argument(s)
    it will subtract all other numbers with the first number
    '''
    ans = nums[0]
    for i in nums:
        if i != nums[0]:
            ans = ans - i
        else:
            pass
    print(ans)
def mul(nums):
    """
    It multiplies every number with other
    here ans = 1 as a default value, because if we multiply nums by 0 it will become 0 and 1 * x = x
    """
    ans = 1
    for i in nums:
        ans = i * ans
    print(ans)
def div(nums):
    '''
    It takes argument(s) = number(s)
    it will divide all other numbers with the first number
    '''
    ans = nums[0]
    for i in nums:
        if i != nums[0]:
            ans = ans / i
        else:
            pass
    print(ans)


# old functions... you can ignore this
# ---------------
def add2(*nums):
    '''
    It will take num(s) as argument(s)
    Then it will add all the arguments
    '''
    ans = 0
    for i in nums:
        ans = i + ans
    print(ans)
def sub2(*nums):
    '''
    It takes argument(s) = number(s)
    it will subtract all other numbers with the first number
    '''
    ans = nums[0]
    for i in nums:
        if i != nums[0]:
            ans = ans - i
        else:
            pass
    print(ans)
def mul2(*nums):
    """
    It multiplies every number with other
    here ans = 1 because if we multiply nums by 0 it will become 0
    """
    ans = 1
    for i in nums:
        ans = i * ans
    print(ans)
def div2(*nums):
    '''
    It takes arguments = numbers
    it will divide all other numbers with the first number
    '''
    if nums[0] == 0:
        raise Exception
    ans = nums[0]
    for i in nums:
        if i != nums[0]:
            ans = ans / i
        else:
            pass
    print(ans)
# ----------------


# easy peasy functions (idk, if that is a word lol)
def evenodd(num1):
    if num1 % 2 == 0:
        print(num1, 'is even')
    else:
        print(num1, 'is odd')
def greater(num1,num2):
    if num1 > num2:
        print(f'{num1} > {num2}')
    elif num1 < num2:
        print(f'{num1} < {num2}')
    else:
        print(f'{num1} = {num2}')

# easy squared
def pow(num1, pow):
    '''It takes number and power and gives the result'''
    ans = num1 ** pow
    print(f'{num1}^{pow} = {ans}')
def square(num):
    print(f'{num}^2 = {num ** 2}')
def cube(num):
    print(f'{num}^3 = {num ** 3}')

# Super duper easy
def divisible(num,divisor):
    if num % divisor == 0:
        print(f'{num} is divisible by {divisor}')
    else:
        print(f'{num} is not divisible by {divisor}')

# This should be medium (it definetly took me 5 minutes and not 5 hours)
def factors(num):
    '''
    This function runs a for loop between 1 and the num + 1
    and checks if the number is divisble by number in the range and prints it
    '''
    for i in range(1,num+1):
        if num % i == 0:
            print(i)
    return True
def isprime(num):
    '''
    It finds all the factors of the number
    Then it checks if it's factors are 2
    if they are it is prime number
    if they are not then its not a prime numbers
    '''
    nu = num + 1
    factor = []
    if num > 10000:
        print('Processing....')
    for i in range(1,nu):
        if num % i == 0:
            factor.append(i)
    if len(factor) == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
def primefac(num):
    '''
    num --> prime factors
    It takes the number and checks if it is divisible by prime numbers i.e 2,3,5,7
    if num is divisible by prime numbers if it is it will divide num to the prime number
    this process loops till num is not 1
    '''
    # here i have printed 1 else e.g it will print x 2 x 5
    # with this it will be printed like this 1 x 2 x 5
    print('1 ', end='')
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            print(f'x 2 ', end='')
        elif num % 3 == 0:
            num = num / 3
            print(f'x 3 ', end='')
        elif num % 5 == 0:
            num = num / 5
            print(f'x 5 ', end='')
        elif num % 7 == 0:
            num = num / 7
            print(f'x 7 ', end='')
        else:
            print(f'x {int(num)}')
            num = num / num
        # print('')

def percent(percent,num):
    '''
    No need to explain this
    '''
    ans = percent/100 * num
    print(ans)

# Copy paste previous code
def iscube(num):
    '''
    it first prime factorises the num 
    and checks if the factors are in the quantity of 3 or multiple of 3
    I could have done something like this-
    ans = cqrt(num)
    if ans == int(ans):
        is_cube == True
    else:
        is_cube == false
    '''
    no = num
    is_cube = False
    var2 = 0
    var3 = 0
    var5 = 0
    var7 = 0
    while num != 1:
        if num % 2 == 0:
            var2 += 1
            num = num / 2
        elif num % 3 == 0:
            num = num / 3
            var3 +=1
        elif num % 5 == 0:
            num = num / 5
            var5 += 1
        elif num % 7 == 0:
            num = num / 7
            var7 += 1
        else:
            num = num / num
        
    if ((var2 % 3 == 0 )and(var2 != 0)):
        is_cube = True
    if ((var3 % 3 == 0 )and(var3 != 0)):
        is_cube = True
    if ((var5 % 3 == 0 )and(var5 != 0)):
        is_cube = True
    if ((var7 % 3 == 0 )and(var7 != 0)):
        is_cube = True
    else:
        is_cube == False

    if is_cube:
        print(f'{no} is a cube')
    else:
        print(f'{no} is not a cube')
def issquare(num):
    '''same this as iscube just instead of checking for multiple of 3 it checks if it is multiple of 2'''
    is_cube = False
    no = num
    var2 = 0
    var3 = 0
    var5 = 0
    var7 = 0
    while num != 1:
        if num % 2 == 0:
            var2 += 1
            num = num / 2
        elif num % 3 == 0:
            num = num / 3
            var3 +=1
        elif num % 5 == 0:
            num = num / 5
            var5 += 1
        elif num % 7 == 0:
            num = num / 7
            var7 += 1
        else:
            num = num / num
        
    if ((var2 % 2 == 0 )and(var2 != 0)):
        is_cube = True
    if ((var3 % 2 == 0 )and(var3 != 0)):
        is_cube = True
    if ((var5 % 2 == 0 )and(var5 != 0)):
        is_cube = True
    if ((var7 % 2 == 0 )and(var7 != 0)):
        is_cube = True
    else:
        is_cube == False

    if is_cube:
        print(f'{no} is a square')
    else:
        print(f'{no} is not a square')



# Geometry
def rectperi(length, breadth):
    ans = 2 * (length + breadth)
    print(f'perimeter of rectangle with length : {length}, breadth: {breadth} is\n{ans}') 
def sqperi(side):
    ans = 4*side
    print(f'perimeter of square with side: {side} is {ans}')
def perfpolyperi(no_side, side):
    ans = no_side * side
    print(f'Perimeter of a perfect polygon with {no_side} is {ans}')
def arearect(length, breadth):
    ans = length * breadth
    print(f'area of rectangle length : {length}, breadth: {breadth} is\n{ans}')

# I TYPED THIS SHAPES, so that you know how the shpae looks like
# (I don't think anyone reading this doesn't know the shapes of these polygons, but anyway i like wasting my time)
def areatri(height, base):
    r'''
    h = height
    b = base
                ___
        /\       |        
       /  \      |
      /    \     | h
     /      \    |   
    /________\  _|_ 
    
    |----b----|   
    '''
    ans = 1/2 * height * base
    print(f'Area of the traingle is {ans}')
def areatri_h(a,b,c):
    '''           
         /\             
        /  \     
     a /    \ b    
      /      \     
     /________\ 
          c
    '''
    s = (a+b+c)/2
    ans = sqrt(s(s-a)(s-b)(s-c))
    print(f'Area of the traingle is {ans}')
def areatrap(height, a, b):

    r'''
    h = height
    a = side
    b = parrellel side

       |-------a--------|
       _________________
      /                 |\
     /                  |h\
    /___________________|__\
    
    |------------b-----------|
    '''
    ans = height(a+b)/2
    print(f'Area of the trapazium is {ans}')


# Data handling
def simintrest(principal, rate, time):
    si = principal * rate/100 * time
    amount = si + principal
    print(f'Total amount after {time} year(s) at the rate of intrest {rate}% per annum will be {amount}\nTotal intrest will be {si}')

# This is compound intrest not communist intrest(unless you copy it)
def comintrest(principal, rate, time):
    amount = principal * (1 + rate/100)**time
    ci = amount - principal
    print(f'Total amount after {time} year(s) at the rate of intrest {rate}% per annum will be {amount}\nTotal intrest will be {ci}')

# Km/h to M/s
def M_s(km):
    m = km*1000
    s = 3600
    ans = m/s
    print(f'{km} km/h --> {ans} m/s')
# M/s to Km/h
def Km_h(m):
    km = m/1000
    h = 1/3600
    ans = km/h
    print(f'{m} m/s --> {ans} km/h')



# Previous large Update dates-
# V1.0 - 26/01/2021
# V1.1 - 8/03/2021
# I don't care about 2 and 3 So,
# V1.4 - 26/05/2021
