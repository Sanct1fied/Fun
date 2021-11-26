# ver 1.0 26/11/21
import webbrowser
from tkinter import *
from tkinter import font

# tkinter setup
root = Tk()
root.title("GAP Project 2021-2022")
root.geometry("1500x1500")


## defining functions for zoom links ##
# maths
def Algorithm():
    webbrowser.open('https://www.thinkautomation.com/eli5/what-is-an-algorithm-an-in-a-nutshell-explanation/#:~:text=Computer%20algorithms%20work%20via%20input,the%20words%20in%20the%20query.')  # insert zoom link here


def Thinking():
    webbrowser.open('https://www.cs.cmu.edu/~15110-s13/Unit03PtA-handout.pdf')  # insert zoom link here


def mathsstats():
    webbrowser.open('https://docs.google.com/document/d/1H6uymwkuX3ZWFUxjINVXl2lOK7fgzO4NqlaUMiwUraM/edit?usp=sharing')  # insert zoom link here


# physics
def Effect():
    webbrowser.open('https://www.lopol.org/article/computers-and-our-life-how-have-computers-changed-our-life#:~:text=Computer%20also%20facilitate%20comfort%20to,relieve%20severity%20of%20traveling%20difficulties.')  # insert zoom link here


def Bad():
    webbrowser.open('https://theconversation.com/ai-can-now-read-emotions-should-it-128988')  # insert zoom link here


# compsci
def media():
    webbrowser.open('https://www.youtube.com/watch?v=Czg_9C7gw0o')  # insert zoom link here


def the_brain():
    webbrowser.open('https://static.nautil.us/14525_0bd97cb91b8d57dad18542081fb8f2b1.png')  # insert zoom link here


## text declaration ##
'''
Text1 = Text(root, "hellO")
Text1.grid(row=0,column=2)
'''

myFont = font.Font(family='Arial', size=25, weight='bold')
## button declaration ##
# maths
ButtonTextPure = Button(root, text="Algorithms", state=DISABLED, font=myFont, fg="black", width=15)
ButtonTextPure.grid(row=0, column=0, padx=10)
ButtonPure = Button(root, text="What are they?", fg="#FFFFFF", bg="#000000", command=Algorithm, height=3, width=25)  # pure
ButtonPure.grid(row=1, column=0, padx=10, pady=1)
ButtonPure = Button(root, text="How does it work?", fg="#FFFFFF", bg="#000000", command=Thinking, height=3, width=25)  # mech
ButtonPure.grid(row=2, column=0, padx=10, pady=1)
ButtonPure = Button(root, text="Statistics", fg="#FFFFFF", bg="#000000", command=mathsstats, height=3, width=25)  # stats
ButtonPure.grid(row=3, column=0, padx=10, pady=1)

# physics
ButtonTextPure = Button(root, text="Devices", state=DISABLED, font=myFont, fg="black", width=15)
ButtonTextPure.grid(row=0, column=1, padx=10)
ButtonPure = Button(root, text="Effects", fg="#5585F9", bg="#4BDBCF", command=Effect, height=3, width=25)  # teacher1
ButtonPure.grid(row=1, column=1, padx=10, pady=1)
ButtonPure = Button(root, text="Consequences", fg="#5585F9", bg="#4BDBCF", command=Bad, height=3, width=25)  # teacher2
ButtonPure.grid(row=2, column=1, padx=10, pady=1)

# comp sci
ButtonTextPure = Button(root, text="Other Info", state=DISABLED, font=myFont, fg="black", width=15)
ButtonTextPure.grid(row=0, column=2, padx=5)
ButtonPure = Button(root, text="Social Media", fg="#5585F9", bg="#4BDBCF", command=media, height=3, width=25)  # theory
ButtonPure.grid(row=1, column=2, padx=10, pady=1)
ButtonPure = Button(root, text="Problem Solving", fg="#5585F9", bg="#4BDBCF", command=the_brain, height=3, width=25)  # pracitcal/problem solving
ButtonPure.grid(row=2, column=2, padx=10, pady=1)
root.mainloop()
