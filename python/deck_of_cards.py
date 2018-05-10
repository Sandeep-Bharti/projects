from random import shuffle
class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"

c = Card("A", "hearts")
c2 = Card("10", "Diamonds")
c3 = Card("K", "Spades")
# print(c)
# print(c2)
# print(c3)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)


	def _deal(self, num):
		count = self.count()
		actualRemove = min([count, num])
		if count == 0:
			raise ValueError("All cards been dealt")
		cards = self.cards[-actualRemove:]
		self.cards = self.cards[:-actualRemove]
		return cards

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)
		return self

d = Deck()
d.shuffle() 
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(hand)
print(d.cards)
# print(d.cards)