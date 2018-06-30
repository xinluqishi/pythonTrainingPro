from multiprocessing import Pool
import os, time, random


def run_task(name):
    print("Task %s (pid = %s) is running..." % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print("Task %s end." % name)


if __name__ == '__main__':
    print("Current process %s." % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i, ))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()   #调用join之前调用close，调用close后就不能添加新的线程了
    print("All subprocesses done.")


