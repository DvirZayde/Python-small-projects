from Deck import Card
from Deck import Deck
from Deck import Hand
from typing import Final

MAX_DRAW: Final=15
funds = int(input("please enter initial funds: "))
deck=Deck()
dealer=Hand()
player=Hand()

#Game on loop
while True:
	#Placing bet loop
	while True:
		#Initial round
		deck.deck.extend(dealer.empty())
		deck.deck.extend(player.empty())
		deck.shuffle()
		print (f"You have : {funds}")
		bet = int(input("Please enter your bet, if you want to quit please enter 0: "))
		if bet<=funds:
			funds-=bet
			break
		else:
			print("Insufficient funds for you bet, try again")
	if bet==0:
		print(f"Game has ended, you leave with {funds}")
		break

	# Handing initial cards
	for i in range(0,2):
		dealer.hit(deck.deal_one())
		player.hit(deck.deal_one())
	print(f"Dealer's exposed card is : {dealer.cards[0]}")
	print("player's hand is :")
	print(player)

	# player's turn to play
	while True:
		move=input("If you want to hit press 1, for stay press any other key: ")
		if (move!="1"):
			break
		player.hit(deck.deal_one())
		print (f"you got: {player.cards[-1]}")
		if player.bust:
			break

	if player.bust:
		print ("Bust! You loose the round")
		continue

	# dealer's turn to play
	print(f"Dealer's second card is : {dealer.cards[1]}")
	while dealer.score<=MAX_DRAW:
		dealer.hit(deck.deal_one())
		print(f"Dealer draws: {dealer.cards[-1]}")

	
	if dealer.bust: 
		print ("Dealer Bust! you win the round!")
		funds+=(bet*2)
		continue
		
	# Counting the table	
	print (f"Dealer has {dealer.score} and player has {player.score}")
	if player.score>dealer.score:
		print ("You win the round :)")
		funds+=(bet*2)
	elif player.score==dealer.score:
		print ("It's a tie :|")
		funds+=bet
	else:
		print("You loose the round :(")







