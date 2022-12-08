package main

import (
	"fmt"
	add "myapp/linux"
)

func Sub(a, b int) int {
	return a - b
}

func main() {
	fmt.Println(add.Add(10, 20))
	//add.Add(10, 20)
}
