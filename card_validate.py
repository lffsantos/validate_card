#coding:utf-8
'''
    >>> validar = CardValidate('visa','4408 0412 3456 7893')
    >>> validar.validate()
    True
    >>> validar = CardValidate('visa','8417 1234 5678 9112')
    >>> validar.validate()
    False
    >>> validar = CardValidate('amex','378282246310005')
    >>> validar.validate()
    True
    >>> validar = CardValidate('mastercard','5105105105105106')
    >>> validar.validate()
    False
    >>> validar = CardValidate('desconhecido','5105105105105106')
    >>> validar.validate()
    False
    >>> validar = CardValidate('mastercard','5105105105105100')
    >>> validar.validate()
    True
    >>> validar = CardValidate('discover','6011111111111117')
    >>> validar.validate()
    True
    >>> print list_flags()
    ['amex', 'discover', 'mastercard', 'visa']
    
'''

import argparse
from card import Card
from file_util import list_flags

class CardValidate():


	def __init__(self,flag,number):
		self.card = Card(flag,number.replace("-","").replace(" ","").strip())

	def validate(self):
		return self.card.is_valid()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--flag", type=str, help="Flag of Credit Card")
	parser.add_argument("-n", "--number", type=str, help="Number of Credit Card")
	args = parser.parse_args()
	
	if not args.flag:
		print "Please enter the credit card flag"
		exit(1)
	if not args.number:
		print "Please enter the credit card number"
		exit(1)

	validar = CardValidate(args.flag,args.number)
	if args.flag in list_flags():
		print args.flag, args.number, "[ Válido ] " if validar.validate() else "[ Inválido ]"
	else:
		print "Flag Not Found"
		print "Disponible Flags - "  + str(list_flags())
