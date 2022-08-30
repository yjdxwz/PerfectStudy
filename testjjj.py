class Driver:

    pass



def process(threading="null"):
    a =Driver()



def main():
    # 开启4个进程，传入爬取的页码范围
    thead_list = []
    t1 = Thread(target=process,args=(1,))
    t1.start()

    t2 = Thread(target=process,args=(2,))
    t2.start()

    thead_list.append(t1)
    thead_list.append(t2)
    for t in thead_list:
        t.join()

if __name__ == '__main__':
    s = time.time()
    main()
    e = time.time()
    print('总用时：',e-s)