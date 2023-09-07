package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type Person struct {
	Name           string `json:"name"`
	TechnicalSkills float64    `json:"Technical methods"`
	SoftSkills      float64    `json:"Soft Skills"`
	BusinessSkills  float64    `json:"Business Skills"`
	CreativeSkills  float64    `json:"Creative Skills"`
	AcademicSkills  float64    `json:"Academic Skills"`
}

type People struct {
	People []Person `json:"people"`
}

func main() {
	// Read the JSON file
	jsonFile, err := os.Open("data2.json")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer jsonFile.Close()

	jsonBytes, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	var people People
	err = json.Unmarshal(jsonBytes, &people)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// Create a CSV file
	csvFile, err := os.Create("data3.csv")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer csvFile.Close()

	writer := csv.NewWriter(csvFile)
	defer writer.Flush()

	// Write header
	err = writer.Write([]string{"Name", "Technical Skills", "Soft Skills", "Business Skills", "Creative Skills", "Academic Skills"})
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// Write data
	for _, person := range people.People {
		row := []string{
			person.Name,
			fmt.Sprint(person.TechnicalSkills),
			fmt.Sprint(person.SoftSkills),
			fmt.Sprint(person.BusinessSkills),
			fmt.Sprint(person.CreativeSkills),
			fmt.Sprint(person.AcademicSkills),
		}
		err = writer.Write(row)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
	}
}
