package main

import "fmt"

// 切片 含左不含右, 是视图
func main() {
	arr := [...]int{0, 1, 2, 3, 4, 5, 6, 7}
	s := arr[2:6]
	fmt.Println(s) //[2 3 4 5]
	fmt.Println(arr[:6])
	fmt.Println(arr[2:])
	fmt.Println(arr[:])

	fmt.Println(arr)
	//s[0] = 100
	fmt.Println(arr)
	s2 := s[3:5] // 超出部分 会在原始 arr 中 往后取
	fmt.Println(s2)
	fmt.Println(cap(s)) // 容量
}
