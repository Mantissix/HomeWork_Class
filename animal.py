import yaml
import os


class animals:
    name: str
    varietie: str
    color: str
    age: int
    gender: str
    skill: str

    def __init__(self,name, varietie, color, age, gender, skill):
        self.name = name
        self.varietie = varietie
        self.color = color
        self.age = age
        self.gender = gender
        self.skill = skill

    def sound(self):
        print('嗷呜')

    def running(self):
        print('Just go！')


class dog(animals):
    dogFur: str

    def __init__(self,name, varietie, color, age, gender, skill, dogFur):
        super().__init__(name, varietie, color, age, gender, skill)
        self.dogFur = dogFur

    def dogIntroduce(self):
        print(f'姓名：{self.name}\n品种：{self.varietie}\n颜色：{self.color}\n性别：{self.gender}\n年龄：{self.age}岁\n毛发：{self.dogFur}\n技能：{self.skill}')

    def saveDog(self):
        # 关于yaml.safe_dump补充：设置allow_unicode=True,可以将中文写入文件；设置sort_keys=False,则不会在排序后写入，如果要追加写入，则将读取方式由'w'改为'a'
        # 关于open函数，如果要打开的文件对象不存在，调用open函数时会自动在指定目录下创建一个该对象，如果存在，则直接调用
        dogProperty = {self.name: {'varietie': self.varietie, 'color': self.color, 'age': self.age, 'gender': self.gender, 'dogFur': self.dogFur, 'skill': self.skill}}
        if not os.path.exists('./datas/dogData'):
            with open('./datas/dogData', 'a', encoding='UTF-8') as dog1:
                yaml.safe_dump(dogProperty, dog1, allow_unicode=True, sort_keys=False)
            print('本地文件创建成功，狗狗数据已保存')
        else:
            with open('./datas/dogData', 'a', encoding='UTF-8') as dog1:
                yaml.safe_dump(dogProperty, dog1, allow_unicode=True, sort_keys=False)
            print('狗狗数据已保存')

class cat(animals):
    catFur: str

    def __init__(self,name, varietie, color, age, gender, skill, catFur):
        super().__init__(name, varietie, color, age, gender, skill)
        self.catFur = catFur

    def catIntroduce(self):
        print(f'姓名:{self.name}\n品种：{self.varietie}\n颜色：{self.color}\n性别：{self.gender}\n年龄：{self.age}岁\n毛发：{self.catFur}\n技能：{self.skill}')

    def saveCat(self):
        catProperty = {self.name: {'varietie': self.varietie, 'color': self.color, 'age': self.age, 'gender': self.gender, 'dogFur': self.catFur, 'skill': self.skill}}
        if not os.path.exists('./datas/catData'):
            with open('./datas/catData', 'a', encoding='UTF-8') as cat1:
                yaml.safe_dump(catProperty, cat1, allow_unicode=True, sort_keys=False)
            print('本地文件创建成功，猫咪数据已保存')
        else:
            with open('./datas/catData', 'a', encoding='UTF-8') as cat1:
                yaml.safe_dump(catProperty, cat1, allow_unicode=True, sort_keys=False)
            print('猫咪数据已保存')