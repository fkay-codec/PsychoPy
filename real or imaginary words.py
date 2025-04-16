# display sequences of letters and prompt participants to quickly determine whether each sequence forms a real word or a
# non-word. Participants should indicate their responses by pressing ’r’ for a real word and ’i’ for a non-word

from psychopy import visual, core, event
import random

#define a window
win = visual.Window(size=(1200, 800), fullscr=False, color='cornflowerblue')
text = ("Dear Participant.\nA sequence of letters will be presented. When the"
"sequence ends please press:\n'r' if the word was real\n'i' if the word"
"is not real\n\nPress the spacebar to continue")

message = visual.TextStim(win, text, color='black', bold = True)
message.draw()
win.flip()
event.waitKeys(keyList = 'space')


#define real
real = [
    'dog', 'cat', 'house', 'tree', 'water', 'sun', 'moon', 'star', 'cloud', 'river',
    'mountain', 'ocean', 'forest', 'flower', 'grass', 'bird', 'fish', 'apple', 'banana',
    'chair', 'table', 'window', 'door', 'book', 'pencil', 'paper', 'school', 'teacher', 
    'student', 'music'
]
#define not real
not_real = [
    'zorp', 'flimby', 'drindle', 'sprock', 'blenko', 'vleeb', 'cringal', 'woft', 'plig',
    'smarve', 'trindle', 'gribble', 'snorf', 'quibbit', 'frozzle', 'marnix', 'skroop', 'twizzle',
    'blurf', 'jibber'
]
#define the whole trial set
words = real + not_real
#randomize the trials
random.shuffle(words)

reaction_times = []
iscorrect = []

#for debuging purposes dummy = ['dog', 'cat', 'ocean','flimby']

for trial in words: #iterating over words
    word_index = 0 #current position in the word
    for word_index in range(len(trial)): #length of the current word, itterate in that length
        message = visual.TextStim(win, text=trial[word_index], color='black', bold = True)  #print the currect position in the word, the letter
        message.draw()
        win.flip()
        core.wait(0.5) #wait a bit, otherwise it itterates very fast and cannot be seen on screen
    
    message = visual.TextStim(win, text="Give Response \n\n r: for real \n\n i: for not real", color='red', bold = True)
    message.draw()
    win.flip()
    timer = core.Clock() #record the time elapsed to press a key
    responses = event.waitKeys(keyList = ['r', 'i'], timeStamped = timer) #store the key used and the general reaction time
    reaction_time = timer.getTime() #store the speicific time elapsed from prompt to pressing
    reaction_times.append(reaction_time) #store the true reaction time in the list
    response, rt = responses[0] #split the key used and the general reaction time in these variables
    correct = False 
    if response == 'r': 
        for rwords in real: #check the real
            if trial == rwords: # if the word is in real then return true and break the loop
                correct = True
                break
    if response == 'i':
        for iwords in not_real: #similar logic
            if trial == iwords:
                correct = True
                break              
    # the idea above is if you dont find with specific characteristics return false
    iscorrect.append(correct) #append the answer to list
    message = visual.TextStim(win, text=f"{correct} \n with Reaction Time: {reaction_time:.2f}s", color='RoyalBlue', bold = True)
    message.draw()
    win.flip()
    core.wait(2.5)

print(f"iscorrect = {iscorrect}\n\nreaction times {reaction_times}") #print everything in terminal, can be used for log file

win.close() # close our opened window




