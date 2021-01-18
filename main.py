# neverAFK - Jacob Tornatta 2020
# This is a program that uses random, time, and pyautogui to generate random inputs on the mouse
# so that the user never appears "away from keyboard" on apps such as Slack and Discord.
import random
import time
import pyautogui  # 1920 x 1080 by default
import tkinter

tkinter._test()

print("Welcome! Keep in mind that each cycle is about 6 seconds.")

def mouse_mover(timer):  # Function that moves the mouse

    while timer > 0:
        time.sleep(3)
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        pyautogui.moveTo(num1, num2, duration=3)
        timer += -1
        if timer < 0:
            break

    inputx = input("Enter 'x' to end the script, enter 's' to start again: ")
    if inputx == "x":
        exit()
    else:
        main()

def main():

    input1 = input("Enter 's' to begin script, enter 'x' to exit: ")

    if input1 == "s":
        input2 = int(input("Enter amount of cycles: "))
        mouse_mover(input2)
    elif input1 == "x":
        exit()
    else:
        main()

main()

def exit():
    print("")

# todo: figure out how to make a gui for this program (Tkinter) and use Pyinstaller to distribute
