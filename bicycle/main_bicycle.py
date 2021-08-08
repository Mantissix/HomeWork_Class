import bicycle
import yaml

with open('../datas/bicycleData') as bicycleData:
    bd = yaml.safe_load(bicycleData)

bd1 = bd['data2']

b1 = bicycle.EBicycle(bd1[0])
b1.run(bd1[1])