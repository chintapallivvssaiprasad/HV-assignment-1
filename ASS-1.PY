product_1= int(input("Enter number-1: "))
product_2= int(input("Enter number-2: "))
product_3= int(input("Enter number-3: "))
product_4= int(input("Enter number-4: "))
product_5= int(input("Enter number-5: "))
total = product_1 + product_2 + product_3 + product_4 + product_5

z = open("Data-1.txt","w")

if (product_1 > 0) and (product_2 > 0) and (product_3 > 0) and (product_4 > 0) and (product_5 > 0):
    print("The sum of all numbers :",total)
    print("The sum of all numbers :",total,file=z)
else:
    print("Enter the POSITIVE NUMBERS: ")
