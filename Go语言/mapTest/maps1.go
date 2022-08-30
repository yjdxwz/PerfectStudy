package main

import "fmt"

func main() {

	m := map[string]string{
		"name":    "ccmouse",
		"course":  "golang",
		"site":    "imooc",
		"quality": "notbad",
	}
	m2 := make(map[string]int)
	var m3 map[string]int
	fmt.Println(m)
	fmt.Println(m2)
	fmt.Println(m3)
	//	 遍历, key 在这里面是无序的， 每次打印的顺序是不固定的
	for k, v := range m {
		fmt.Println(k, v)
	}
	/**
	name ccmouse
	course golang
	site imooc
	quality notbad
	*/

	//	 获取key key 不存在， 会获得初始值
	coursename := m["name"]
	fmt.Println(coursename)
	sss, ok := m["sssss"]
	fmt.Println(sss, ok)
	if sss, ok := m["cause"]; ok {
		fmt.Println(sss)
	} else {
		fmt.Println("Key does not exits")
	}

	// 删除元素
	//name, ok := m["name"]啥

	delete(m, "name")
	for k, v := range m {
		fmt.Println(k, v)
	}
}
