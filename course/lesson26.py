"""
s-string
d-int
f-float
.<digits of number>f
x or X - Hexa
(Character)(><^)(quantity)
> - left
< - right
^ - center
Signal - + or -
Ex.: 0 >- 100,.1f
Conversion flags - !r !s !a
"""
variable = 'ABC'
print(f'{variable}')
print(f'{variable:0>10}')
print(f'{variable:0<10}.')
print(f'{variable:0^10}.')
print(f'{10.555558888:.1f}')
print(f'Hexa of number 1500 is {1500:08X}')