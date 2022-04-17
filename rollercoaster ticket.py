print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
   print("you can ride the rollercoaster")
   age = int(input("how old are you?"))
   if age >= 18:
     print("your ticket price is $12")  
   elif age <= 12:
     print("your ticket price is $7")    
   else:
     print("your ticket price is $10")    
     
else:
  print("you're not allowed to ride the rollercoaster")