"""
This experiment assesses participants' mathematical abilities by presenting simple math problems 
involving addition and subtraction. The goal is to measure both the accuracy and reaction times 
of participants when solving these problems. 

The experiment consists of the following key steps:

1. Task Design:
   - The experiment is divided into three blocks, each containing 60 trials.
   - In each trial, participants are presented with a random math problem: either an addition or a subtraction problem.
   - The answers are guaranteed to be one-digit numbers (i.e., ranging from 0 to 9).
   - Participants are asked to respond to the problem using the keys '0' to '9' on the keyboard.
   
2. Trial Details:
   - For addition problems: Random one-digit numbers are chosen, ensuring the result is a one-digit number.
   - For subtraction problems: Random one-digit subtractions are used, but some "hard" and "medium" difficulty subtractions are generated for variety (ensuring answers are still one-digit numbers).
   
3. Response and Data Collection:
   - Participants' responses are recorded, and the reaction time for each answer is logged.
   - At the end of each block, participants will receive feedback showing their percentage of correct answers and the average reaction time. They will be prompted to press the spacebar to proceed to the next block.
   
4. Data Export:
   - The reaction times and accuracy for each trial are saved into a matrix, which is then exported into a CSV file for further analysis.
   
5. Post-Experiment Analysis:
   - At the end of the experiment, a bar plot is generated displaying the average reaction times for addition versus subtraction problems.
   
The code uses the PsychoPy library to present stimuli and capture responses, while statistical calculations are done using Python's built-in libraries (e.g., `statistics` and `numpy`).
"""

import matplotlib.pyplot as plt #to be able to plot the variables
import random #to get random numbers
import statistics #to do basic maths like means
import numpy as np #i used this because i want to create maatrices
import csv #to write into csv file, it seems a better method that just hardcoding in csv, if i make a mistake then it wont be readable in csv, and with import csv i reduce the probability of a mistake
from psychopy import visual, core, event


def text_space(text):
#defining a function with the text presented to avoid repetition
#using space to continue
    message = visual.TextStim(win, text +"\n press [SPACE] to continue", color='black', bold = True)
    message.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])

def give_response(text):
#defining a function that records the the participants responses and returns responses which is a list
    message = visual.TextStim(win, text, color='black', bold = True)
    message.draw()
    win.flip()
    timer = core.Clock()
    responses = event.waitKeys(keyList = ['0','1','2','3','4','5','6','7','8','9'], timeStamped = timer)
    win.flip
    return responses

def experiment(number, name):
#define a function that does the trials, it presents the calculations [before presenting, it randomly selects addition or subtraction, then calculates
#if its addition to be one digit answer, if its subtraction to be one digit answer, also i play a bit with subtraction difficulty, i created easy/medium/hard subtractions
#with one digit answer
#it records the response and reaction time; the name of the block (if its trial, block 1,block2,block3; trial number 1,2,3,4,...; whether the participants answer is correct
#it records the number of correct and the number of incorrect responses
#then all these list variables are merged into a matrix and returned to the main code to add the matrices together from each block and then convert the matrix with all the data into a file.
#we need to record the reaction time and accuracy in a file
#do not provide feedback within block
#provide feedback at the end of block [precentage of correct + average reaction time] wait for SPACEBAR to proceed

    block = []
    trial = []
    operation_list = []
    iscorrect = []
    rt_overall = []

    correct_test = 0
    incorrect_test = 0

    for i in range(number): # 10 trials in the test
        block.append(name)
        #append the name in each row because later I create a matrix with all the variables needed and to calculate the mean I need the name of the block to locate the appropriate variable
        trial.append(i + 1) #creating a list with the trial number, it is +1 because i starts at 0
        a = 0 
        b = 0
        c = 0
        operation = random.choice(['addition', 'subtraction'])
        # for debuging purposes print(operation, '\n\n')
        operation_list.append(operation)
        
        #randomly select addition or subtraction to make it unpredictable for the participant
        #if the operation is addition do addition
        #choose for a and b values from 0 to 9 because otherwise the result will be larger than one digit
        #random numbers to reduce any expectancy from the participant and reduce bias in our experiment
        if operation == 'addition':
            #for debuging print("addition\n\n")
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c = a + b
            #for debuging print(f"a = {a}, b = {b}, c = {c}")
            #if its not 1 letter stay in the loop and assign random numbers until the addition is one digit
            while c < 0 or c > 9:
                a = random.randint(0, 9)
                b = random.randint(0, 9)
                c = a + b
                # for debuging: print(f"a = {a}, b = {b}, c = {c}")
            #for debuging print(f"chosen c: {c}")
            #here you going to add what the participant will see and record their input compare it with c say correct/incorrect
            text = f"{str(a)} + {str(b)}"
            responses = give_response(text)
            # for debuging purposes print(responses)
            result, rt = responses[0]   #placed the items of list responses to result and rt
            result = int(result)    #converted results to integer because it was string and the if below did not work


        if operation == 'subtraction':
            difficulty = random.choice(['easy', 'medium', 'hard'])
            #play a bit with difficulty, because why not
            # for debuging purposes print(difficulty, '\n')
            if difficulty == 'easy':
                a = random.randint(0, 9)
                b = random.randint(0, 9)
                c = a - b
                # for debuging purposes print(f"a = {a}, b = {b}, c = {c}")

                while c < 0 or c > 9: #check last while-loop for explanation
                    a = random.randint(0, 9)
                    b = random.randint(0, 9)
                    c = a - b
                    # for debuging purposes print(f"a = {a}, b = {b}, c = {c}")
                # for debuging purposes print(f"chosen c: {c}")
            #medium lets say are numbers between 10 to 1000
            if difficulty == 'medium':
                a = random.randint(10, 30)
                b = random.randint(10, 30)
                c = a - b
                # for debuging purposes print(f"a = {a}, b = {b}, c = {c}")
                while c < 0 or c > 9: # check last while-loop for explanation
                    a = random.randint(10, 30)
                    b = random.randint(10, 30)
                    c = a - b
                    # for debuging purposes print(f"a = {a}, b = {b}, c = {c}")
                # for debuging purposes print(f"chosen c: {c}")
            #lets say a hard subtraction is from 30 to 100
            if difficulty == 'hard':
                a = random.randint(30, 100)
                b = random.randint(30, 100)
                c = a - b
                # for debuging purposes print(f"a = {a}, b = {b}, c = {c}")
                while c < 0 or c > 9: #here basically if its 0-9 its one digit, if its not we recaclulate a,b until the result is one digit
                    a = random.randint(30, 100)
                    b = random.randint(30, 100)
                    c = a - b    
                    # for debuging purposes print(f"a = {a}, b = {b}, c = {c}")
                # for debuging purposes print(f"chosen c: {c}")
            text = f"{str(a)} - {str(b)}"
            responses = give_response(text)
            #here we have found which a and b will be used and show them to the participant, while we know the result we ask them for the result
            result, rt = responses[0] #here the keys stored in the list responses are splited into results and reaction time
            result = int(result) #the keys were stored in string and we need them in integer type to do the below if operation; c == result

        if c == result:
        #here if they answered correct append in the list True and add +1 to calculate later the percepntage of correct/the same for incorrect
            # for debuging purposes print("correct")
            iscorrect.append(True)
            correct_test += 1
        else:
            # for debuging purposes print("incorrect")
            iscorrect.append(False)
            incorrect_test += 1
        rt_overall.append(rt) #append to our list the reaction time irrespective of correxxt/incorrect bcs we are going to design a matrix with all the results and it will have True/False in one column

    if correct_test + incorrect_test == 0: #here we calculate the percentage of correct responses
        perc_correct = 0
    else:
        perc_correct = 100*(correct_test/(correct_test + incorrect_test)) #percentage of correct, while avoiding division by 0
    # for debuging purposes print(block, trial, operation_list ,iscorrect, rt_overall)
    text = f"you answered {perc_correct}% correct with {statistics.mean(rt_overall):.4f}s average reaction time"
    text_space(text)
    if name == "Test Trial" and perc_correct < 60: 
    # Here if its the test trial, and the accuracy is below 60% then we repeat the test trial by calling again the experiment(_,_)
        text = f"You had {perc_correct}% which is lower than the 60% threshold.\n The trial will restart. Please try to be more accurate\n"
        text_space(text)
        experiment(number, "Test Trial")
    #here I am going to merge the lists created by adding them in a 2d matrix, this matrix will be later used to export all the data in a .csv
    matrix = np.column_stack((block, trial, operation_list, iscorrect, rt_overall))
    return matrix #now the lists are in columnar shape in a matrix and are returned

#define a window
win = visual.Window(size=(1200, 800), fullscr=False, color='RoyalBlue')

#welcoming participants and explaining the task
text = '''
Dear participant. Thank you for volunteering to this experiment.
You will be assessed on your mathematical abilities
by solving simple math problmes involving addition and subtraction 
the result of the problem will be a one-digit result

e.g., 8 - 2 = ?
correct answer: 6
'''
text_space(text)

# rewriting the text varible
text = '''
You should always use the keys 0 - 9

remember that all problems involve a one-digit solution
'''
text_space(text)

#create a test trial with accuracy measures
text = '''
First you will perform some test trials to get used to the experiment
'''
text_space(text)
text = '''
Test Trial
use keys 0 to 9 to answer
'''

#test trial, we need 60% accuracy, above chance, to continue to the main experiment; I just wanted to make it better
matrix_test = experiment(10, "Test Trial")
#now that we have the matrix we are going to add the other matrices into this one, and at the end export the final product into a .csv

# for debuging purposes print("\n\nmatrixTEST:\n\n", matrix_test)


text = '''
Now you are going to perform the actual experiment. 
It consists of 3 BLOCKS.
Please try to be as accurate as possible
'''
text_space(text)

text = '''
BLOCK 1
use keys 0 to 9 to answer
'''
text_space(text)

matrix_1 = experiment(60, "BLOCK 1") 

#because adding 2 matrices of different dimension is not possible with matrix[:] = matrix nor .stack I am going to use .vstack from numpy which allows it once they have the same width
# [copy-pasted] numpy.vstack() function is used to stack the sequence of input arrays vertically to make a single array.
# for debuging purposes print("\n\nmatrix1:\n\n", matrix_1)

output_matrix = np.vstack((matrix_test, matrix_1)) #here i concatinate the one matrix with the other

# for debuging purposes print("\n\n np.vstack((matrix_test, matrix_1))\n\n", output_matrix)

text = '''
BLOCK 2
use keys 0 to 9 to answer
'''
text_space(text)

matrix_2 = experiment(60, "BLOCK 2") 
# for debuging purposes print("\n\nmatrix2:\n\n", matrix_2)

output_matrix = np.vstack((output_matrix, matrix_2)) #here i merge matrix_2 in the resulted outpute matrix; so i link test [trial+block1] + the block2
# for debuging purposes print("\n\noutput_matrix = np.vstack((output_matrix, matrix_2))\n\n", output_matrix)

text = '''
BLOCK 3
use keys 0 to 9 to answer
'''
text_space(text)

matrix_3 = experiment(60, "BLOCK 3") 
# for debuging purposes print("\n\nmatrix3:\n\n", matrix_3)

output_matrix = np.vstack((output_matrix, matrix_3)) #same as above
# for debuging purposes print("\n\n\noutput_matrix = np.vstack((output_matrix, matrix_3))\n\n", output_matrix)

# for debuging purposes print("\n\n\n FINAL MATRIX ", output_matrix, "\n\n\n")

text = '''
Congratz
'''
text_space(text)

win.close() # close our opened window

#now that I have created an array with all the data, I will export the data into a .csv
#i will import csv because I think its better; here is from where i searched this: https://www.geeksforgeeks.org/writing-csv-files-in-python/
#from my perspective its less prone to error because it does not rely on me to hard code into csv format but its preset

with open ('logdata.csv', 'w', newline='') as file: #opening a file named logdata.csv with write option and newline='' to avoid creation of new lines
    header = ['TrialType', 'TrialNumber', 'OperationUsed', 'IsCorrect','ReactionTime'] #here is my header
    write = csv.writer(file) #in this file every row will be written in csv format
    write.writerow(header) #into this object write the header in a row in csv format
    write.writerows(output_matrix) #write all my data in csv format bellow the header

# for debuging purposes print('check if csv file is created successfully')

#here i will create 2 list variables to store the reaction times of addition and the reaction times of subtraction
#the reaction times will be located in the large 2d matrix (output_matrix) and stored in two individual list variables
#the reaction times will be from the experimental blocks 1, 2, and 3 and not the test trial block

rt_addition = []
rt_subtraction = []

# for debuging purposes print(len(output_matrix))
for i in range(len(output_matrix)):
    # for debuging purposes print(f"output_matrix row {i} = {output_matrix[i]}\n")
    for y in range(len(output_matrix[i])):
        #for debuging purposes print(f"output_matrix row {i} column {y} = {output_matrix[i][y]}\n")
        if output_matrix[i][0] != 'Test Trial': #If we are in the test trial dont get the reaction times, if we are in the other trials insert the reaction times to the list variables
            if output_matrix[i][2] == 'addition': #if the trial was addition place it in the rt_addition, if its not addition (then its subtraction) place it in the subtraction variable
                rt_addition.append(float(output_matrix[i][4])) #i convert the value in the matrix to float because I need the list to be comprised of floats not strings, to put them in a graph later
            else:
                rt_subtraction.append(float(output_matrix[i][4]))
            
# for debuging purposes print(f"rt addition =\n {rt_addition}\n\n rt subtraction =\n {rt_subtraction}\n\n and the output matrix is \n {output_matrix}")

#here I calculated the mean of each in order to use the mean as an input for the bar plots
mean_addition = statistics.mean(rt_addition)
mean_subtraction = statistics.mean(rt_subtraction)

# for debuging purposes print(mean_addition, mean_subtraction)

plt.bar (["Addition", "Subtraction"],[round(mean_addition,4), round(mean_subtraction, 4)])
plt.title('Reaction Time of Addition/Subtraction')
plt.xlabel('Operation')
plt.ylabel('Average Reaction Time')
plt.show()


