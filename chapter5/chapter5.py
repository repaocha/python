#!/usr/bin/python
# -*- coding:utf-8 -*-
cars=['audi','bmw','subaru','toyota']

for car in cars:
     if car=='bmw':
     	  print(car.upper())
     else:
       print(car.title())


requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies!")


answer=17
if answer!=42:
    print("That is not the correct answer.Please try again!")


banned_user=['andrew','carolina','david']
user='marie'
if user in banned_user:
     print(user.title()+",you can't post a response.")
if user not in banned_user:
     print(user.title()+",you can post a response if you wish.")


age=19
if age >= 18:
     print("You are old enough to votel!")
     print("Have you registered to vote yet?")
else:
     print("Sorry,You are too yuong to vote!")
     print("Please register to vote as you turn 18!")


age=12
if age<4:
    print("Your admission cost is free")
elif age<18:
    print("Your admission cost is 5 dollars")
else:
    print("Your admission cost is 10 dollars")


requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")
print("Finished making your pizza!")


requested_topping=[]
if requested_topping:
      for requested_topping in requested_topping:
           print("Adding "+requested_topping+".")
      print("Finished making your pizza!")
else:
      print("Are you sure you want a plain pizza?")


available_topping=['mushrooms','olives','green peppers','peppers','pineapple','extra cheese']
requested_topping=['mushrooms','french fries','extra cheese']
for requested_topping in available_topping:
     if requested_topping in available_topping:
         print("Adding "+requested_topping+".")
     else:
         print("Sorry,we don't have "+requested_topping+".")