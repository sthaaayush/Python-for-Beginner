#Fresh Start to new domain
print("Hello Python")

#Understanding the datatypes
intTyp=1
floatTyp=23.40
charTyp='20'
strTyp="Python" #String value can be enclosed in '' or ""
boolTyp=True

print(type(intTyp))
print(type(floatTyp))
print(type(charTyp))
print(type(strTyp))
print(type(boolTyp))

#Taking input from user using input()
userInput=input("Enter your name:")
print("Your name is ", userInput)

#Type conversion
typ1="234" #Before Conversion
print("%s is " %typ1, type(typ1))

typ2=int(typ1)  #After Conversion
print("%s is " %typ2, type(typ2))