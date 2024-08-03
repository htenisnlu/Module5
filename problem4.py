# Hikmet Tenis
# 08/02/2024
# This program prints messages based on the divisibility of numbers from 1 to 50.

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)