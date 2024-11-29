intList=[2,5,8,1,5,4] #defining list
print(type(intList)) 
print(intList) #printing whole list

#iterating through list
for i in intList:
    print(i, end=',')
print()

#accessing and modifying
mixList=[2,2.50,'a','python']
print(mixList[0]) #accessing value at index 0
print(mixList)
mixList[2]=34 #modifying value at index 2
print(mixList)

tempList=[5,'t',3,4]

#list built-in function
mixList.extend(tempList) #extending list with another list
print(mixList)

mixList.insert(2,'arr') #insert value at given index
print(mixList)  

mixList.append("pycharm") #append value at last
print(mixList)

mixList.pop() #pop the last element
print(mixList)

mixList.remove('arr') #remove first occurrence of that value
print(mixList)
