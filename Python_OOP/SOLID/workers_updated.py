from abc import ABCMeta, abstractmethod, ABC
import time


class Work(ABC):
    @abstractmethod
    def work(self):
        pass


class Eat(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Work, Eat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class Robot(Work):

    def work(self):
        print("I'm a robot. I'm working....")


class WorkManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, Work), "`worker` must be subclass of {}".format(Work)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, Eat), "`worker` must be subclass of {}".format(Eat)

        self.worker = worker

    def manage(self):
        self.worker.work()
