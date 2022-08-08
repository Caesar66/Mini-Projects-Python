import re
import sys

def getWords(file_name):
	with open(file_name, 'r') as f:
		words = f.readlines()
		word_list = []
		for word in words:
			w = word.strip(' \n')
			word_list.append(w.lower())
		return word_list

def setWords(new_file, words):
	with open(new_file, 'w') as f:
		keys_ = list(words.keys())
		words_ = list(words.values())
		for key in keys_:
			f.write("%s\n" %key)
		f.write("\n")
		for word in words_:
			f.write("%s\n" %word)
		return None

def selectWords(words, minsize, condition):
	new_word_list = {}
	for word in words:
		if len(word) < minsize:
			continue
		if condition.search(word):
			continue
		new_word_list[word] = ''.join(sorted(word))
	return new_word_list

def main(file_name, new_file_name):
	r = re.compile('[\'áéíóúàèòìùçãẽõĩũäëïöüâêîôûÿỳýŷ]')
	word_list = getWords(file_name)
	#print(word_list)
	new_word_list = selectWords(word_list, 4, r)
	#print(new_word_list)
	#print(len(new_word_list))
	setWords(new_file_name, new_word_list)
	return

#file_name = "word_list.txt"
#new_file_name = "new_word_list.txt"
#main(file_name, new_file_name)
main(sys.argv[1], sys.argv[2])
