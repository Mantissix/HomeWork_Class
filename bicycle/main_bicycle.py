import bicycle
import yaml

data5 = {'data5': {'battery': 20, 'km': 300}}
with open('../datas/bicycleData', 'w') as bicycleData:
    # bd = yaml.safe_load(bicycleData)
    yaml.safe_dump(data5, stream=bicycleData)

# print(bd)
# bd1 = bd['data4']

# b1 = bicycle.EBicycle(bd1['battery'])
# b1.run(bd1['km'])