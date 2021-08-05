from multiprocessing import Process


def func1():
    rocket = 0
    print('start func1')
    while rocket < 100000000:
        rocket += 1
    print(f"func1: {rocket}")
    return


def func2():
    rocket = 0
    print('start func2')
    while rocket < 100000000:
        rocket += 1
    print(f"func2: {rocket}")
    return


if __name__ == '__main__':
    p1 = Process(target=func1).start()
    p2 = Process(target=func2).start()
