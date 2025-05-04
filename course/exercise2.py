#Criar funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro

def create_multi(multiplexer):
    def multi(number):
        return multiplexer * number
    return multi

double = create_multi(2)
triple = create_multi(3)
quad = create_multi(4)

print(double(2))
print(triple(2))
print(quad(2))