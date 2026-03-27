# --coding:utf-8--
import os

nDividers = 0
os.system("cls")
print("Input an integer positive number")
ulNumber = int(input())
print(f"The number {ulNumber} has the folowing dividers:")
for i in range(1, ulNumber + 1):
    if ulNumber % i == 0:
        print(i, end=" ")
        nDividers += 1
print("")
match (nDividers):
    case 0 | 1:
        print(f"The number {ulNumber} is neither composite nor prime")
    case 2:
        print(f"The number {ulNumber} is prime")
    case _:
        print(f"The number {ulNumber} is composite")
