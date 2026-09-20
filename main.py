count = ""
itog = 0
one = int(input("назови первое число: "))
count = input("назови знак: \n1)+ \n2)- \n3)* \n4)/ \n5)= \nОтвет: ")
two = int(input("назови второе число: "))
if count == "+":
    itog = one + two
elif count == "-":
    itog = one - two
elif count == "*":
    itog = one * two
elif count == "/":
    itog = one / two
while count != "=":
    count = input("назови знак: \n1)+ \n2)- \n3)* \n4)/ \n5)= \nОтвет: ")
    if count == "=":
        print(itog)
        break
    ee = int(input("напиши число: "))
    if count == "+":
        itog = itog + ee
    elif count == "-":
        itog = itog - ee
    elif count == "*":
        itog = itog * ee
    elif count == "/":
        itog = itog / ee
    elif count == "=":
        print(itog)
