package main

import "fmt"

func printArray(arr [5]int) {
	for i, v := range arr {
		fmt.Println(i, v)
	}

}

func printArrayPoint(arr *[5]int) {
	arr[0] = 100
	for i, v := range arr {
		fmt.Println(i, v)
	}

}

func main() {
	var arr1 [5]int
	arr2 := [3]int{1, 3, 5}
	arr3 := [...]int{2, 4, 6, 8, 10}
	fmt.Println(arr1, arr2, arr3)

	// 遍历 数组
	for i := 0; i < len(arr3); i++ {
		fmt.Println(arr3[i])
	}

	for i := range arr3 {
		fmt.Println(arr3[i])
	}

	fmt.Println("---------")
	printArray(arr1)
	printArray(arr3)
	//printArray(arr2)
	fmt.Println(arr1)
	fmt.Println(arr3)
	printArrayPoint(&arr1)
	printArrayPoint(&arr3)
	fmt.Println(arr1)
	fmt.Println(arr3)
}
