package main

import (
	"fmt"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

type Astronaut struct {
	Name  string
	Craft string
}

func setupDB() {
	db, err := gorm.Open("sqlite3", "mydb")

	defer db.Close()

	if err != nil {
		panic("failed to connect to database")
	}

	db.AutoMigrate(&Astronaut{})
}

func main() {
	// getTopStories()
	fmt.Print("=== Starting Astro Search ===\n\n")

	setupDB()

	a1 := Astronaut{Name: "Allen", Craft: "ISS"}
	db.Create(&a1)

	var t1 Astronaut

	db.First(&t1)

	fmt.Println(t1.Name)
	fmt.Println(t1.Craft)

	fmt.Print("=== Terminating Astro Search ===\n\n")
}
