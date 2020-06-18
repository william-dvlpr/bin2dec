# coding: UTF-8

reply = input('[1] - decimal to binary\n[2] - binary to decimal\n')

if reply == '1':
    decimal = int(input('Enter decimal number: '))
    binary = "" 
    while decimal >= 1 :
        remainder = decimal % 2
        binary = str(remainder) + binary # inverted order
        decimal = decimal // 2

    print('Converted to binary:', binary)

elif reply == '2':
    binary = input('Enter binary number: ')
    position = len(binary) - 1
    decimal = 0
    for i in binary:
        decimal += int(i) * 2**position
        position -= 1

    print('Converted to decimal:', decimal)    

else:
    print('Invalid input') 
