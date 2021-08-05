"""
写一个Bicycle（自行车）类
    有run（骑行）方法，调用时显示骑行里程（骑行里程为传入的数字）

写一个EBicycle（电动自行车）类继承Bicycle类
    添加电池电量battery_level属性，通过参数传入
    同时有两个方法
        fill_charge(vol)用来充电，vol为充至满电所需电量，满格电量为100
        run（km）方法用于骑行，每骑行10km消耗1度电
        注：当电量耗尽时，调用Bicycle的run方法骑行
通过传入的骑行里程数，显示骑行结果（即剩余电量可骑行里程数）

"""


class Bicycle:
    def run(self, b_km):
        print(f"当前已骑行{b_km}公里")


class EBicycle(Bicycle):
    battery_level = 0

    def __init__(self, battery_level):
        self.battery_level = battery_level
        print(f"当前电量剩余{self.battery_level}%, 还可行驶{self.battery_level * 10}公里")

    def fill_charge(self, vol):
        if 20 < self.battery_level <= 50:
            print(f"当前剩余电量{self.battery_level}%，请注意使用")

        elif self.battery_level <= 20:
            print(f"提示：剩余电量不足20%，请充电")
            print("充电中。。。")
            # 即 self.battery_level = self.battery + vol
            self.battery_level += vol
            if self.battery_level >= 100:
                print(f"电池已充满")

            elif 0 < self.battery_level < 100:
                print(f"当前电量剩余{self.battery_level}%, 还可行驶{self.battery_level * 10}公里")

    def run(self, eb_km):
        print("行驶中。。。")
        for i in range(3):
            print("。。。")
        # auto_km = eb_km
        # km_battery_level = eb_km / 10
        # self.battery_level -= km_battery_level
        # if self.battery_level > 0:
        #     print(f"剩余电量{self.battery_level}%，已自动骑行{eb_km}公里，共计行驶{eb_km}公里")

        # else:
        #     print("电量已耗尽，正在转入手动模式。。。")
        #     print("请输入想要继续行驶的里程数：")
        #     new_km = int(input())
        #     eb_km += new_km
        #     Bicycle().run(eb_km)
        #     print(f"已自动骑行{auto_km}公里，手动骑行{new_km}公里，共计行驶{eb_km}公里")

        if eb_km > self.battery_level * 10:
            manual_km = eb_km - self.battery_level * 10
            print(f"当前已行驶{eb_km}公里， 其中电动行驶{self.battery_level * 10}公里，手动行驶{manual_km}公里")

        else:
            print(f"当前已行驶{eb_km}公里， 其中电动行驶{self.battery_level * 10}公里，手动行驶0.0公里")
