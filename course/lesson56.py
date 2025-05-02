phrase = '  Hello world, we are together       '
words_list = phrase.split(', ')
words_list_2 = []

print(words_list)

for i, phrase in enumerate(words_list):
    words_list_2.append(words_list[i].strip())# delete spaces in start and end of the string

join_phrases = '-'.join('abc')
print(join_phrases)