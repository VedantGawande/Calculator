from Calculator import *
# DO i need to explain this? You are intelligent enough to understand it (i'm too lazy to explain)
q = ''
user_input = 0
def user():
    global user_input
    try:
        user_input = int(input('Press 1 to add\n2 to sub\n3 to multiply\n4 to divide\n5 to power\n6 to square\n7 to cube\n8 to check even or odd\n9 to check greater or smaller\n10 to check divisiblity\n11 to show factors\n12 to check prime or not\n13 to %\n14 to prime factorize\n15 to check if perfect square\n16 to check if perfect cube\n17 to show square root\n'))
        print('')
        invalid = False
    except:
        print('Invalid input\n')
        print('...............................................')
        invalid = True
        if invalid:
            user()
while q.lower() != 'q':
    print('...............................................\n')
    user()
    lst = []
    if user_input == 1:
        no = int(input('How many numbers do you want to add? '))
        no += 1
        ans = 0
        for i in range(1,no):
            num = int(input(f'Number {i}: '))
            lst.append(num)
        add(lst)
        print('...............................................\n')
    elif user_input == 2:
        print('First input the number then input the numbers you want to subtract\n')
        no = int(input('How many numbers do you want to subtract with the first number? '))
        no += 1
        ans = 0
        for i in range(0,no):
            if i == 0:
                num = int(input(f'First number: '))
                lst.append(num)
            else:
                num = int(input(f'Number {i}: '))
                lst.append(num)
        sub(lst)
        print('...............................................\n')
    elif user_input == 3:
        no = int(input('How many numbers do you want to multiply? '))
        no += 1
        ans = 0
        for i in range(1,no):
            num = int(input(f'Number {i}: '))
            lst.append(num)
        mul(lst)
        print('...............................................\n')
    elif user_input == 4:       
        no = int(input('How many numbers do you want to divide with divisor? '))
        no += 1
        print('First input the number then input divisors\n')
        ans = 0
        for i in range(0,no):
            if i == 0:
                num = int(input('Number: '))
                lst.append(num)
            else:
                num = int(input(f'Divisor {i}: '))
                lst.append(num)
        div(lst)
        print('...............................................\n')
    elif user_input == 5:
        print('First input the number then input the power')
        no = int(input('Number: '))
        po = int(input('Power: '))
        pow(no,po)
    elif user_input == 6:
        no = int(input('Number: '))
        square(no)
        print('...............................................\n')
    elif user_input == 7:
        no = int(input('Number: '))
        cube(no)
        print('...............................................\n')
    elif user_input == 8:
        no = int(input('Number: '))
        evenodd(no)
        print('...............................................\n')
    elif user_input == 9:
        no1 = int(input('Number 1: ')) 
        no2 = int(input('Number 2: '))
        greater(no1,no2)
        print('...............................................\n')
    elif user_input == 10:
        no = int(input('Number: '))
        div = int(input('Divisor: '))
        divisible(no,div)
        print('...............................................\n')
    elif user_input == 11:
        no = int(input('Number: '))
        factors(no)
        print('...............................................\n')
    elif user_input == 12:
        no = int(input('Number: '))
        isprime(no)
        print('...............................................\n')
    elif user_input == 13:
        pc = int(input('Percentage: '))
        no = int(input('Number: '))
        percent(no,pc)
        print('...............................................\n')
    elif user_input == 14:
        no = int(input('Number: '))
        primefac(no)
        print('\n...............................................\n')
    elif user_input == 15:
        no = int(input('Number: '))
        issquare(no)
        print('\n...............................................\n')
    elif user_input == 16:
        no = int(input('Number: '))
        iscube(no)
        print('\n...............................................\n')
    
    elif user_input == 17:
        no = int(input('Number: '))
        print(sqrt(no))
        print('\n...............................................\n')
    
    else:
        print('Not a valid option\n')
        print('...............................................')
    q = input('Press q to quit: ')
