from gzip import BadGzipFile
import random
from tkinter import *
import tkinter
from turtle import back

# Square root question
def question(correct):
    answer = input("Qual é a raíz quadrada de " + str(correct**2))
    if answer == str(correct):
        return([True,answer])
    else:
        return([False,answer])

# Main Window
master = Tk()
master.title("QUESTÃO RAÍZ QUADRADA")
master.geometry('800x600')

#startingScene = input('Pressione 0 para treino ou qualquer outra coisa para pergunta normal')
startingScene = '0'

############################################################################################################################################################
########################################################################  Overlay  #########################################################################
############################################################################################################################################################

# Separator Lines
line1 = Label(text = "                                                                                                                          ", font=("Arial", 50,'underline'))
line1.place(x=-100,y=30)
line2 = Label(text = "                                                                                                                          ", font=("Arial", 50,'underline'))
line2.place(x=-100, rely=1, y=-120, anchor='sw')

# Title
title = Label(text="QUIZ RAÍZ QUADRADA", font=("Arial", 40, 'bold'), justify=CENTER)
title.place(relx=0,y=15, relwidth=1)
title.tkraise(aboveThis=line1)

# Setup answer history on the bottom of the window
answerHistory = []
for i in range(3):
    specificQuestion = [Label(text = "√▢▢▢▢▢▢=▢▢▢", font=('Arial', 30)), Label(text = "▢", font=('Arial', 60)), False]
    answerHistory.append(specificQuestion)
    answerHistory[i][1].place(relx=1/6+i/3, rely=1, y=-80, anchor='n')
    answerHistory[i][0].place(relx=1/6+i/3, rely=1, y=-110, anchor='n')
    answerHistory[i][0].tkraise(aboveThis=answerHistory[i][1])

############################################################################################################################################################
###################################################################  Question Scene (0)  ###################################################################
############################################################################################################################################################


answer = tkinter.StringVar()
answerEntry = Entry(master, textvariable=answer, font=('Arial', 20))
if startingScene == '0':
    # Question
    currentQuestionText = Label(text="Qual é a raiz quadrada de...", font=("Arial", 40), justify=CENTER)
    currentQuestionText.place(relx=0.5, rely = 0.2, anchor='n')
    currentQuestionNumber = Label(text="▢▢▢▢▢▢", font=("Arial", 100), justify=CENTER)
    currentQuestionNumber.place(relx=0.5, rely = 0.3, anchor='n')

    # Submit Answer
    answerEntry.place(relx=0.5,rely=0.57, anchor='n')

    showAnswer = Label(master, text='RESPOSTA\nCORRETA', font=('Arial', 50), justify=CENTER)
    showNumberAnswer = Label(master,text='▢▢▢', font=('Arial', 100), justify=CENTER)

############################################################################################################################################################
####################################################################  Answer Scene (1)  ####################################################################
############################################################################################################################################################

else:
    # Question
    currentQuestionText = Label(text="Qual é a raiz quadrada de...", font=("Arial", 36), justify=CENTER)
    currentQuestionText.place(relx=0.4, rely = 0.2, anchor='n')
    currentQuestionNumber = Label(text="▢▢▢▢▢▢", font=("Arial", 90), justify=CENTER)
    currentQuestionNumber.place(relx=0.4, rely = 0.3, anchor='n')

    # Show Answer
    showAnswer = Label(master, text='RESPOSTA\nCORRETA', font=('Arial', 25), justify=CENTER)
    showNumberAnswer = Label(master,text='▢▢▢', font=('Arial', 60), justify=CENTER)
    showAnswer.place(relx=0.85, rely=0.4, anchor='n')
    showNumberAnswer.place(relx=0.85, rely=0.55, anchor='n')

############################################################################################################################################################
##########################################################################  Code  ##########################################################################
############################################################################################################################################################

def generateQuestion():
    global currentAnswer
    currentAnswer = random.randint(100,1000)
    currentQuestionNumber.configure(text=str(currentAnswer**2))
    showNumberAnswer.configure(text=str(currentAnswer))

generateQuestion()

currentQuestion = 0

############################################################################################################################################################
##################################################################  Buttons and Functions  #################################################################
############################################################################################################################################################

def checkAnswer():

    thisAnswer = -1
    for i in range(4):
        if not answerHistory[i][2]:
            thisAnswer = i
            answerHistory[i][2] = True
            break

    try:
        if int(answerEntry.get())==currentAnswer:
            answerHistory[thisAnswer][1].configure(text='✔️', font=('arial', 30), justify=CENTER, fg='green')
            answerHistory[thisAnswer][1].place(relx=1/6+thisAnswer/3, rely=1, y=-80, anchor='n')
        else:
            answerHistory[thisAnswer][1].configure(text='✘', font=('arial', 60), justify=CENTER, fg='red')
    except:
        answerHistory[thisAnswer][2] = False
        return()
    
    answer.set('')
    answerHistory[thisAnswer][0].configure(text='√' + str(currentAnswer**2) + '=' + str(currentAnswer))

    if thisAnswer == 2:
        changeScene()
    else:
        generateQuestion()

def answerCorrectFunction():

    thisAnswer = -1
    for i in range(4):
        if not answerHistory[i][2]:
            thisAnswer = i
            answerHistory[i][2] = True
            break

    answerHistory[thisAnswer][1].configure(text='✔️', font=('arial', 40), justify=CENTER, fg='green')
    answerHistory[thisAnswer][1].place(relx=7/36+thisAnswer/3, rely=1, y=-70, anchor='n')
        
    answerHistory[thisAnswer][0].configure(text='√' + str(currentAnswer**2) + '=' + str(currentAnswer))

    if thisAnswer == 2:
        changeScene()
    else:
        generateQuestion()

def answerWrongFunction():

    thisAnswer = -1
    for i in range(4):
        if not answerHistory[i][2]:
            thisAnswer = i
            answerHistory[i][2] = True
            break

    answerHistory[thisAnswer][1].configure(text='✘', font=('arial', 60), justify=CENTER, fg='red')
        
    answerHistory[thisAnswer][0].configure(text='√' + str(currentAnswer**2) + '=' + str(currentAnswer))

    if thisAnswer == 2:
        changeScene()
    else:
        generateQuestion()

submitButton = Button(master, text='Submit', font=('Arial', 20), command=checkAnswer)
correctButton = Button(master, text='CORRETO', font=('Arial', 20), fg='green', command=answerCorrectFunction)
wrongButton = Button(master, text='ERRADO', font=('Arial', 20), fg='red', command=answerWrongFunction)


if startingScene == '0':
    submitButton.place(relx=0.5, rely=0.65, anchor='n')
else:
    correctButton.place(relx=0.27,rely=0.57, anchor='n')
    wrongButton.place(relx=0.5,rely=0.57, anchor='n')

    

############################################################################################################################################################
##########################################################################  Code  ##########################################################################
############################################################################################################################################################

def changeScene():

    currentQuestionText.destroy()
    currentQuestionNumber.destroy()
    answerEntry.destroy()
    submitButton.destroy()
    correctButton.destroy()
    wrongButton.destroy()
    showAnswer.destroy()
    showNumberAnswer.destroy()

    correctAnswers = 0

    for i in answerHistory:
        if i[1].cget('text') == '✔️':
            correctAnswers += 1

    ending1 = Label(master, text=str(correctAnswers) + ' DE 3 QUESTÕES', justify=CENTER, font=('arial', 50))
    ending1.place(relx=0.5, rely=0.45, anchor=S)
    ending2 = Label(master, text='RESPONDIDAS CORRETAMENTE', justify=CENTER, font=('arial', 30))
    ending2.place(relx=0.5, rely=0.5, anchor=N)

master.update()

master.mainloop()