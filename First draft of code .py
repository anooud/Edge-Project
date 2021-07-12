Story = "      An AI by Meg Richards has taken over the world. \n     This is the only device not infintrated by Nachos"
Intro= "     \n           The world is ending\n     Find the kill code and save the world"
import time
print(Story)
time.sleep(5)
print(Intro)
time.sleep(5)
start = input("\nEnter password to start ")

while start != "password" :
    print("Error")
    start = input("Enter password to start ")

print("Task One")
time.sleep(2)

Intro1 = " \n Meg accidently revealed the kill code in one of her edge classes. \n   You must find out who secretly knows the kill code"

print(Intro1)
time.sleep(4)

students = ["sara", "sarim", "haya", "azmain"]
import random
r =random.randint(0,3)

x = students[r]
suspects = ["\nsara looks suspicious", "maybe sarim?", "no..no..haya?", "it's azmain right?"]
y = 0
while y < 4 :
    print(suspects[y])
    time.sleep(1)
    y = y + 1

g = input("\nYou only have 2 guesses \nWho knows the kill code? ")

for guess in range(1) :

    if g == "mohammed" :
        print("You guessed it!")
        break

    else:
        print("Incorrect")
        g = input("\nAnother Guess?")










