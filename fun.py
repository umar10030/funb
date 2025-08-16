def total_caclc(bill_amount,tip_prec):
    total = bill_amount*(1 + 0.01*tip_prec)
    total = round(total, 2)
    print(f"Total amount to be paid: ${total}")

total_caclc(150, 20)
just_a_test = 1

# activity 2
def cube(number):
    return number*number*number
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))

#activity 3

def facrtorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        return x * facrtorial(x - 1)
print(facrtorial.__doc__)
print("the facrtorial of 0:", facrtorial(0))
print("the factorial of1:", facrtorial(1))
print("the factorial of 2:", facrtorial(2))
print("the factorial of 5:", facrtorial(5))
print("the factorial of 10:", facrtorial(10))