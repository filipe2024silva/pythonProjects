#iterations, how cycle For work in back
text = 'Filipe' 
iterator = iter(text) #__iter__()
print(text)

while True:
    try:
        word = next(iterator)
        print(word)
    except StopIteration:
        break