1.
print("My", "Name", "Is", "King", sep="$$")
2.
name1,name2,name3 = input("Enter three names: ").split(",")
print("name1:", name1)
print("name2:", name2)
print("name3:", name3)
3.
print(f"{5.26459884:.2f}")
4.
year=2023
quantity=3
price=450
print(f"I have bought{quantity} footballs for {price:.2f}£ , in the year {year}.")
5.
sentence="i have bought 3 footballs for 450.00£ , in the year 2023."
print(sentence[0])
6.
sentence=" i have bought 3 footballs."
print(len(sentence))
7.
from datetime import date
print(date.today())
8.
import random
print(random.randint(1,100))
9.
import random
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(random.randint(a, b))
10.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
