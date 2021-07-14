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
time.sleep(5)

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

for guess in range(2) :

    if g == "mohammed" :
        print("You guessed it!")
        break

    else:
        print("Incorrect")
        g = input("\nAnother Guess? ")
        if g != "mohammed" :
            print("Nachos has taken over")
            exit()
time.sleep(3)
print("Let's go ask Mohammed!")
time.sleep(2)
print("       ____________________        ")
print("      /     Hello, I'm     \       ")
print("     /   Mohammed. Is there \      ")
print("    |     Something I can    |     ")
print("     \  help you with??     /      ")
print("      \  __________________/       ")
print("       |/                          ")

question = input("\nWhat is your question: ")


while question != "what is the kill code?" :
    question = input("\nAre you sure that is the question you want to ask?")

response = ["\nThe kill code?", "Was it 11100??", "oh wait no", "I shouldn't have said that", "What?? Kill Code I don't know any kill code"]

y = 0
while y < 5 :
    print(response[y])
    time.sleep(1)
    y = y + 1

task1conc = "    Congrats! You have the kill code. \nHowever you must enter this code in Nacho's main server "

print(task1conc)

print("\nTask Two")
time.sleep(2)

Intro2 = "         We must find Meg's secret Lab.\n    And enter the kill code in Nacho's main server."
print(Intro2)

Intro202 = "To find her secret lab, let's take a closer look at her rock collection. \n"

rocknum = input("You only have permission to read about 3 of her rocks. \nEnter a number from 1-10 to read about the rock in her rock collection: ")

class rock :
    def __init__(self, num, name, des) :
        self.num = num
        self.name = name
        self.des = des

    def __repr__(self) :
        return self.num + " " + self.name + "\n" + self.des


file = open("/Users/alanooudalthani/Documents/GitHub/Edge-Project/Rocks2.txt","r")


rock_list = []
for line in file :
    line_splitted = line.split("-")
    temp_rock = rock(line_splitted[0],
    line_splitted[1],
    line_splitted[2].rstrip('\n'))
    rock_list.append(temp_rock)
file.close()


print(rock_list[0])






