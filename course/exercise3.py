import os
os.system('cls')

questions = [
    {
        'Question': 'How many are 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Response': '4'
    },
    {
        'Question': 'How many are 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Response': '25'
    },
    {
        'Question': 'How many are 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Response': '5'
    },
]

qtt_correct = 0

for question in questions:
    print('Question:', question['Question'])
    print()
    
    options = question['Options']
    
    for i, option in enumerate(options):  
        print(f'{i}) {option}')
    print()
    
    response = input('Type your choice: ')
    
    correct = False
    response_int = None
    qtt_options = len(options)
    
    if response.isdigit():
        response_int = int(response)
        
    if response_int is not None:
        if response_int >= 0 and response_int <= qtt_options:
            if options[response_int] == question['Response']:
                correct = True
                qtt_correct += 1
    
    print()
    if correct:
        print('Correct')
    else:
        print('Incorrect')
        
    print()
print(f'You have {qtt_correct} corrects of {len(questions)} questions')

        
    
    