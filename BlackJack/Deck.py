import random

ranks=("Two", "Three", "Four", "Five" ,"Six", "Seven", "Eighth", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
types = ("Haerts", "Diamonds", "Spades", "Clubs")
values={"Two":2, "Three":3, "Four":4, "Five":5 ,"Six":6, "Seven":7, "Eighth":8, "Nine":9, "Ten": 10, "Jack": 10, "Queen": 10, "King":10, "Ace": 11}

class Card:
	
	def __init__(self, type, rank):
		self.type=type
		self.rank=rank
		self.value=values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.type

class Deck:

	def __init__ (self):
		self.deck=[]
		for i in ranks:
			for j in types:
				self.deck.append(Card(j,i))
	
	def deal_one(self):
		return self.deck.pop(0)

	def shuffle(self):
		random.shuffle(self.deck)


class Hand:
	
	def __init__(self):
		self.cards=[]
		self.score=0
		self.aces=0
		self.bust=False

	def hit(self, another_card:Card):
		self.cards.append(another_card)
		self.score+=another_card.value
		if another_card.rank=="Ace":
			self.aces+=1
		if self.score>21:
			if self.aces>0:
				self.score-=10
				self.aces-=1
			else:
				self.bust=True

	def empty(self):
		self.score=0
		self.aces=0
		self.bust=False
		temp=[]
		while len(self.cards) > 0:
			temp.append(self.cards.pop())
		return temp

	def __str__(self):
		ans=""
		for card in self.cards:
			ans += f"{card} \n"
		return ans

