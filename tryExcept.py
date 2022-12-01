for i in ["a",2,"c"]:
	try:
		print(i**2)
	except:
		print("i must be integers")

def ask():
	while True:
		try:
			result=int(input("please emter a number:"))
			break
		except:
			print("Must be interger")
			continue
		finally:
			print("all Done")
			

ask()