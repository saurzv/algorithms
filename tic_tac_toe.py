def greet() :
	""" Function to greet and give the instruction."""

	print("\n-xx-Welcome to the tic-tac-toe game-xx-\n\n"
		"Position of the board is as follow\n"
		"Enter these key words to enter X and O\n")
	print("\ta1 | a2 | a3\n"
		"\t-----------\n"
		"\tb1 | b2 | b3\n"
		"\t-----------\n"
		"\tc1 | c2 | c3\n")

def decide_turn(t):
	""" Function to decide whose turn is this. """

	if t%2 == 1 :
		return 1
	else :
		return 2

def print_board(a):
	""" Function to print the board each turn"""

	print(f"\t{a[0][0]} | {a[0][1]} | {a[0][2]}\n"
		"\t---------\n"
		f"\t{a[1][0]} | {a[1][1]} | {a[1][2]}\n"
		"\t---------\n"
		f"\t{a[2][0]} | {a[2][1]} | {a[2][2]}\n")

def check_and_insert(a, usr_inpt, turn):
	""" Function to check if the entry is correct and put it on the board. """

	if len(usr_inpt) != 2 :
		return False

	p = usr_inpt[0]
	q = int(usr_inpt[1])
	
	if p < 'a' or p > 'c':
		return False

	if q < 1 or q > 3 :
		return False

	x = {'a':0,'b':1,'c':2}

	if a[x[p]][q - 1] != " ":
		return False

	if turn == 1 :
		a[x[p]][q - 1] = 'X'
	else :
		a[x[p]][q - 1] = 'O'


	return True

arr = [[" " for i in range(3)] for j in range(3)] # array to store the input

def check_winner(a):
	""" Check for winner at each turn. """
	
	for row in a :
		if row.count(row[0]) == 3 and row[0] != " ":
			return True

	for i in range(3):
		if (a[0][i] == a[1][i] == a[2][i] != " ") :
			return True

	if(a[0][0] == a[1][1] == a[2][2] != " ") :
		return True

	if(a[0][2] == a[1][1] == a[2][0] != " ") :
		return True

	return False

def take_input():
	""" Function to take input from the players. """
	
	t = 1
	while(t != 9) :
		turn = decide_turn(t)
		print("Player {}'s turn\n"
			"Enter :".format(turn), end=" ")
		usr_inpt = input()
		conf = check_and_insert(arr,usr_inpt,turn)
		if conf :
			print_board(arr)
			if check_winner(arr):
				print("Player {} wins".format(turn))
				quit()
			t += 1
		else :
			print("Invalid input")

def start() :
	greet()
	take_input()

start()