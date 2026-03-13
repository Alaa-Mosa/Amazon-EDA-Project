  #---------1 Create variables to store your name, age, height, and whether you are a student. Print their types.--------#
name=("A'laa MOsa")
Age=(20)
height=(160)
Are_student=True
print(type(name))
print(type(Age))
print(type(height))
print(type(Are_student))

   #--------2: Ask the user for two numbers and print their sum, difference,product, and division.--------# 
num1= (float (input("enter the frist Num")))
num2=(float (input("enter the secondNum")))
sum=num1+num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
print(num1)
print(num2)
print(sum)
print(difference)
print(product)
print(division)
   #---------3 Take an intger input and check if it’s positive, negative, or zero-------#
num=(int(input(" enter num")))
if num > 0:
 print("positive")
elif num<0:
 print("negative")
else:
 print("zero")
  #--------4 Print all even numbers between 1 and 20.-------#
for a in range(0,22):
 if a%2==0:
     print(a)
  #--------5 Ask the user to guess a number (secret = 7) until they get it right.
secret = 7
guess = int(input("Guess the number"))
while guess != secret:
    print("Wrong, try again")
    guess = int(input("Guess the number"))
print("This is the secret number  ")
   #----------6 Create a text file named data.txt, write a few lines, then read and print its content.--#
with open("data.txt", "w") as file: 
  file.write(" few line \n")
  file.write("=few line \n")
  file.write("few line \n")
  with open("data.txt", "r") as file:
    content = file.read()
    print(content)
  #----------7 Create a list of 5 numbers, print the sum, maximum, and reverse it.-------#
      
g =[9,8,7,6,5] 
g.reverse()
print(g)
print(max(g))
print(sum(g))  
  #---------------8 Create a tuple of city names, and print the first and last city.-------#
cities =("Ankara","Istanbol","Bursa","Izmir")
print(cities[0])
print(cities[-1])
  #---------9 Given two sets of student names, find those who are in both groups.#
group1 ={"ali","omer","amr","malak" }
group2={"amr","alaa","salma","asmaa"}
print(group1 & group2 )
     #------------10 Handle division by zero using try and except.-------#
try:
 num= int(input("enter the num"))
 result =10/num
 print(result)
except ValueError:
  print("Not a vaild ")
except ZeroDivisionError:
  print("Can not divide by zero")
  #---------------11 celsius_to_fahrenheit(c): Converts a temperature in Celsius to Fahrenheit.-----#

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def average_temperature(temp_list, unit):
    avg = sum(temp_list) / len(temp_list)  
    if unit == "C":
        return avg
    elif unit == "F":
        return celsius_to_fahrenheit(avg)
    else:
        return None
    
def highest_temperature(temp_list, unit):
     high = max(temp_list) 
     if unit == 'C':
        return high
     elif unit == 'F':
        return celsius_to_fahrenheit(high)
     else:
        return None
try:
 user = input("Enter temperatures in Celsius, separated by commas: ")
 temps = [float(x.strip()) for x in user.split(",")]
except ValueError:
 print("Error: enter only numbers separated by commas.")


A= average_temperature(temps, "C")
B=average_temperature(temps, "F")
C=highest_temperature(temps, "C")
D=highest_temperature(temps, "F")
print("A",A)
print("B",B)
print("C",C)
print("D",D)


