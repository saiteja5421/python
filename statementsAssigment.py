st = 'Print only the words that start with s in this sentence'
for i in st.split(" "):
	if i[0]=='s':
		print(i)

for i in range(11):
	if(i % 2==0):
		print(i)

my_list=[i for i in range(1,51) if i % 3 == 0]
print(my_list)

st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
	if len(i) % 2 == 0:
		print(i)
my_FizzBuzz=[]
for i in range(1,101):
	if i % 3==0 and i %5==0:
		my_FizzBuzz.append("FizzBuzz")
	elif i % 3==0:
		my_FizzBuzz.append("Fizz")
	elif i % 5==0:
		my_FizzBuzz.append("Buzz")
	else:
		my_FizzBuzz.append(i)
print(my_FizzBuzz)

st = 'Create a list of the first letters of every word in this string'
my_string=[x[0] for x in st.split()]
print(my_string)