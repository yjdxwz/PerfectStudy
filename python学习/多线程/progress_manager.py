from multiprocessing import Process, Queue, Manager, Pipe


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == '__main__':
    progress_dict = Manager().dict()

    # pipe 只能适用月 两个进程
    first_progress = Process(target=add_data, args=(progress_dict, "boobyy", 22,))
    sencode_progress = Process(target=add_data, args=(progress_dict, "boobyy2", 23,))

    first_progress.start()
    sencode_progress.start()

    first_progress.join()
    sencode_progress.join()

    print(progress_dict)
