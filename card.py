from file_util import get_propertie_flag

class Card:

	def __init__(self, flag, number):
		self.number = number
		self.properties = get_propertie_flag(flag)		

	def start_with(self):
		return 0 if isinstance(self.properties, int) else self.properties[0]
		

	def len_card(self):
		return 0 if isinstance(self.properties, int) else self.properties[1]


	def is_valid(self):
		if self.validate_card_number():
			if isinstance(self.len_card(), int):
				return False
			for x in self.len_card():
				if len(self.number) == x:
					return True

			for x in self.start_with():
			    if self.number.startswith(str(x)):
			        return True

			return False
		else:
			return False


	def validate_card_number(self):
		number_card = [ int(n) for n in self.number]
		number_card = number_card[::-1]
		for i in xrange(len(number_card)):
			if i%2 !=0:
				number_card[i] *= 2
			if number_card[i] > 9:
				number_card[i] -= 9  
					
		return True if sum(number_card)%10 == 0 else False