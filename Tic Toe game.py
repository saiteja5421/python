# def lesser_of_two_even(a,b):
# 	if a % 2==0 and b % 2==0:
# 		if a<b:
# 			return a
# 		else:
# 			return b
# 	else:
# 		if a>b:
# 			return a
# 		else:
# 			return b

# print(lesser_of_two_even(2,4))
# print(lesser_of_two_even(2,5))

# def animal_crackers(string):
# 	s=string.split()
# 	if s[0][0].lower() == s[1][0].lower():
# 		return True
# 	else:
# 		return False

# print(animal_crackers("Levelheaded Liama"))
# print(animal_crackers("Crazy Kangaroo"))

# def makes_twenty(a,b):
# 	if a == 20 or b ==20:
# 		return True
# 	elif a+b == 20:
# 		return True
# 	else:
# 		return False
# print(makes_twenty(20,10))
# print(makes_twenty(12,8))

# print(makes_twenty(2,3))
# def old_macdonald(string):
# 	s=string.capitalize()
# 	s1=s[:3]+s[3].upper()+s[4:]
# 	return s1
# print(old_macdonald("macdonald"))

# def master_yoda(string):
# 	l=string.split()
# 	a=[]
# 	for i in range(len(l)):
# 		a.append(l.pop())
# 	return " ".join(a)


# print(master_yoda('I am home')) #--> 'home am I'
# print(master_yoda('We are ready'))

# def almost_there(n):
# 	for i in range(1,11):
# 		if abs(i+n) == 100:
# 			return True
# 		elif n-i ==100:
# 			return True
# 		elif i+n ==200:
# 			return True
# 		elif n-i==200:
# 			return True
# 	return False
# print(almost_there(90)) #--> True
# print(almost_there(104)) #--> True
# print(almost_there(150)) #
# print(almost_there(209)) 
# print(almost_there(95.5))


# def has_33(l):
# 	for i in range(len(l)):
# 		if i<len(l)-1:
# 			if l[i]==3 and l[i+1]==3:
# 			    return True
# 	return False
# print(has_33([1, 3, 3]))# → True
# print(has_33([1, 3, 1, 3]))# → False
# print(has_33([3, 1, 3]))

# def paper_doll(s):
# 	string=''
# 	for i in s:
# 		string+=i*3

# 	return string

# print(paper_doll('Hello'))# --> 'HHHeeellllllooo'
# print(paper_doll('Mississippi'))

# def blackjack(a,b,c):
#     l=[a,b,c]
#     l1=sum(l)
#     if l1 <= 21:
#     	return l1
#     elif a == 11 or b == 11 or c == 11:
#     	s=l1-10
#     	if s<=21:
#     		return s 
#     else:
#     	return "BUST"
# print(blackjack(5,6,7)) #--> 18
# print(blackjack(9,9,9))# --> 'BUST'
# print(blackjack(9,9,11))

# print(abs(100-104))


# def prime_numbers():
# 	n=2
# 	prime=[]
# 	for i in range(2,101):
# 		for j in range(2,i):
# 			if i%j==0:
# 				break
# 		else:
# 			prime.append(i)
# 	print(len(prime))
# prime_numbers()


# def vol(a):
# 	return (4*(3.14)*((a)**3))/3

# print(vol(2))

# def ran_check(a,b,c):
# 	for i in range(b+1,c+1):
# 		if i == a:
# 			return True
# 	else:
# 		return False
# print(ran_check(5,5,7))
# def up_low(string):
# 	s=string.replace(" ","")
# 	upper=0
# 	lower=0
# 	for i in s:
# 		if i.isupper():
# 			upper+=1
# 		elif i.islower():
# 			lower+=1
# 	return "upper letters are {} lower letters are {}".format(upper,lower)
# print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

# def unique_list(l):
# 	return list(set(l))
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# def multiply(*args):
# 	m=1
# 	for i in args[0]:
# 		m=m*i
# 	return m
# print(multiply([1,2,3,-4,2]))

# print('hello'[::-1])

import string

# def ispangram(str1,alphabet=string.ascii_lowercase):
# 	s=str1.replace(" ","")
# 	count=0
# 	for i in set(s):
# 		if i in alphabet:
# 			count+=1
# 	if count==26:
# 		return "its a pangram"
# 	else:
# 		return False
# print(ispangram("The quick brown fox jumps over the lazy doggg"))
#from ipython import clear_output
def display_board(board):
 	print(board[1]+"|"+board[2]+"|"+board[3])
 	print("-"+"|"+"-"+"|"+"-")
 	print(board[4]+"|"+board[5]+"|"+board[6])
 	print("-"+"|"+"-"+"|"+"-")
 	print(board[7]+"|"+board[8]+"|"+board[9])
test_board = [' ',' ','O',' X',' ','O',' ',' ','X',' ']


def player_input():
	player1=""
	player2=""
	choice="wrong"
	while choice not in ["X","O"]:
 		choice=input("player1 choices X or O: ")
 		if choice not in ["X","O"]:
 			print("choice X or O") 
 		elif choice == "X":
 			player1="X"
 			player2="O"
 		else:
 			player1="O"
 			player2="X"
	return (player1,player2)

#position=int(input("choice a position from (1-9): "))

def place_marker(test_board,player,position):
	test_board[position]=player


def win_check(board,marker):
	return ((board[1]==board[2]==board[3]==marker) or 
		    (board[4]==board[5]==board[6]==marker) or
		    (board[7]==board[8]==board[9]==marker) or
		    (board[1]==board[5]==board[9]==marker) or
		    (board[3]==board[2]==board[7]==marker) or
		    (board[1]==board[4]==board[7]==marker) or
		    (board[2]==board[5]==board[8]==marker) or
		    (board[3]==board[6]==board[9]==marker))

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations! player1 You have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break