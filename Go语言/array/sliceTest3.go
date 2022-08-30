package main

import "fmt"

func printArrays(s []int) {
	fmt.Printf("len=%d, cap=%d\n", len(s), cap(s))
}
func main() {
	//arr := [...]int{0, 1, 2, 3, 4, 5, 6, 7}
	var s []int
	for i := 0; i <= 100; i++ {
		printArrays(s)
		s = append(s, i*2+1)
	}
	//	0 , 1 , 2 , 4, 8, 16 , 32
	//  9-16 -> 16
	//  17-32 -> 32
}
