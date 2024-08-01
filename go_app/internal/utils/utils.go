package utils

import "fmt"

func reading(readingNumber int) map[string]int {
	var ReadingSYS int
	var ReadingDIA int
	var ReadingPUL int

	fmt.Println("What is the SYS of the", readingNumber, "reading?")
	fmt.Scanln(&ReadingSYS)

	fmt.Println("What is the DIA of the", readingNumber, "reading?")
	fmt.Scanln(&ReadingDIA)

	fmt.Println("What is the PUL of the", readingNumber, "reading?")
	fmt.Scanln(&ReadingPUL)


	fmt.Println(readingNumber, "Blood Pressure Reading is:")
	fmt.Printf("%d/%d %d\n\n", ReadingSYS, ReadingDIA, ReadingPUL)

	return_value := map[string]int{
		"SYS": ReadingSYS,
		"DIA": ReadingDIA,
		"PUL": ReadingPUL,
	}
	// return this these as an dictionary
	return return_value
}

func avgbp(reading1, reading2, reading3 map[string]int) map[string]int {
	// average the three readings
	// return the average
	return_value := map[string]int{
		"SYS": (reading1["SYS"] + reading2["SYS"] + reading3["SYS"])/3,
		"DIA": (reading1["DIA"] + reading2["DIA"] + reading3["DIA"])/3,
		"PUL": (reading1["PUL"] + reading2["PUL"] + reading3["PUL"])/3,
	}

	fmt.Println("The average blood pressure is:")
	fmt.Printf("%d/%d %d\n\n", return_value["SYS"], return_value["DIA"], return_value["PUL"])

	return return_value
}

func diagnose(reading map[string]int) {
	// diagnose the reading
	// return the diagnosis

	var sys_diagnosis string
	var dia_diagnosis string

	diagnosis_map := map[string]string{
		"1": "Hypotension",
		"2": "Normal Blood Pressure",
		"3": "Prehypertension",
		"4": "Stage 1 Hypertension",
		"5": "Stage 2 Hypertension",
	}


	if num := reading["SYS"]; num < 90 {
		fmt.Printf("Your average SYS is showing signs of hypotension\n\n")
		sys_diagnosis = "1"
	} else if num >= 91 && reading["SYS"] <= 120 {
		fmt.Printf("Your average SYS is showing signs of normal blood pressure\n\n")
		sys_diagnosis = "2"
	} else if num >= 121 && reading["SYS"] <= 140 {
		fmt.Printf("Your average SYS is showing signs of prehypertension\n\n")
		sys_diagnosis = "3"
	} else if num >= 141 && reading["SYS"] <= 160 {
		fmt.Printf("Your average SYS is showing signs of stage 1 hypertension\n\n")
		sys_diagnosis = "4"
	} else if num >= 161 {
		fmt.Printf("Your average SYS is showing signs of stage 2 hypertension\n\n")
		sys_diagnosis = "5"
	}

	// Check the DIA reading
	if num := reading["DIA"]; num < 60 {
		// If the DIA is less than 60, it is considered to be in hypotension
		fmt.Println("Your average DIA is showing signs of hypotension")
		dia_diagnosis = "1"
	} else if num >= 61 && reading["DIA"] <= 80 {
		// If the DIA is between 61 and 80, it is considered to be in normal blood pressure
		fmt.Println("Your average DIA is showing signs of normal blood pressure")
		dia_diagnosis = "2"
	} else if num >= 81 && reading["DIA"] <= 90 {
		// If the DIA is between 81 and 90, it is considered to be in prehypertension
		fmt.Println("Your average DIA is showing signs of prehypertension")
		dia_diagnosis = "3"
	} else if num >= 91 && reading["DIA"] <= 100 {
		// If the DIA is between 91 and 100, it is considered to be in stage 1 hypertension
		fmt.Println("Your average DIA is showing signs of stage 1 hypertension")
		dia_diagnosis = "4"
	} else if num >= 101 {
		// If the DIA is 101 or greater, it is considered to be in stage 2 hypertension
		fmt.Println("Your average DIA is showing signs of stage 2 hypertension")
		dia_diagnosis = "5"
	}


	fmt.Printf("Your diagnosis is: %s/%s\n\n", diagnosis_map[sys_diagnosis], diagnosis_map[dia_diagnosis])
}
