import tkinter as Tkinter
from tkinter import Tk, Text, Button, Label, END
import random
# defining dictionary for choices
computer_dict = {
                "0": "Rock",
                "1": "Paper",
                "2": "Scissor"
                
                } 

# define global variables
user_choice = ""
computer_choice = ""
user_score = 0
computer_score = 0

#################################### IMPORTANT FUNCTIONS  #####################################

# displayed 
def Playagain():
    text_to_display.delete('1.0', 'end') 
    
# function to update points after every game
def points():
    text_to_scores.delete('1.0', 'end')
    text_to_scores.insert(END,f"    {user_score}                   {computer_score}")
    

# function to define what happens when user select Rock 

def rock():
    global computer_score
    global user_score
    your_choice = 'Rock'
    
    # choosing random variable from above function
    computer_choice = computer_dict[str(random.randint(0,2))]
    # to display choices
    text_to_display.insert(END, f"Your Choice:   {your_choice}\ncomputer choice:    {computer_choice}")
    
    # to increase the score accordingly
    if computer_choice == "Paper":
        computer_score +=1
    if computer_choice == "Scissor":
        user_score +=1
    points()
    
    
# same as the above function 

def paper():
    global computer_score
    global user_score
    user_choice ="Paper"
    computer_choice = computer_dict[str(random.randint(0,2))]
    text_to_display.insert(END, f"Your Choice:    {user_choice}\ncomputer Choice:     {computer_choice}")
    
    if computer_choice == "Scissor":
        computer_score +=1
    if computer_choice =="Rock":
        user_score+=1
    
    points()
    
def scissor():
    global computer_score
    global user_score
    user_choice ="Scissor"
    computer_choice = computer_dict[str(random.randint(0,2))]
    text_to_display.insert(END, f"Your Choice:    {user_choice}\ncomputer Choice:     {computer_choice}")
    
    if computer_choice == "Rock":
        computer_score +=1
    if computer_choice =="Paper":
        user_score+=1   
    points()   

# Defining main window and all its widgets of python Rock Paper scissors Game

root = Tk()
root.title('Rock Paper Scissor')

root.geometry('270x200')
root.config(bg="light blue")

# text widget to display choices

text_to_display = Text(root, height = 30, width = 300)
text_to_display.grid(row = 0, columnspan = 5, pady = 10)

# define buttons accordingly
button_rock = Button(root, text = 'Rock', width = 6, command = rock)
button_rock.grid(row = 2, column = 0, padx = 10)

button_paper = Button(root, text = 'Paper', width = 6, command = paper)
button_paper.grid(row=2, column= 1, padx = 10)

button_scissor = Button(root, text = 'Scissor', width = 6, command = scissor)
button_scissor.grid(row=2, column= 2, padx = 10)

# widget to add label specified by text
label_scores = Label(root, text = 'Your Score               vs             computer score')
label_scores.grid(row = 3, columnspan = 5, pady = 8)


text_to_scores = Text(root, height = 1,width = 30)
text_to_scores.grid(row = 4, columnspan = 5, pady = 5)

# play again to start the game again
play_again = Button(root, text = 'Play Again', command = Playagain)
play_again.grid(row=5, columnspan = 3)

root.mainloop()