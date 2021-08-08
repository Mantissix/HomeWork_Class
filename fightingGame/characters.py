"""
一个回合制游戏，游戏中有两个角色，每个角色都有HP、Power、Armor三种基本属性，主角属性有初始值
HP代表血量（初始值为100），Power代表攻击力（初始值为10），Armor代表护甲（初始值为10）
定义一个fight方法
    final_HP = HP - enemy_Power + My_Armor
    enemy_final_HP = enemy_HP - my_Power + enemy_Armor
    血量变为0的一方获胜
"""
import random


class game_characters:
    pro_hp: int
    pro_power: int
    pro_armor: int

    enemy_hp: int
    enemy_power: int
    enemy_armor: int

    def __init__(self):
        self.pro_hp = random.randint(100, 120)
        self.pro_power = random.randint(10, 15)
        self.pro_armor = random.randint(0, 5)

        self.enemy_hp = random.randint(120, 150)
        self.enemy_power = random.randint(5, 10)
        self.enemy_armor = random.randint(0, 10)

    def fight(self):
        while self.pro_hp >= 0 and self.enemy_hp >= 0:
            self.pro_hp = self.pro_hp - self.enemy_power + self.pro_armor
            self.enemy_hp = self.enemy_hp - self.pro_power + self.enemy_armor
            print(f"主角当前剩余血量：{self.pro_hp}")
            print(f"敌人当前剩余血量：{self.enemy_hp}")

        if self.pro_hp > self.enemy_hp:
            print("Win")
        else:
            print("Lose")


class protagonist(game_characters):
    def introduce(self):
        print(f"血量：{self.pro_hp} 攻击力：{self.pro_power} 护甲：{self.pro_armor}")

    def protagonist_back(self):

        pass


class enemy(game_characters):
    def introduce(self):
        print(f"血量：{self.enemy_hp} 攻击力：{self.enemy_power} 护甲：{self.enemy_armor}")

    def enemy_back(self):

        pass
