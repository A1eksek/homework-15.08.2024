#Первая задача
# class Singleton:
#     _instance = None
#
#     def __new__(perper, *args, **kwargs):
#         if not perper._instance:
#             perper._instance = super(Singleton, perper).__new__(perper)
#         return perper._instance
#
#     def some_method(self):
#         return "Это метод класса Singleton"
#
# singleton1 = Singleton()
# singleton2 = Singleton()
# print(singleton1 is singleton2)
# print(singleton1.some_method())

#Вторая задача

# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method.")
# class Dog(Animal):
#     def speak(self):
#         return "Гав!"
# class Cat(Animal):
#     def speak(self):
#         return "мяу!"
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type):
#         if animal_type.lower() == "dog":
#             return Dog()
#         elif animal_type.lower() == "cat":
#             return Cat()
#         else:
#             raise ValueError("Unknown animal type.")
#
#
# if __name__ == "__main__":
#     dog = AnimalFactory.create_animal("dog")
#     print("Собака говорит:", dog.speak())
#
#     cat = AnimalFactory.create_animal("cat")
#     print("Кот говорит:", cat.speak())

#Третья задача

class Subject:
    def __init__(self):
        self._observers = []

    def fafas(self, observer):

        self._observers.append(observer)

    def fufus(self, observer):

        self._observers.remove(observer)

    def fifus(self):

        for observer in self._observers:
            observer.update(self)


class Observer:
    def update(self, subject):

        raise NotImplementedError("Subclass must implement abstract method")


class ConcreteObserverA(Observer):
    def update(self, subject):
        print("ConcreteObserverA: Обновление получено от", subject)


class ConcreteObserverB(Observer):
    def update(self, subject):
        print("ConcreteObserverB: Обновление получено от", subject)


if __name__ == "__main__":

    subject = Subject()


    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()


    subject.fafas(observer_a)
    subject.fafas(observer_b)


    subject.fifus()


    subject.fufus(observer_a)


    subject.fifus()
