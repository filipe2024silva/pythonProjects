import re
import sys
import os

os.system('cls')

#cpf_user  = '746.824.890-70'.replace('.','').replace('-','')

entry = input('type you cpf [746.824.890-70]: ')
cpf_user  = re.sub(r'[^0-9]', '', entry)

sequencial_entry = entry == entry[0] * len(entry)

if sequencial_entry:
    sys.exit()

nine_digits = cpf_user[:9]
reversed_counter_1 = 10
result_1 = 0

for digit in nine_digits:
    result_1 += int(digit) * reversed_counter_1
    reversed_counter_1 -= 1

digit_1 = (result_1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

ten_digits = nine_digits + str(digit_1)
reversed_counter_2 = 11

result_2 = 0
for digit in ten_digits:
    result_2 += int(digit) * reversed_counter_2
    reversed_counter_2 -= 1

digit_2 = (result_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

generated_cpf = f'{nine_digits}{digit_1}{digit_2}'

if cpf_user == generated_cpf:
    print(f'{cpf_user} is valid')
else:
    print('Invalid cpf')