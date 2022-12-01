# python program to check whether a string is palindrome or not

string = input("Enter a string to check palindrome or not: ")
if string.lower() == string[::-1].lower():
    print("it's a palindrome")
else:
    print("Not a palindrome")


# python function to multiply all the numbers in a list
def multiply_all_numbers_in_list(l):
    multiply_all_numbers = 1
    for i in l:
        multiply_all_numbers *= i
    return multiply_all_numbers


print(multiply_all_numbers_in_list([1, 2, 3, 4, 5]))


# python function that accepts a string and calculates the upper case and lower case letters
def count_uppercase_lowercase(string):
    uppercase_letters = 0
    lowercase_letters = 0
    string1 = string.replace(" ", "")
    for i in string1:
        if i == i.upper():
            uppercase_letters += 1
        elif i == i.lower():
            lowercase_letters += 1

    return f'uppercase letters: {uppercase_letters}\nlowercase_letters: {lowercase_letters}'


print(count_uppercase_lowercase("The Upper Case"))


# python function that takes a list and returns a new list with unique elements

def unique_elements(l):
    return list(set(l))


print(unique_elements([1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]))


# output =[1,2,3,4]


# function that checks a number is in a given range 1 to 100

def in_given_range(number):
    for i in range(1, 101):
        if i == number:
            return f"Number {number} is inclusive in range 1 and 100"
    else:
        return f'Number {number} is Not inclusive in range 1 and high 100'


print(in_given_range(20))


# function that checks a number is in a given range


def in_given_range(low, high, number):
    for i in range(low, high + 1):
        if i == number:
            return f"Number is inclusive in range {low} and {high}"
    else:
        return f'Number is Not inclusive in range {low} and high {high}'


print(in_given_range(10, 100, 20))

z = set('abc')
print(z)
z.add('san')
print(z)
z.update(set(['p', 'q']))

print(z)

print(4.3 == 4)
