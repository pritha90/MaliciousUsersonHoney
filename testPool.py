import requests
import sys
IS_PY2 = sys.version_info < (3, 0)

if IS_PY2:
    from Queue import Queue
else:
    from queue import Queue

from threading import Thread


class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()
        self.result = None

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                self.result = func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()
    def get_result(self):
        return self.result

class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        self.results = []
        for _ in range(num_threads):
            w =   Worker(self.tasks)
            self.results.append(w.get_result())

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()

    def get_results(self):
        return self.results

def getRequest(i):
    response = requests.get("https://d.joinhoney.com/stores/flipkart/?coupons=1")
    return response.status_code

if __name__ == "__main__":
    from random import randrange
    from time import sleep

    N = 10
    # Instantiate a thread pool with 5 worker threads
    pool = ThreadPool(5)

    # Add the jobs in bulk to the thread pool. Alternatively you could use
    # `pool.add_task` to add single jobs. The code will block here, which
    # makes it possible to cancel the thread pool with an exception when
    # the currently running batch of workers is finished.
    #pool.map(getRequest, data)
    for n in range(1, N+1):
        pool.add_task(getRequest, n)
    pool.wait_completion()
    #results = pool.get_results()
