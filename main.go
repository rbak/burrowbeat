package main

import (
	"os"

	"github.com/elastic/beats/libbeat/beat"

	"github.com/goomzee/burrowbeat/beater"
)

func main() {
	err := beat.Run("burrowbeat", "", beater.New)
	if err != nil {
		os.Exit(1)
	}
}
