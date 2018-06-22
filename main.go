package main

import (
	"os"

	"github.com/elastic/beats/libbeat/cmd"

	"github.com/goomzee/burrowbeat/beater"
)

func main() {
    var RootCmd = cmd.GenRootCmd("burrowbeat", "", beater.New)
	err := RootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}
