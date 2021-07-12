Story = "     An AI by Meg Richards has taken over the world. \n     This is the only device not infintrated by Nachos"
Intro= "     The world is ending\n     Find the kill code and save the world"
import time
print(Story)
time.sleep(5)
print(Intro)
time.sleep(5)
start = input("Enter password to start ")

while start != "password" :
    print("Error")
    start = input("Enter password to start ")

print("Task One")



