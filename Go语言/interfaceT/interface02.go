package main

import (
	"fmt"
	"go-study/interfaceT/mock"
	real2 "go-study/interfaceT/real"
)

//duck typing

// 描述事物的外部行为 而非内部结构
// 像鸭子走路, 像鸭子叫  , 那么就是鸭子
// 结构化类型系统

// Retriever 接口的实现时隐式的
// 只要实现接口里的方法
type Retriever interface {
	Get(url string) string
}

func download(r Retriever) string {
	return r.Get("http://www.baidu.com")
}

type Poster interface {
	Post(url string, form map[string]string) string
}

func post(poster Poster) {
	poster.Post("http://www.imooc.com", map[string]string{
		"name":   "ccmouse",
		"course": "goland",
	})
}

type RetrieverPoster interface {
	Retriever
	Poster
}

//type
func main() {
	var r Retriever
	r = mock.Retriever{Contents: "this is fake data"}

	var r2 Retriever
	r2 = real2.Retriever{UserAgent: "agg"}

	fmt.Println(download(r))
	fmt.Println(download(r2))
}
