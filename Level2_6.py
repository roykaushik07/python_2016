import math
C = 50
H = 30
D = []
result = []
Range = int(input('How many values you want to enter: '))
for i in range(0, Range):
    m = int(input('Enter the number: '))
    D.append(m)

for j in range(0,Range):
    mul_value = 2 * C * D[j]
    div_value = mul_value/H
    final_value = int(math.sqrt(div_value))
    result.append(final_value)

print('The Final result is ' , result)

