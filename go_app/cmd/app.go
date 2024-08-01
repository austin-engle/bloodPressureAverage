package main

import (
	"fmt"
	// "utils"

	"github.com/austin_engle/bloodpressureaverage/internal/utils"
	// "os"
	// "strconv"
)



func main() {

	// clear the console
	fmt.Print("\033[H\033[2J")

	// write a welcome message
	fmt.Println("Welcome to the Blood Pressure Averager")

	reading1 := utils.reading(1)

	reading2 := utils.reading(2)

	reading3 := utils.reading(3)

	avgbp := utils.avgbp(reading1, reading2, reading3)

	utils.diagnose(avgbp)

}
