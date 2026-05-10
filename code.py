import time
import os
import requests
import msvcrt

def end():
    os.system("cls")
    print("Exiting",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    os.system("cls")
    print("T",end="")
    time.sleep(0.15)
    print("H",end="")
    time.sleep(0.15)
    print("A",end="")
    time.sleep(0.15)
    print("N",end="")
    time.sleep(0.15)
    print("K",end=" ")
    time.sleep(0.15)
    print("Y",end="")
    time.sleep(0.15)
    print("O",end="")
    time.sleep(0.15)
    print("U",end=" ")
    time.sleep(0.15)
    print("^_^\n",end=" ")
    time.sleep(1.25)
    exit()

def mainScreen():
    os.system("cls")
    time.sleep(0.5)
    print("What do you want to do:\n")
    time.sleep(0.55)
    print("a) Know the weather of your place.")
    time.sleep(0.35)
    print("b) Guess the weather of a random place.")
    time.sleep(0.35)
    print("c) Exit\n")
    time.sleep(0.35)

    ch = msvcrt.getch().decode()
    while(ch!='a' and ch!='b' and ch!='c'):
        time.sleep(0.5)
        print("Kindly Enter a valid imput(a, b, c).")
        time.sleep(0.5)
        ch = msvcrt.getch().decode()
    
    if ch == 'c':
        time.sleep(0.25)
        end()

def welcome():
    os.system("cls")
    time.sleep(0.5)
    print("Welcome",end=" ")
    time.sleep(0.4)
    print("to",end=" ")
    time.sleep(0.4)
    print("the",end=" ")
    time.sleep(0.4)
    print("Weather",end=" ")
    time.sleep(0.4)
    print("App",end=" ")
    time.sleep(1)
    mainScreen()

welcome()