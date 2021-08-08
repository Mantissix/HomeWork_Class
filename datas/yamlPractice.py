import yaml


person = {'name': 'Lucy', 'age': 20, 'gender': 'female'}
# yaml.safe_load()是将yaml格式转换成python对象
# yaml.safe_dump()是将python对象转换成yaml格式
with open("./dataPractice", encoding='UTF-8') as practice:
    print(yaml.safe_load(practice))
    print(yaml.safe_dump(person))