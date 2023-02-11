def add(P,  A):
    return P + A
def substract(P, A):
    return P - A
def multi(P, A):
    return P * A
def divide(P, A):
    return P / A

print("Pleas select the operation.")
print('a. Add')
print('b. Substract')
print('c. Multiplay')
print('d. Divided')

choice = input("Pleas Enter choice (a/ b/ c/ d): ")

num_1  = int(input('Pleas enter the First Number: '))
num_2 = int(input('Pleas enter the Second Number: '))

if choice == 'a':
    print(num_1, " + ", num_2, '=', add(num_1,num_2))

elif choice == 'b':
    print(num_1, '_', num_2, '= ', substract(num_1,num_2))
elif choice == 'c':
    print(num_1, '*', num_2, '=', multi(num_1,num_2))
elif choice == 'd':
    print(num_1, '/', num_2, '=', divide(num_1,num_2))

else:
    print("this is an invalid input")
