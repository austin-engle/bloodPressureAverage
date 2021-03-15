from time import sleep
import os
import datetime
import csv
from statistics import mean

now = datetime.datetime.now()

if len(str(now.month)) == 1:
    month = f"0{now.month}"
    print(month)
else:
    month = now.month

if len(str(now.day)) == 1:
    day = f"0{now.day}"
    print(day)
else:
    day = now.day

date = f"{month}/{day}/{now.year}"

time_24hr = f"{now.hour}:{now.minute}"
d = datetime.datetime.strptime(time_24hr, "%H:%M")
time_12hr = d.strftime("%I:%M %p")


def clear():

    # Clears the console
    os.system("clear")


def reading(num):

    # Gathers the blood pressure readings.

    print(f"Please take the {num} reading now.\n")
    sleep(30)

    correct = None
    sys = None
    dia = None
    pul = None

    while correct != "yes" and correct != "y" and correct != "1":

        # TODO add error handling for value errors (right now a '' will break the script, Likely need to remove the int and make it an int later in the script)
        sys = int(input(f"What is the SYS of the {num} reading? "))
        dia = int(input(f"What is the DIA of the {num} reading? "))
        pul = int(input(f"What is the PUL of the {num} reading? "))

        print(f"\n{num.capitalize()} Blood Pressure reading:\n {sys}/{dia} {pul}\n")
        sleep(1)

        correct = input("Is this the correct blood pressure reading? (Yes/No) ").lower()

        print("")

    bp = {"sys": sys, "dia": dia, "pul": pul}

    return bp


def countdown():

    # Countdown timer for 30 seconds

    countdown = 30
    print(f"Please wait {countdown} seconds before continuing.")

    while countdown != 0:
        countdown = countdown - 1
        sleep(1)
        if countdown == 20 or countdown == 10:
            print(f"{countdown} seconds remaining.")

    print("")


def avgbp(bp1, bp2, bp3):

    # Averages the Blood Pressures that were previously collected.

    print(f"Calculating average blood pressure")
    sleep(2)

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
        sys_diagnosis = "1"

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
        dia_diagnosis = "1"

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
        "1": "Hypotension",
        "2": "Normal",
        "3": "Prehypertension",
        "4": "Stage 1 Hypertension",
        "5": "Stage 2 Hypertension",
    }

    if sys_diagnosis == "1" or dia_diagnosis == "1":
        diagnosis = dia["1"]

    elif sys_diagnosis > dia_diagnosis:
        diagnosis = dia[sys_diagnosis]

    elif sys_diagnosis < dia_diagnosis:
        diagnosis = dia[dia_diagnosis]
    else:
        diagnosis = "Unable to gather diagnosis"

    return diagnosis


def tags():
    tags_arm = {"1": "Right arm", "2": "Left arm"}

    tags_position = {"1": "Seated", "2": "Laying Down"}

    arm_choice = None
    position_choice = None

    while arm_choice != "1" and arm_choice != "2":
        arm_choice = input(
            "Did you take the reading with your Right(1) or Left(2) arm?\n"
        )

    while position_choice != "1" and position_choice != "2":
        position_choice = input(
            "Were you seated(1) or laying down(2) when taking the reading?\n"
        )

    tags = f"{tags_arm[arm_choice]} | {tags_position[position_choice]}"

    return tags


def push_to_github():

    # Pushes the updates to github automatically as the end of the script
    sleep(3)
    os.system("git add * >/dev/null 2>&1")
    sleep(2)
    os.system(
        f"git commit -m 'commit after blood pressure reading: {date} {time_12hr}' >/dev/null 2>&1"
    )
    sleep(2)
    os.system(f"git push >/dev/null 2>&1")

    print("Pushed to git successfully, exiting script")


def write_to_csv(avg_bp, diagnosis, tags):

    # rows to gather

    # SYS
    sys = avg_bp["avg_sys"]

    # DIA
    dia = avg_bp["avg_dia"]

    # PUL
    pul = avg_bp["avg_pul"]

    # BPZ
    bpz = diagnosis

    # TAGS
    tags = tags

    # DATE,TIME,SYS,DIA,PUL,BPZ,TAGS
    csv_write_format = date, time_12hr, sys, dia, pul, bpz, tags

    import csv

    with open(
        r"bloodpressure.csv",
        "a",
    ) as f:
        writer = csv.writer(f)
        writer.writerow(csv_write_format)


def average_over_time(t):

    # Calculate the average blood pressure over time from the csv file

    sys_data = []
    dia_data = []
    pul_data = []
    attempt = None

    try:
        for i in range(t):
            n = str(now - datetime.timedelta(days=i)).replace("-", "/")

            year = n[0:4]
            month = n[5:7]
            day = n[8:10]

            adj_date = f"{month}/{day}/{year}"
            # print(adj_date)
            with open(
                "bloodpressure.csv",
                newline="",
            ) as csvfile:
                csv_data = csv.DictReader(csvfile)
                for row in csv_data:
                    # print(row)
                    if row["DATE"] == adj_date:
                        # print("match")
                        sys = int(row["SYS"])
                        dia = int(row["DIA"])
                        pul = int(row["PUL"])
                        sys_data.append(sys)
                        dia_data.append(dia)
                        pul_data.append(pul)
        print(sys_data)
        print(dia_data)
        print(pul_data)
        avg_data = {
            "sys": round(mean(sys_data)),
            "dia": round(mean(dia_data)),
            "pul": round(mean(pul_data)),
        }
        print(avg_data)

    except:
        print("Unable to pull historical data trying again")
        attempt += 1
        if attempt == 2:
            raise ValueError("Unable to gather historical data")
        else:
            pass

    return avg_data


def all_time_average():

    # Calculate the average blood pressure from all data in the csv file

    sys_data = []
    dia_data = []
    pul_data = []

    with open("bloodpressure.csv", newline="") as csvfile:
        csv_data = csv.DictReader(csvfile)
        for row in csv_data:
            sys = int(row["SYS"])
            dia = int(row["DIA"])
            pul = int(row["PUL"])
            sys_data.append(sys)
            dia_data.append(dia)
            pul_data.append(pul)

    avg_data = {
        "sys": round(mean(sys_data)),
        "dia": round(mean(dia_data)),
        "pul": round(mean(pul_data)),
    }

    return avg_data


def print_averages():
    with open("averages.txt", "r") as file:
        print(file.read())


def write_averages_to_file(
    avg_bp, seven_day_average, thirty_day_average, ninty_day_average, all_time_average
):

    # Writes the averages to a file for easy tracking

    latest_reading_message = f'{date}\nLatest Reading: {avg_bp["avg_sys"]}/{avg_bp["avg_dia"]} {avg_bp["avg_pul"]}'
    seven_day_average_message = f'7 Day Average: {seven_day_average["sys"]}/{seven_day_average["dia"]} {seven_day_average["pul"]}'
    thirty_day_average_message = f'30 Day Average: {thirty_day_average["sys"]}/{thirty_day_average["dia"]} {thirty_day_average["pul"]}'
    ninty_day_average_message = f'90 Day Average: {ninty_day_average["sys"]}/{ninty_day_average["dia"]} {ninty_day_average["pul"]}'
    all_time_average_message = f'All Time Average: {all_time_average["sys"]}/{all_time_average["dia"]} {all_time_average["pul"]}'

    print(
        f"{latest_reading_message}\n{seven_day_average_message}\n{thirty_day_average_message}\n{ninty_day_average_message}\n{all_time_average_message}",
        file=open(
            "averages.txt",
            "w",
        ),
    )
