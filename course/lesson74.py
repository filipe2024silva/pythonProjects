#Closure-> Manter estado entre chamadas de função sem usar variáveis globais ou classes
def create_welcome(msg):
    def welcome(name):
        return f'{msg}, {name}!'
    return welcome #quando a função é representada sem () será indicado o valor da memória onde essa função está armazenada


welcome_morning = create_welcome('Good morning')
welcome_evening = create_welcome('Good evening')

print(welcome_morning('Filipe Silva'))
print(welcome_evening('Pedro'))
print('--------------')

for name in ['Pedro', 'Catarina', 'Filipe']:
    print(welcome_morning(name))