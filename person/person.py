class Person:
    # 静态属性
    name: str
    gender: str
    age = 0
    # 私有属性
    __deposit = 0

    def __init__(self, name, gender, age, deposit):
        self.name = name
        self.gender = gender
        self.age = age
        self.__deposit = deposit

    def instroduce(self):
        print(f"大家好，我叫{self.name}，我今年{self.age}岁，我是个{self.gender}")

    def sing(self):
        pass

    def dance(self):
        pass

    def rap(self):
        pass

    def basketball(self):
        pass

    def depositshow(self):
        return self.__deposit

    def depositsearch(self):
        print(f"我有{self.__deposit}元存款")

    def __secret(self):
        print("我有一个秘密")


class teacher(Person):
    def __init__(self, name, gender, age, deposit, skill):
        super().__init__(name, gender, age, deposit)
        self.skill = skill


"""
""
创建一个Person类
包含姓名、年龄、性别、存款基础属性
包含自我介绍、吃、睡、娱乐、工作基础方法
""

class Person:
    # 静态属性
    name: str
    gender: str
    age = 0
    # 私有属性
    __deposit = 0

    def __init__(self, name, gender, age, deposit):
        self.name = name
        self.gender = gender
        self.age = age
        self.__deposit = deposit
        pass

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁，我是个{self.gender}生")

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleeping")

    def amusement(self):
        print("amusement")

    def job(self):
        print("working")

    def deposit(self):
        return self.__deposit

    def depositSearch(self):
        print(f"我有{self.__deposit}元存款")

    def __secret(self):

        pass


class Comedian(Person):
    skill: str

    def __init__(self, name, gender, age, deposit, skill):
        super().__init__(name, gender, age, deposit)
        self.skill = skill

    def act(self):
        print(f"{self.name}正在表演")
"""
