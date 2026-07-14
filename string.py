str = "Apna COllege"
print(str[2:6])
print(str[0:3])
print(str[5:len(str)])
print(str[0:])
print(str[-3:-2])
print(str[-7: ])

#function in string

str = " I Love my self"
print(str.upper())
print(str.endswith("self"))
print (str.count("I"))
print(str.capitalize())
print(str.replace("I", "Suhani"))
print(str.find("o"))
print(str.find("Suhani"))
print(str.count("I"))
print(str.isalnum())
#practice
name = input("Enter your name:")
print(len(name))
str = input("Enter your string:")
print(str.count("$"))
#Conditional statements
age = 89
if(age>18):
    print("your are ready to vote")
elif(age==18):
    print("Your age is 18, now you can vote")
else:
    print("Your age is not eligible for votting")
num = 45
if(num%2==0):
    print("Even number")
else:
    print("Odd number")