package main

import (
	"fmt"
	"go_app/internal/utils"
)

func main() {

	// clear the console
	fmt.Print("\033[H\033[2J")

	// write a welcome message
	fmt.Println("Welcome to the Blood Pressure Averager")

	reading1 := utils.Reading(1)

	reading2 := utils.Reading(2)

	reading3 := utils.Reading(3)

	avgbp := utils.Avgbp(reading1, reading2, reading3)

	utils.Diagnose(avgbp)

}
