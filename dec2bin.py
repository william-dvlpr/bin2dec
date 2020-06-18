# coding: UTF-8

decimal = int(input('Enter decimal number: '))

binary = "" 

while decimal >= 1 :
    remainder = decimal % 2
    binary = str(remainder) + binary # inverted order
    decimal = decimal // 2

print("Converted to binary: ", binary)
