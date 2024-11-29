#if condition
val1=10
if(val1>5):
    print("%d is greater than 5" %val1)

# if and else
val2=int(input("Enter a number: "))
if(val2%2==0):
    print("%d is even number" %val2)
else:
    print("%d is odd number" %val2)

#elif ladder
val3=input("Enter the day: ")
val3=val3.upper()
if(val3=="SUNDAY" or val3=="SATURDAY"):
    print("It's Weekend")
elif(val3=="MONDAY" or val3=="TUESDAY"):
    print("You have a meeting")
elif(val3=="WEDNESDAY" or val3=="THURSDAY" or val3=="FRIDAY"):
    print("Normal working day")
else:
    print("Invalid day")

#while loop
val4=1
while val4<=10:
    print(val4, end=",") #end="<separator>" allows to print in single line with separator
    val4+=1
print()

#for loop
for i in range(0,6): #range defines the loop iteration but second parameter is excluded ps: can use range(6)
    print(i, end=" ")
print()

for i in range(0,10,2): #third parameter defines the step difference between two number
    print(i, end=" ")

print()

#break & continue
sum=0
for i in range(10):
    if(i%2==0):
        sum+=i
        continue #back to look
    elif(sum>10):
        print("Breaking out of loop...")
        break #break out of loop
print("Sum of even number ",sum)

#pass
for i in range(5):
    pass #pass is placeholder where code is not suppose to be empty