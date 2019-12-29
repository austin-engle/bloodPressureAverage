# from time import sleep
import os
from datetime import datetime

now = datetime.now()
date = f"{now.month}/{now.day}/{now.year}"

def clear():

    # Clears the console

    os.system("clear")


def reading(num):

    # Gathers the blood pressure readings.

    print(f"Please take the {num} reading now.\n")
    # sleep(30)

    correct = None

    while correct != "yes" and correct != "y":

        sys = int(input(f"What is the SYS of the {num} reading? "))
        dia = int(input(f"What is the DIA of the {num} reading? "))
        pul = int(input(f"What is the pul of the {num} reading? "))

        print(f"\n{num.capitalize()} Blood Pressure reading:\n {sys}/{dia} {pul}\n")
        # sleep(1)

        correct = input("Is this the correct blood pressure reading? (Yes/No) ").lower()

        print("")

    bp = {
        "sys": sys,
        "dia": dia,
        "pul": pul
    }

    return bp


def countdown():

    # Countdown timer for 30 seconds

    countdown = 30
    print(f"Please wait {countdown} seconds before continuing.")

    while countdown != 0:
        countdown = countdown - 1
        # sleep(1)
        if countdown == 20 or countdown == 10:
            print(f"{countdown} seconds remaining.")

    print("")


def avgbp(bp1, bp2, bp3):

    # Averages the Blood Pressures that were previously collected.

    print(f"Calcuating average blood pressure")
    # sleep(2)

    avg_sys = int(((bp1["sys"] + bp2["sys"] + bp3["sys"]) / 3))
    avg_dia = int(((bp1["dia"] + bp2["dia"] + bp3["dia"]) / 3))
    avg_pul = int(((bp1["pul"] + bp2["pul"] + bp3["pul"]) / 3))

    print(f"\nAverage blood pressure: \n {avg_sys}/{avg_dia} {avg_pul}\n")

    avg_bp = {"avg_sys": avg_sys, "avg_dia": avg_dia, "avg_pul": avg_pul}

    return avg_bp


def diagnosis_output(avg_bp):

    # Idenifys the diagnosis range that the Average sys is in.

    if avg_bp["avg_sys"] < 90:
        print(f"Your average sys is showing signs of Hypotension")
        sys_diagnosis = '1'

    elif avg_bp["avg_sys"] >= 91 and avg_bp["avg_sys"] <= 120:
        print(f"Your average sys is in a healthy range")
        sys_diagnosis = "2"

    elif avg_bp["avg_sys"] >= 121 and avg_bp["avg_sys"] <= 140:
        print(f"Your average sys is showing signs of Prehypertension")
        sys_diagnosis = "3"

    elif avg_bp["avg_sys"] >= 141 and avg_bp["avg_sys"] <= 160:
        print(f"Your average sys is showing signs of Stage 1 Hypertension")
        sys_diagnosis = "4"

    elif avg_bp["avg_sys"] >= 161:
        print(f"Your average sys is showing signs of Stage 2 Hypertension")
        sys_diagnosis = "5"

    # Idenifys the diagnosis range that the Average dia is in.

    if avg_bp["avg_dia"] < 60:
        print(f"Your average dia is showing signs of Hypotension")
        dia_diagnosis = '1'

    elif avg_bp["avg_dia"] >= 61 and avg_bp["avg_dia"] <= 80:
        print(f"Your average dia is in a healthy range")
        dia_diagnosis = "2"

    elif avg_bp["avg_dia"] >= 81 and avg_bp["avg_dia"] <= 90:
        print(f"Your average dia is showing signs of Prehypertension")
        dia_diagnosis = "3"

    elif avg_bp["avg_dia"] >= 91 and avg_bp["avg_dia"] <= 100:
        print(f"Your average dia is showing signs of Stage 1 Hypertension")
        dia_diagnosis = "4"

    elif avg_bp["avg_dia"] >= 101:
        print(f"Your average dia is showing signs of Stage 2 Hypertension")
        dia_diagnosis = "5"

    print("")

    # Now compare the diagnosis from the SYS and DIA and come to one diagnosis

    dia = {
        "1" : "Hypotension",
        "2" : "Normal",
        "3" : "Prehypertension",
        "4" : "Stage 1 Hypertension",
        "5" : "Stage 2 Hypertension"
    }

    if sys_diagnosis == '1' or dia_diagnosis == '1':
        diagnosis = dia["1"]
        
    elif sys_diagnosis > dia_diagnosis:
        diagnosis = dia[sys_diagnosis]

    elif sys_diagnosis < dia_diagnosis:
        diagnosis = dia[dia_diagnosis]

    print(diagnosis) # Remove
    return diagnosis


def tags():
    tags_arm = {
        '1' : 'Right arm',
        '2' : 'Left arm'
    }

    tags_position = {
        '1' : "Seated",
        '2' : "Laying Down"
    }

    arm_choice = input('Did you take the reading with your Right(1) or Left(2) arm?\n')

    position_choice = input('Were you seated(1) or laying down(2) when taking the reading?\n')

    tags = f'{tags_arm[arm_choice]} | {tags_position[position_choice]}'

    return tags


def push_to_github():

    # Pushes the updates to github automatically as the end of the script

    os.system("git add *")
    # sleep(1)
    os.system(f"git commit -m 'commit after blood pressure reading: {date}'")
    # sleep(1)
    os.system(f"git push")


def write_to_csv(avg_bp, diagnosis, tags):

    # rows to gather

    # DATE
    date
    print(date)
    # TIME
    time = f"{now.hour}:{now.minute}"
    print(time)
    # SYS
    sys = avg_bp['avg_sys']
    print(sys)

    # DIA
    dia = avg_bp['avg_dia']
    print(dia)

    # PUL
    pul = avg_bp['avg_pul']
    print(pul)

    # BPZ
    bpz = diagnosis

    # TAGS
    tags = tags


    return