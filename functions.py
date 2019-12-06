import time
import os


def clear():

    # Clears the console

    os.system("clear")


def reading(num):

    # Gathers the blood pressure readings.

    print(f"Please take the {num} reading now.\n")
    time.sleep(30)

    correct = None

    while correct != "yes" and correct != "y":

        sys = int(input(f"What is the SYS of the {num} reading? "))
        dia = int(input(f"What is the DIA of the {num} reading? "))
        pul = int(input(f"What is the PUL of the {num} reading? "))

        print(f"\n{num.capitalize()} Blood Pressure reading:\n {sys}/{dia} {pul}\n")
        time.sleep(1)

        correct = input("Is this the correct blood pressure reading? (Yes/No) ").lower()

        print("")

    bp = {"sys": sys, "dia": dia, "PUL": pul}

    return bp


def countdown():

    # Countdown timer for 30 seconds

    countdown = 30
    print(f"Please wait {countdown} seconds before continuing.")

    while countdown != 0:
        countdown = countdown - 1
        time.sleep(1)
        if countdown == 20 or countdown == 10:
            print(f"{countdown} seconds remaining.")

    print("")


def avgbp(bp1, bp2, bp3):

    # Averages the Blood Pressures that were previously collected.

    print(f"Calcuating average blood pressure")
    time.sleep(2)

    avg_sys = int(((bp1["sys"] + bp2["sys"] + bp3["sys"]) / 3))
    avg_dia = int(((bp1["dia"] + bp2["dia"] + bp3["dia"]) / 3))
    avg_pul = int(((bp1["PUL"] + bp2["PUL"] + bp3["PUL"]) / 3))

    print(f"\nAverage blood pressure: \n {avg_sys}/{avg_dia} {avg_pul}\n")

    avg_bp = {"avg_sys": avg_sys, "avg_dia": avg_dia, "avg_pul": avg_pul}

    return avg_bp


def reading_output(avg_bp):

    # Idenifys the diagnosis range that the Average sys is in.

    if avg_bp["avg_sys"] < 90:
        print(f"Your average sys is showing signs of Hypotension")

    elif avg_bp["avg_sys"] >= 91 and avg_bp["avg_sys"] <= 120:
        print(f"Your average sys is in a healthy range")

    elif avg_bp["avg_sys"] >= 121 and avg_bp["avg_sys"] <= 140:
        print(f"Your average sys is showing signs of Prehypertension")

    elif avg_bp["avg_sys"] >= 141 and avg_bp["avg_sys"] <= 160:
        print(f"Your average sys is showing signs of Hypertension Stage 1")

    elif avg_bp["avg_sys"] >= 161:
        print(f"Your average sys is showing signs of Hypertension Stage 2")

    # Idenifys the diagnosis range that the Average dia is in.

    if avg_bp["avg_dia"] < 60:
        print(f"Your average dia is showing signs of Hypotension")

    elif avg_bp["avg_dia"] >= 61 and avg_bp["avg_dia"] <= 80:
        print(f"Your average dia is in a healthy range")

    elif avg_bp["avg_dia"] >= 81 and avg_bp["avg_dia"] <= 90:
        print(f"Your average dia is showing signs of Prehypertension")

    elif avg_bp["avg_dia"] >= 91 and avg_bp["avg_dia"] <= 100:
        print(f"Your average dia is showing signs of Hypertension Stage 1")

    elif avg_bp["avg_dia"] >= 101:
        print(f"Your average dia is showing signs of Hypertension Stage 2")

    print("")
