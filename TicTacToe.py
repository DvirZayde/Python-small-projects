from IPython.display import clear_output

#Displaying the current board
def display(loc_list):
	# Clearing last move

	print('\n'*100) # for terminal
	clear_output() # for jupiter
	#Displaying current board
	print(f" {loc_list[0]} | {loc_list[1]} | {loc_list[2]} ")
	print("-----------")
	print(f" {loc_list[3]} | {loc_list[4]} | {loc_list[5]} ")
	print("-----------")
	print(f" {loc_list[6]} | {loc_list[7]} | {loc_list[8]} ")

#update data according to players input	
def update_board(loc_list, flag):
	index = input("please choose your move according to the free options:")
	while (index.isdigit()==False or int(index) not in range(1,10) or loc_list[int(index)-1].isdigit()==False):
		index = input("Your choose is not valid please choose an open place on the board:")
	index = int(index)
	if flag:
		loc_list[index-1]="X"
	else:
		loc_list[index-1]="O"

#Checking if there is a winner after the last move
def check_board(loc_list, flag):
	for x in [0,1,2]:
		if (loc_list[x]==loc_list[x+3] and loc_list[x]==loc_list[x+6]):
			return True
	for x in [0,3,6]:
		if (loc_list[x]==loc_list[x+1] and loc_list[x]==loc_list[x+2]):
			return True
	if (loc_list[0]==loc_list[4] and loc_list[0]==loc_list[8]):
		return True
	if (loc_list[6]==loc_list[4] and loc_list[6]==loc_list[2]):
		return True
	return False

#Checking if the board is full with no winner
def tie_check(loc_list):
	for x in loc_list:
		if x.isdigit():
			return False
	return True

#Entry message
def entry():
	print("This is a Tic Tac Toe game, first player is 'X' and second is 'O'")
	input("Press ENTER to start the game")

#Checking if the players want to play again
def another_game():
	while True:
		answer=input("Do you want another game? 'Y' or 'N' :")
		if answer=='Y':
			return False
		elif answer=='N':
			return True
		else:
			print("Invalid answer please try again")

##main----

#the board's "date"
loc_list=[str(x) for x in range(1,10)]
#flag that indicate wich of the players turn it is
flag=True
#check if the players want another game 
end=False

entry()

while not end:
	while True:
		display(loc_list)
		update_board(loc_list,flag)
		if check_board(loc_list, flag):
			if flag:
				print("First player has won!")
			else:
				print("Second player has won!")
			end=True
			break
		if tie_check(loc_list):
			print("It's a tie :\\ ")
			break
		flag= not flag
	end=another_game()
	if not end:
		loc_list=[str(x) for x in range(1,10)]
		flag=True
