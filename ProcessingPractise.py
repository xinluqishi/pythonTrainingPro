from multiprocessing import Process, Queue
import os, time, random
import multiprocessing


# Practising to the communicating in the multiprocess
# writing data process
def process_write(q, urls):
    print('Process (%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())


# reading data process
def process_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)


# send message in the Pipe way
def process_send(pipe, urls):
    for url in urls:
        print('Process(%s) send: %s' % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def process_rec(pipe):
    while True:
        print('Process(%s) rev:%s' % (os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    # q = Queue()
    # process_write1 = Process(target=process_write, args=(q, ['url_1', 'url_2', 'url_3']))
    # process_write2 = Process(target=process_write, args=(q, ['url_3', 'url_4', 'url_5']))
    # process_reader = Process(target=process_read, args=(q,))
    #
    # process_write1.start()
    # process_write2.start()
    #
    # process_reader.start()
    #
    # process_write1.join()
    # process_write2.join()
    #
    # process_reader.terminate()

    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=process_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=process_rec, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()







