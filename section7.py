################################
#クラスの定義

# class Person(object):
#     def say_something(self):
#         print("hello")

# person = Person()
# person.say_something()

################################
#クラスの初期化とクラス変数
# class Person(object):
#     def __init__(self, name="hibiki"):
#         self.name = name
#         print(self.name)
#     def say_something(self):
#         print(f"I am {self.name}.hello")
#         self.run()

#     def run(self, num=5):
#         print("run" * num)

# person = Person()
# person.say_something()

################################
#コンストラクタとデストラクタ
# class Person(object):
#     def __init__(self, name="hibiki"):
#         self.name = name
#         print(self.name)
#     def say_something(self):
#         print(f"I am {self.name}.hello")
#         self.run()

#     def run(self, num=5):
#         print("run" * num)

#     def __del__(self):
#         print("good bye")

# person = Person()
# person.say_something()
# del person
# print("###################")
################################
#クラスの継承
# class Car(object):
#     def run(self):
#         print("run")

# class ToyotaCar(Car):
#     pass

# class TeslaCar(Car):
#     def auto_run(self):
#         print("auto run")

# car = Car()
# car.run()
# print("###############")
# toyota_car = ToyotaCar()
# toyota_car.run()
# print("###############")
# tesla_car = TeslaCar()
# tesla_car.auto_run()
# tesla_car.run()

################################
#メソッドのオーバーライドとsuperによる親のメソッドの呼び出し

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
        
#     def run(self):
#         print("run")

# class ToyotaCar(Car):
#     def run(self):
#         print("fast")
    

# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False):
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run
#     def run(self):
#         print("super fast")
#     def auto_run(self):
#         print("auto run")

# car = Car()
# car.run()
# print("###############")
# toyota_car = ToyotaCar("Lexus")
# print(toyota_car.model)
# toyota_car.run()
# print("###############")
# tesla_car = TeslaCar("Model S")
# print(tesla_car.model)
# tesla_car.auto_run()
# tesla_car.run()
################################
#プロパティを使った属性の設定
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
        
#     def run(self):
#         print("run")

# class ToyotaCar(Car):
#     def run(self):
#         print("fast")
    
# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False, passwd = "123"):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run
#         self.passwd = passwd

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
    
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == "456":
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print(self.__enable_auto_run)
#         print("super fast")
#     def auto_run(self):
#         print("auto run")

# tesla_car = TeslaCar("Model S", passwd = "456")
# tesla_car.run()
#print(tesla_car.__enable_auto_run)

################################
#クラスを構造体として扱う時の注意点
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
        
#     def run(self):
#         print("run")

# class ToyotaCar(Car):
#     def run(self):
#         print("fast")
    
# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False, passwd = "123"):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run
#         self.passwd = passwd

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
    
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == "456":
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print(self.__enable_auto_run)
#         print("super fast")
#     def auto_run(self):
#         print("auto run")

# tesla_car = TeslaCar("Model S", passwd = "456")
# #tesla_car.__enable_auto_run = "XXXXXXXXXXXXXXXx"
# print(tesla_car.__enable_auto_run)

# class T(object):
#     pass

# t = T()
# t.name = "Mike"
# t.age = 20
# print(t.name, t.age)

################################
#ダックタイピング
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print("ok")
#         else:
#             raise Exception("No drive")
        
# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
        
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
        

# baby = Baby()
# adult = Adult()

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
        
#     def run(self):
#         print("run")
    
#     def ride(self, person):
#         person.drive()

# car = Car()
# car.ride(adult)

# class ToyotaCar(Car):
#     def run(self):
#         print("fast")
    
# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False, passwd = "123"):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run
#         self.passwd = passwd

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
    
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == "456":
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print(self.__enable_auto_run)
#         print("super fast")
#     def auto_run(self):
#         print("auto run")

# tesla_car = TeslaCar("Model S", passwd = "456")
# #tesla_car.__enable_auto_run = "XXXXXXXXXXXXXXXx"
# #print(tesla_car.__enable_auto_run)

# class T(object):
#     pass

# t = T()
# t.name = "Mike"
# t.age = 20
# print(t.name, t.age)

################################
#抽象クラス
# import abc

# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age=1):
#         self.age = age

    
#     @abc.abstractclassmethod
#     def drive(self):
#         pass
        
# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
        
#     def drive(self):
#         raise Exception('No drive')
        
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
        
#     def drive(self):
#         print('ok')
        

# baby = Baby()
# adult = Adult()
# adult.drive()

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
        
#     def run(self):
#         print("run")
    
#     def ride(self, person):
#         person.drive()

# car = Car()
# car.ride(adult)

# class ToyotaCar(Car):
#     def run(self):
#         print("fast")
    
# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False, passwd = "123"):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run
#         self.passwd = passwd

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
    
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == "456":
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print(self.__enable_auto_run)
#         print("super fast")
#     def auto_run(self):
#         print("auto run")

# tesla_car = TeslaCar("Model S", passwd = "456")
# #tesla_car.__enable_auto_run = "XXXXXXXXXXXXXXXx"
# #print(tesla_car.__enable_auto_run)

# class T(object):
#     pass

# t = T()
# t.name = "Mike"
# t.age = 20
# print(t.name, t.age)

################################
#多重継承
# class Person(object):
#     def talk(self):
#         print("talk")

#     def run(self):
#         print("Person run")

# class Car(object):
#     def run(self):
#         print("Car run")

# class PersonCarRobot(Car, Person):
#     def fly(self):
#         print("fly")

# person_car_robot =  PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()

################################
#クラス変数
# class Person(object):
#     kind  = "human"#クラス変数

#     def __init__(self, name):
#         self.name = name
        

#     def who_are_you(self):
#         print(self.name, self.kind)

# a = Person("A")
# a.who_are_you()
# b = Person("B")
# b.who_are_you()

# class T(object):
#     def __init__(self):
#         self.words = []#インスタンス変数

#     def add_word(self, word):
#         self.words.append(word)

# c = T()

# c.add_word("add 1")
# c.add_word("add 2")
# print(c.words)

# d = T()
# d.add_word("add 3")
# d.add_word("add 4")
# print(d.words)

################################
#クラスメソッドとスタティックメソッド

# class Person(object):

#     kind = "human"

#     def __init__(self):
#         self.x = 100

#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind
    
#     @staticmethod
#     def about(year):
#         print(f"about human {year}")

# a = Person()
# print(a.what_is_your_kind())

# b = Person
# print(b.what_is_your_kind())

# print(Person.what_is_your_kind())

# Person.about(1999)

################################
#特殊メソッド

# class Word(object):
#     def __init__(self, text):
#         self.text = text
    
#     def __str__(self):
#         return "Word!!!!"
    
#     def __len__(self):
#         return len(self.text)
    
#     def __add__(self, word):
#         return self.text.lower() + word.text.lower()
    
#     def __eq__(self, word):
#         return self.text.lower() == word.text.lower()
    
# w = Word("Test")
# w2 = Word("##########")
# print(w + w2)    


