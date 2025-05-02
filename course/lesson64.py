import random
import sys

nine_digits = ''
for i in range(9):
    nine_digits += str(random.randint(0, 9))

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
print(generated_cpf)

sys.exit()