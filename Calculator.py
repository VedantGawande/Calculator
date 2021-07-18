# Update V1.6
# Date - 17/07/2021
# Newly added features-
#   Finding speed
#   Finding velocity
#   Finding accelaration 
#   Finding a value using equations of motion
#   Some bug fixes

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
        print(f'{num} is divisible by {divisor} by {num/divisor}')
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
        print('Processing....Might take several minutes')
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
            print(f'x {num}')
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
    print(f'perimeter of rectangle with length : {length}, breadth: {breadth} is\n{ans} units') 
def sqperi(side):
    ans = 4*side
    print(f'perimeter of square with side: {side} is {ans} units')
def perfpolyperi(no_side, side):
    if no_side >= 2:
        print('A polygon has at least 3')
        return False
    ans = no_side * side
    print(f'Perimeter of a perfect polygon with {no_side} sides is {ans} units')
def arearect(length, breadth):
    ans = length * breadth
    print(f'area of rectangle length : {length}, breadth: {breadth} is\n{ans} unit^2')

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
    print(f'Area of the traingle is {ans} unit^2')
def areatri_h(a,b,c):
    '''           
         /\             
        /  \     
     a /    \ b    
      /      \     
     /________\ 
          c
    '''
    try:
        s = (a+b+c)/2
        ans = sqrt(s*(s-a)*(s-b)*(s-c))
        print(f'Area of the traingle is {ans} unit^2')
    except:
        print('PLease enter valid sides...')
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
    ans = height*(a+b)/2
    print(f'Area of the trapazium is {ans} unit^2')


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

# Simple Physics Calculations
def speed(distance, time):
    v = distance/time
    print(f'speed: {v} m/s')

def vel(displacement, time):
    v = displacement/time
    print(f'velocity: {v} m/s')

def xlr8(v, u, t):
    a = (v-u)/t
    print(f'accelaration: {a} m/s^2')

# Motion equation

# -------------------------------------------

# First equation (took me 2 and half hour+ lol)         - 13/07

# Functions for first equation
def canf(u_,v_,a_,t_):
    '''
    Checks if needed values are given or not
    '''
    # checking if 4 values are given
    if ((u_==False) and (v_==False) and (a_==False) and (t_==False)):
        return False

    # checking if 3 value are given
    elif ((u_==True) and (v_==False) and (a_==False) and (t_==False)):
        return False
    elif ((u_==False) and (v_==True) and (a_==False) and (t_==False)):
        return False
    elif ((u_==False) and (v_==False) and (a_==True) and (t_==False)):
        return False
    elif ((u_==False) and (v_==False) and (a_==False) and (t_==True)):
        return False

    # checking if 2 values are given
    # i.e uv, ua, ut, va, vt, at = true respectivly -
    elif ((u_==True) and (v_==True) and (a_==False) and (t_==False)):
        return False
    elif ((u_==True) and (v_==False) and (a_==True) and (t_==False)):
        return False
    elif ((u_==True) and (v_==False) and (a_==False) and (t_==True)):
        return False
    elif ((u_==False) and (v_==True) and (a_==True) and (t_==False)):
        return False
    elif ((u_==False) and (v_==True) and (a_==False) and (t_==True)):
        return False
    elif ((u_==False) and (v_==False) and (a_==True) and (t_==True)):
        return False

    # if the above possibilites are False, then we can go for our next step i.e finding which values are given
    else:
        return True
def whichf(u_,v_,a_, t_):
    '''
    Checks if 4 values are given
    if not then, it tells which values are given
    '''
    uva = False
    uat = False
    uvt = False
    vat = False
    if ((u_==False) and (v_==True) and (a_==True) and (t_==True)):
        vat = True

    elif ((u_==True) and (v_==False) and (a_==True) and (t_==True)):
        uat = True

    elif ((u_==True) and (v_==True) and (a_==False) and (t_==True)):
        uvt = True

    elif ((u_==True) and (v_==True) and (a_==True) and (t_==False)):
        uva = True
    # if the above possibilites are True, then we can go for our next step i.e C A L C U L A T I O N!
    # if the above possibilites are False, then it mens all 4 values are given
    else:
        uva = True
        vat = True
        uat = True
        uvt = True
    
    return uva, uat, uvt, vat 

def f_uva(u,v,a):
    t = (v-u)/a
    print(f'''
    We know, v = u + at

    (v) - u = (u + at) - u

    (v - u)/a = (at)/a

    t = (v - u)/a

    So, t = ({v} - {u}){a}

    t = ({v - u})/{a}

    t = {t}
    ''')
def f_uat(u,a,t):
    v = u + a*t
    print(f'''
    We know, v = u + at
    
    So, v = {u} + {a}*{t}

    v = {u} + {a*t}

    v = {v}
    ''')
def f_uvt(u,v,t):
    a = (v-u)/t
    print(f'''
    We know, v = u + at

    (v) - u = (u + at) - u
    
    (v - u)/t = (at)/t
    
    a = (v - u)/t

    So, a = ({v} - {u}){t}

    a = ({v-u})/{t}

    a = {a}
    ''')
def f_vat(v,a,t):
    u = v - a*t
    print(f'''
    We know, v = u + at

    (v) - u = (u + at) - u
    
    (v - u) - v = (at) - v
    
    -(-u) = -(at - v)

    u =  v - at

    So, u = {v} - {a}*{t}

    u = {v} - {a*t}

    u = {u}
    ''')

# Main function of first equation
def first_eq():
    u_ = False
    v_ = False
    a_ = False
    t_ = False
    qu = input('Press 1 if you know initial velocity or press 0: ')
    qv = input('Press 1 if you know final velocity or press 0: ')
    qa = input('Press 1 if you know accelaration or press 0: ')
    qt = input('Press 1 if you know time or press 0: ')
    if qu == '1':
        u_ = True
    if qv == '1':
        v_ = True
    if qa == '1':
        a_ = True
    if qt == '1':
        t_ = True
    if ((u_ ==True) and (v_ ==True) and (a_ ==True) and (t_ ==True)):
            print("You know all the values...")
            return False
    # from this function we can know if at least 3 values are known (check the dunction for more details)
    can = canf(u_,v_,a_,t_)

    uva = False
    uat = False
    uvt = False
    vat = False

    if can == False:
        print("at least 3 values are needed...")
    else:
        # form this function we can know what values are given
        which = whichf(u_,v_,a_, t_)

        for i in range(3):
            if i == 0:
                if which[i] == True:
                    uva = True
            if i == 1:
                if which[i] == True:
                    uat = True
            if i == 2:
                if which[i] == True:
                    uvt = True
            if i == 3:
                if which[i] == True:
                    vat = True

        if uva == True:
            u = float(input('initial velocity(m/s): '))
            v = float(input('final velocity(m/s): '))
            a = float(input('accelaration(m/s^2): '))
            f_uva(u,v,a)
        if uat == True:
            u = float(input('initial velocity(m/s): '))
            a = float(input('accelaration(m/s^2): '))
            t = float(input('time(s): '))
            f_uat(u,a,t)
        if uvt == True:
            u = float(input('initial velocity(m/s): '))
            v = float(input('final velocity(m/s): '))
            t = float(input('time(s): '))
            f_uvt(u,v,t)
        if vat == True:
            v = float(input('final velocity(m/s): '))
            a = float(input('accelaration(m/s^2): '))
            t = float(input('time(s): '))
            f_vat(v,a,t)


# -------------------------------------------


# Second equation (took me 1 and 1/4 th hour approximately) - 16/07

# Functions for second equation
def can_s(u_,s_,a_,t_):
    '''
    Checks if needed values are given or not
    '''
    # checking if 4 values are given
    if ((u_==False) and (s_==False) and (a_==False) and (t_==False)):
        return False

    # checking if 3 value are given
    elif ((u_==True) and (s_==False) and (a_==False) and (t_==False)):
        return False
    elif ((u_==False) and (s_==True) and (a_==False) and (t_==False)):
        return False
    elif ((u_==False) and (s_==False) and (a_==True) and (t_==False)):
        return False
    elif ((u_==False) and (s_==False) and (a_==False) and (t_==True)):
        return False

    # checking if 2 values are given
    # i.e uv, ua, ut, va, vt, at = true respectivly -
    elif ((u_==True) and (s_==True) and (a_==False) and (t_==False)):
        return False
    elif ((u_==True) and (s_==False) and (a_==True) and (t_==False)):
        return False
    elif ((u_==True) and (s_==False) and (a_==False) and (t_==True)):
        return False
    elif ((u_==False) and (s_==True) and (a_==True) and (t_==False)):
        return False
    elif ((u_==False) and (s_==True) and (a_==False) and (t_==True)):
        return False
    elif ((u_==False) and (s_==False) and (a_==True) and (t_==True)):
        return False

    # if the above possibilites are False, then we can go for our next step i.e finding which values are given
    else:
        return True
def which_s(u_,s_,a_, t_):
    '''
    Checks if 4 values are given
    if not then, it tells which values are given
    '''
    usa = False
    uat = False
    ust = False
    sat = False
    if ((u_==False) and (s_==True) and (a_==True) and (t_==True)):
        sat = True

    elif ((u_==True) and (s_==False) and (a_==True) and (t_==True)):
        uat = True

    elif ((u_==True) and (s_==True) and (a_==False) and (t_==True)):
        ust = True

    elif ((u_==True) and (s_==True) and (a_==True) and (t_==False)):
        usa = True
    # if the above possibilites are True, then we can go for our next step i.e C A L C U L A T I O N!
    # if the above possibilites are False, then it mens all 4 values are given
    else:
        usa = True
        sat = True
        uat = True
        ust = True
    
    return usa, uat, ust, sat 

def s_usa():
    '''I'll add this later if I can do this'''
    print("Sorry...I can't do this. Please do it by yourself")
def s_uat(u,a,t):
    s = u*t + 1/2 *a*t*t
    print(f'''
    We know, s = ut + 1/2 * at^2

    So, s = {u}*{t} + 1/2 * {a}*{t}^2

    s = {u}*{t} + 1/2 * {a}*{t}^2

    s = {u*t} + {1/2*a*t**2}

    s = {s}
    ''')
def s_ust(u,s,t):
    a = (2*s - 2*u*t)/t**2
    print(f'''
    We know, s = ut + 1/2 * at^2

    s - ut = 1/2 * t^2 * a

    (s - ut)*2 = t^2 * a    -Cross multiplication

    a = (2s - 2ut)/t^2      -Cross multiplication

    So, a = (2*{s} - 2*{u}*{t})/{t}^2

    a = ({2*s} - {2*u*t})/{t**2}

    a = {2*s - 2*u*t}/{t**2}

    a = {a}
    ''')
def s_sat(s,a,t):
    u = -1/2*a*t - s/t
    print(f'''
    We know, s = ut + 1/2 * at^2
    
    s - ut = 1/2 * at^2

    - ut = 1/2 * at^2 -s
    
    - ut/t = (1/2 * at^2 - s)/t
    
    u = 1/2 * at - s/t

    so, u = 1/2 * {a}*{t} - {s}/{t}

    u = 1/2 * {a*t} - {s/t}

    u = {1/2*a*t} - {s/t}

    u = {u}
    ''')


# Main function of second equation
def second_eq():
    u_ = False
    s_ = False
    a_ = False
    t_ = False
    qu = input('Press 1 if you know initial velocity or press 0: ')
    qs = input('Press 1 if you know distance travelled or press 0: ')
    qa = input('Press 1 if you know accelaration or press 0: ')
    qt = input('Press 1 if you know time or press 0: ')
    if qu == '1':
        u_ = True
    if qs == '1':
        s_ = True
    if qa == '1':
        a_ = True
    if qt == '1':
        t_ = True
    if ((u_ ==True) and (s_ ==True) and (a_ ==True) and (t_ ==True)):
            print("You know all the values...")
            return False
    # from this function we can know if at least 3 values are known (check the dunction for more details)
    can = can_s(u_,s_,a_,t_)
       
    usa = False
    uat = False
    ust = False
    sat = False

    if can == False:
        print("at least 3 values are needed...")
    else:
        # form this function we can know what values are given
        which = which_s(u_,s_,a_, t_)

        for i in range(3):
            if i == 0:
                if which[i] == True:
                    usa = True
            if i == 1:
                if which[i] == True:
                    uat = True
            if i == 2:
                if which[i] == True:
                    ust = True
            if i == 3:
                if which[i] == True:
                    sat = True

        if usa == True:
            print("Sorry...I can't do this. Please do it by yourself")
            return False
        if uat == True:
            u = float(input('initial velocity(m/s): '))
            a = float(input('accelaration(m/s^2): '))
            t = float(input('time(s): '))
            s_uat(u,a,t)
        if ust == True:
            u = float(input('initial velocity(m/s): '))
            s = float(input('distance travelled(m): '))
            t = float(input('time(s): '))
            s_ust(u,s,t)
        if sat == True:
            s = float(input('distance travelled(m): '))
            a = float(input('accelaration(m/s^2): '))
            t = float(input('time(s): '))
            s_sat(s,a,t)


# -------------------------------------------

# Third equation                                           - 17/07

# Functions for third equation
def can_t(u_,s_,a_,v_):
    '''
    Checks if needed values are given or not
    '''
    # checking if 4 values are given
    if ((u_==False) and (s_==False) and (a_==False) and (v_==False)):
        return False

    # checking if 3 value are given
    elif ((u_==True) and (s_==False) and (a_==False) and (v_==False)):
        return False
    elif ((u_==False) and (s_==True) and (a_==False) and (v_==False)):
        return False
    elif ((u_==False) and (s_==False) and (a_==True) and (v_==False)):
        return False
    elif ((u_==False) and (s_==False) and (a_==False) and (v_==True)):
        return False

    # checking if 2 values are given
    # i.e uv, ua, ut, va, vt, at = true respectivly -
    elif ((u_==True) and (s_==True) and (a_==False) and (v_==False)):
        return False
    elif ((u_==True) and (s_==False) and (a_==True) and (v_==False)):
        return False
    elif ((u_==True) and (s_==False) and (a_==False) and (v_==True)):
        return False
    elif ((u_==False) and (s_==True) and (a_==True) and (v_==False)):
        return False
    elif ((u_==False) and (s_==True) and (a_==False) and (v_==True)):
        return False
    elif ((u_==False) and (s_==False) and (a_==True) and (v_==True)):
        return False

    # if the above possibilites are False, then we can go for our next step i.e finding which values are given
    else:
        return True
def which_t(u_,s_,a_, v_):
    '''
    Checks if 4 values are given
    if not then, it tells which values are given
    '''
    usa = False
    uav = False
    usv = False
    sav = False
    if ((u_==False) and (s_==True) and (a_==True) and (v_==True)):
        sav = True

    elif ((u_==True) and (s_==False) and (a_==True) and (v_==True)):
        uav = True

    elif ((u_==True) and (s_==True) and (a_==False) and (v_==True)):
        usv = True

    elif ((u_==True) and (s_==True) and (a_==True) and (v_==False)):
        usa = True
    # if the above possibilites are True, then we can go for our next step i.e C A L C U L A T I O N!
    # if the above possibilites are False, then it mens all 4 values are given
    else:
        usa = True
        sav = True
        uav = True
        usv = True
    
    return usa, uav, usv, sav 

def t_usa(u,s,a):
    v = sqrt(2*a*s + u**2)
    print(f'''
    We know, 2as = v^2 - u^2

    2as + u^2 = v^2

    v = sqroot(2as + u^2)

    so, v = sqroot(2*{a}*{s} + {u}^2)

    v = sqroot({2*a*s} + {u**2})

    v = sqroot({2*a*s + u**2})

    v = {v}
    ''')
def t_uav(u,a,v):
    s = (v**2 + u**2)/2*a
    print(f'''
    We know, 2as = v^2 - u^2

    s = (v^2 - u^2)/2a

    so, s = ({v}^2 - {u}^2)/2*{a}

    s = ({v**2} - {u**2})/{2*a}

    s = {v**2 - u**2}/{2*a}

    s = {s}
    ''')
def t_usv(u,s,v):
    a = (v**2 - u**2)/2*s
    print(f'''
    We know, 2as = v^2 - u^2

    a = (v^2 - u^2)/2s

    so, a = ({v}^2 - {u}^2)/2*{s}

    a = ({v**2} - {u**2})/{2*s}

    a = {v**2 - u**2}/{2*s}

    a = {a}
    ''')
def t_sav(s,a,v):
    u = sqrt(-2*a*s + v**2)
    print(f'''
    We know, 2as = v^2 - u^2

    2as - v^2 = - u^2

    -(-u^2) = -(2as - v^2)

    u = sqroot(-2as + v^2)

    so, u = sqroot(-2*{a}*{s} + {v}^2)

    u = sqroot({-2*a*s} + {v**2})

    u = sqroot({-2*a*s + v**2})

    u = {u}
    ''')


# Main function of third equation
def third_eq():
    u_ = False
    s_ = False
    a_ = False
    v_ = False
    qu = input('Press 1 if you know initial velocity or press 0: ')
    qs = input('Press 1 if you know distance travelled or press 0: ')
    qa = input('Press 1 if you know accelaration or press 0: ')
    qv = input('Press 1 if you know time or press 0: ')
    if qu == '1':
        u_ = True
    if qs == '1':
        s_ = True
    if qa == '1':
        a_ = True
    if qv == '1':
        v_ = True
    if ((u_ ==True) and (s_ ==True) and (a_ ==True) and (v_ ==True)):
            print("You know all the values...")
            return False
    # from this function we can know if at least 3 values are known (check the dunction for more details)
    can = can_t(u_,s_,a_,v_)
       
    usa = False
    uav = False
    usv = False
    sav = False

    if can == False:
        print("at least 3 values are needed...")
    else:
        # form this function we can know what values are given
        which = which_t(u_,s_,a_, v_)

        for i in range(3):
            if i == 0:
                if which[i] == True:
                    usa = True
            if i == 1:
                if which[i] == True:
                    uat = True
            if i == 2:
                if which[i] == True:
                    ust = True
            if i == 3:
                if which[i] == True:
                    sat = True

        if usa == True:
            u = float(input('initial velocity(m/s): '))
            s = float(input('distance travelled(m): '))
            a = float(input('accelaration(m/s^2): '))
            s_usa(u,s,a)
        if uat == True:
            u = float(input('initial velocity(m/s): '))
            a = float(input('accelaration(m/s^2): '))
            v = float(input('final velocity(m/s): '))
            s_uat(u,a,v)
        if ust == True:
            u = float(input('initial velocity(m/s): '))
            s = float(input('distance travelled(m): '))
            v = float(input('final velocity(m/s): '))
            s_ust(u,s,v)
        if sat == True:
            s = float(input('distance travelled(m): '))
            a = float(input('accelaration(m/s^2): '))
            v = float(input('final velocity(m/s): '))
            s_sat(s,a,v)





# Previous Update dates-
# V1.0 - 26/01/2021
# V1.1 - 8/03/2021
# I don't care about 2 and 3 So,
# V1.4 - 26/05/2021
    # Update included -
    # Geometry operations
    # Simple Intrest
    # Compound Intrest
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
