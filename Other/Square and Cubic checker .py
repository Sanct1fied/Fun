import random
import time

def squared():

    num = random.randint(0,21)
    answer = num*num
    useranswer = 0
    attempts = 0

    while useranswer != answer:
        useranswer = int(input("what is " + str(num) + " squared"))
        if attempts >= 5:
            print("the answer is", answer,"\n noob")
            break
        elif useranswer != answer:
            for i in range(5):
                print("THAT ANSWER IS WRONG!!!!!!! >>:(")
                time.sleep(0.25)
            attempts += 1
        else:
            print("yay")

def cubed():

    num = random.randint(0,5)
    answer = (num*num)*num
    useranswer = 0
    attempts = 0

    while useranswer != answer:
        useranswer = int(input("what is " + str(num) + " cubed"))
        if attempts >= 5:
            print("the answer is",answer,"\n noob")
            break
        elif useranswer != answer:
            for i in range(5):
                print("THAT ANSWER IS WRONG!!!!!!! >>:(")
                time.sleep(0.25)
            attempts += 1

        else:
            print("yay")

continued = ["yes"]

while continued not in ["no"]:
    choice = input("do you want to practice squared or cubic numbers?")
    if choice in ["squared"]:
        squared()
    else:
        cubed()
    continued = input("do you want to continue?")
