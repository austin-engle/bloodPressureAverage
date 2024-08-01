package main

import (
	"reflect"
	"testing"
    "go_app/internal/utils"
)

func TestReading(t *testing.T) {
    expected := map[string]int{
        "SYS": 0,
        "DIA": 0,
        "PUL": 0,
    }
    result := utils.Reading(1)
    if !reflect.DeepEqual(result, expected) {
        t.Errorf("reading() failed, expected %v, got %v", expected, result)
    }
}

func TestAvgbp(t *testing.T) {
    expected := map[string]int{
        "SYS": 120,
        "DIA": 80,
        "PUL": 76,
    }
    // Create three sample readings
    reading1 := map[string]int{"SYS": 130, "DIA": 90, "PUL": 80}
    reading2 := map[string]int{"SYS": 120, "DIA": 70, "PUL": 60}
    reading3 := map[string]int{"SYS": 110, "DIA": 80, "PUL": 90}
    // Call the avgbp function with the sample readings
    result := utils.Avgbp(reading1, reading2, reading3)
    // Check if the result matches the expected output
    if !reflect.DeepEqual(result, expected) {
        t.Errorf("avgbp() failed, expected %v, got %v", expected, result)
    }
}

// no return from diagnose so no way to test
