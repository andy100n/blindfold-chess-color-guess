from time import sleep
import random
import os
import keyboard
import pyttsx3
# import winsound

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()



score = 0
total = 0

os.system("cls")
sq = (random.randint(0,7), random.randint(0,7))
sq_color = (sq[0] + sq[1]) % 2 
print(chr(sq[0]+ord('a')) + str(sq[1]+1), '\t\t', '0.0%')
speak(chr(sq[0]+ord('a')) + ' ' + str(sq[1]+1))

while True:
    key = keyboard.read_event()
    
    if key.event_type == keyboard.KEY_DOWN:
        if key.name == 'esc':
            break
        elif key.name == 'b' or key.name == 'w':
            if sq_color == 0 and key.name == 'b' or sq_color == 1 and key.name == 'w':
                # winsound.Beep(1000, 250)
                score += 1
            else:
                # winsound.Beep(200, 500)
                print('X')
                sleep(2)
                
            total += 1
            os.system("cls")
            
            sq = (random.randint(0,7), random.randint(0,7))
            sq_color = (sq[0] + sq[1]) % 2 
            print(chr(sq[0]+ord('a')) + str(sq[1]+1), '\t\t', round(score*100/total, 2), '%')
            speak(chr(sq[0]+ord('a')) + ' ' + str(sq[1]+1))