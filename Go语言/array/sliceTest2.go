package main

import "fmt"

// 切片 含左不含右, 是视图
func main() {
	arr := [...]int{0, 1, 2, 3, 4, 5, 6, 7}
	s1 := arr[2:6]
	s2 := s1[3:5]
	s3 := append(s2, 10)
	s4 := append(s3, 11)
	s5 := append(s4, 12)
	fmt.Println(s1)  // {2,3,4,5}
	fmt.Println(s2)  // {5, 6}
	fmt.Println(s3)  // {5,6, 10}
	fmt.Println(s4)  // {5,6, 10,11}
	fmt.Println(s5)  // {5,6, 11, 12}
	fmt.Println(arr) // [0 1 2 3 4 5 6 10]

}
