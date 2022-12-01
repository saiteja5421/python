package main

import "fmt"

func main() {
	//count := 0
	for i := 1; i <= 500; i++ {
		if i%7 == 0 && i%5 == 0 {
			fmt.Printf("%d ", i)
		}
	}
	birthady()
	positive()
}

func birthady() {
	time := 2022
	for i := 1998; i <= time; i++ {
		fmt.Printf("%d ", i)

	}
}

func positive() {
	nums := [...]int{30, -1, -6, 90, -6}

	for i, v := range nums {
		if v >= 0 {
			fmt.Printf("%d ", v)
			_ = i
		}
	}
}
