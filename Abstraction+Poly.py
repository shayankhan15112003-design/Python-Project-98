from abc import ABC, abstractmethod

class AbsClass:
    def print(self, x):
        print("Passed Value: ", x)


    @abstractmethod
    def task(self):
        print("We are inside abstract method!")

class test_class(AbsClass):
    def task(self):
        print("We are inside test_class Class!")

test_obj = test_class()
test_obj.task()
test_obj.print(100)

