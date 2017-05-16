import threading, multiprocessing


class MyThread(threading.Thread):
    def __init__(self, fun, args, name=""):
        threading.Thread.__init__(self)
        self.fun = fun
        self.args = args
        self.name = name

    def run(self):
        self.result = apply(self.fun, self.args)

    def getResult(self):
        return self.result


def worker():
    x = 0
    while 1:
        x = x ^ 1


def main():
    l = multiprocessing.cpu_count()
    for i in range(l):
        t = threading.Thread(target=worker)
        t.start()


if __name__ == '__main__':
    main()