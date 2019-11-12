import time
import os

def clear():

    # Clears the console

    os.system('clear')

def reading(num):

    # Gathers the blood pressure readings.
    
    print(f'Please take the {num} reading now.\n')
    time.sleep(30)

    correct = None

    while correct != 'yes' and correct != 'y':

        SYS = int(input(f'What is the SYS of the {num} reading? '))
        DIA = int(input(f'What is the DIA of the {num} reading? '))
        PUL = int(input(f'What is the PUL of the {num} reading? '))

        print(f'\n{num.capitalize()} Blood Pressure reading:\n {SYS}/{DIA} {PUL}\n')
        time.sleep(1)

        correct = input('Is this the correct blood pressure reading? (Yes/No) ').lower()

        print('')

    bp = {
        "SYS" : SYS,
        "DIA" : DIA,
        "PUL" : PUL
    }

    return bp

def countdown():

    # Countdown timer for 30 seconds

    countdown = 30
    print(f'Please wait {countdown} seconds before continuing.')

    while countdown != 0:
        countdown = countdown - 1
        time.sleep(1)
        if countdown == 20 or countdown == 10:
            print(f'{countdown} seconds remaining.')

    print('')

def avgBp(bp1, bp2, bp3):

    # Averages the Blood Pressures that were previously collected.

    print(f'Calcuating average blood pressure')
    time.sleep(2)

    AVG_SYS = int(((bp1["SYS"] + bp2["SYS"] + bp3["SYS"]) / 3))
    AVG_DIA = int(((bp1["DIA"] + bp2["DIA"] + bp3["DIA"]) / 3))
    AVG_PUL = int(((bp1["PUL"] + bp2["PUL"] + bp3["PUL"]) / 3))

    print(f"\nAverage blood pressure: \n {AVG_SYS}/{AVG_DIA} {AVG_PUL}\n")

    AVG_BP = {
        'AVG_SYS' : AVG_SYS,
        'AVG_DIA' : AVG_DIA,
        'AVG_PUL' : AVG_PUL
    }

    return AVG_BP

def readingOutput(AVG_BP):

    # Idenifys the diagnosis range that the Average SYS is in. 

    if AVG_BP['AVG_SYS'] < 90:
        print(f"Your average SYS is showing signs of Hypotension")

    if AVG_BP['AVG_SYS'] >= 91 and AVG_BP['AVG_SYS'] <= 120:
        print(f"Your average SYS is in a healthy range")

    if AVG_BP['AVG_SYS'] >= 121  and AVG_BP['AVG_SYS'] <= 140:
        print(f"Your average SYS is showing signs of Prehypertension")

    if AVG_BP['AVG_SYS'] >= 141 and AVG_BP['AVG_SYS'] <= 160:
        print(f"Your average SYS is showing signs of Hypertension Stage 1")

    if AVG_BP['AVG_SYS'] >= 161:
        print(f"Your average SYS is showing signs of Hypertension Stage 2")

    # Idenifys the diagnosis range that the Average DIA is in. 

    if AVG_BP['AVG_DIA'] < 60:
        print(f"Your average DIA is showing signs of Hypotension")

    if AVG_BP['AVG_DIA'] >= 61 and AVG_BP['AVG_DIA'] <= 80:
        print(f"Your average DIA is in a healthy range")

    if AVG_BP['AVG_DIA'] >= 81  and AVG_BP['AVG_DIA'] <= 90:
        print(f"Your average DIA is showing signs of Prehypertension")

    if AVG_BP['AVG_DIA'] >= 91 and AVG_BP['AVG_DIA'] <= 100:
        print(f"Your average DIA is showing signs of Hypertension Stage 1")

    if AVG_BP['AVG_DIA'] >= 101:
        print(f"Your average DIA is showing signs of Hypertension Stage 2")

    print('')