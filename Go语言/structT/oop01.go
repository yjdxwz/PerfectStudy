package main

import "fmt"

// 封装 ， 不支持继承 多态
// go 语言没有class ， 只有 struct
// 不论地址还是结构本身， 一律使用 . 访问成员

// 堆栈? 不需要知道
// 只有指针才可以改变结构内容
// nil 指针也可以调用方法!
// 要改变内容使用 指针接受者
// 结构过大也考虑使用指针
// 一致性 , 如 有指针接收者, 最好都是指针接收者

// 值 接收者 是 go 语言特有

type treeNode struct {
	//i,j int
	value       int
	left, right *treeNode
}

func main() {
	var root treeNode
	fmt.Println(root)
	root = treeNode{value: 3}
	root.left = &treeNode{}
	root.right = &treeNode{5, nil, nil}
	root.right.left = new(treeNode)
}
