import os

secret_word = "house"
correct_words = ''
number_of_times = 0

while True:
    
    word_user = input('Type a word: ')
    number_of_times += 1
    
    if len(word_user) > 1:
        print('Just type one word.')
        continue
    
    if word_user in secret_word:
        correct_words += word_user
        
    format_word = ''
    for secret_charecter in secret_word:
        if secret_charecter in correct_words:
            format_word += secret_charecter
        else:
            format_word += '*'
    
    print(format_word)
    
    if format_word == secret_word:
        os.system('cls')
        print('Congratulations! You win')
        print('The secret word is', secret_word)
        print('You try:', number_of_times)
        correct_words = ''
        number_of_times = 0
        
