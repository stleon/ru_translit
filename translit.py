#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def do_translit(word):
	"""Latin transliteration of the Russian alphabet"""
	my_dict = { 
		u'а':'a',
		u'б':'b',
		u'в':'v',
		u'г':'g',
		u'д':'d',
		u'е':'e',
		u'ё':'e',
		u'ж':'zh',
		u'з':'z',
		u'и':'i',
		u'й':'y',
		u'к':'k',
		u'л':'l',
		u'м':'m',
		u'н':'n',
		u'о':'o',
		u'п':'p',
		u'р':'r',
		u'с':'s',
		u'т':'t',
		u'у':'u',
		u'ф':'f',
		u'х':'h',
		u'ц':'ts',
		u'ч':'ch',
		u'ш':'sh',
		u'щ':'shch',
		u'ы':'y',
		u'ь':"'",
		u'ъ':"'",
		u'э':'e',
		u'ю':'yu',
		u'я':'ya',
		' ':'-',
	}
	new_word = ""
	for symbol in word.lower().strip():
		if symbol in my_dict:
			new_word = new_word + my_dict[symbol]
		else:
			new_word = new_word + symbol
	return new_word


def main():
	try:
		word = ""
		for i in sys.argv[1:]:
			word = word + i + " "
		print do_translit(word.decode('utf-8'))
	except IndexError:
		print 'usage: add some words'

if __name__=='__main__':
	main()