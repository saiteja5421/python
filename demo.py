# #Multiplication and sum of two numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# multiple_of_two_numbers=num1*num2
# sum_of_two_numbers=num1+num2
# print("multiplication of two numbers:{}".format(multiple_of_two_numbers))
# print("sum of two numbers:{}".format(sum_of_two_numbers))

# #print charactres from the string that are present an even index number 
# word="msystechnologies"
# for i in range(len(word)):
#     if i % 2 == 0:
#         print(word[i])

# #Display numbers divisible by 5 from the list in list
# numbers=[10,20,33,46,55]
# divisible_by_5=[]
# for num in numbers:
#     if num % 5 == 0:
#         divisible_by_5.append(num)
# print(divisible_by_5)

# #Display numbers dividible by 5 using list comparastion.
# s=[i for i in numbers if i % 5 == 0]
# print(s)


# # to check palidrome are not
# a=678                             
# b=str(a)
# c=b[::-1]
# if a==int(c):
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

# #reverse a list
# list_of_any=[10,20,45,33,45,67,88]
# list_of_any.reverse()
# print(list_of_any)


# #reverse a list
# list_of_any=[10,20,45,33,45,67,88]
# a=[]
# for i in range(len(list_of_any)-1,-1,-1):
#     a.append(list_of_any[i])
# print(a)

s=(1,2,[3,4],(5),{6,7,8})
print(s[3])

s="it\'s tech_chill"
print(s.capitalize())

a={}
b={1}
print(type(a))
print(type(b))
print(type(a)==type(b))