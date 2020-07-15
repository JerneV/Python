import yaml
import re

import random


def getLastPlant():
    with open('plants.yml', 'r') as file:
        data = yaml.safe_load(file)
    # print(data['plants'])
    if data['plants'] is not None:
        data_list = list(data['plants'])
        last_item = data_list[-1:][0]
        return int(re.match('.*?([0-9]+)$', last_item).group(1))
    return 1


def addNewPlant(lat, lon, logger, **kwargs):
    if kwargs.get("country_code") is not None:
        country_code = kwargs.get("country_code")
    else:
        country_code = ''
    if kwargs.get("name") is not None:
        name = kwargs.get("name")
    else:
        country_code = ''
    plant_id = "plant_" + str(getLastPlant()+1).zfill(3)
    print("New plant with ID: ", plant_id)
    newData = {plant_id: {
        'country_code': country_code, 'longitude': lon, 'latitude': lat, 'name': name, 'logger': logger
    }}

    with open('plants.yml', 'r') as file:
        data = yaml.safe_load(file)
        data['plants'].update(newData)
    if data:
        with open('plants.yml', 'w') as file:
            yaml.safe_dump(data, file)

for x in range(0,5):
    addNewPlant(random.randint(0, 50), random.randint(0, 6), str(random.random()), name= str(random.random()))

# plants.yml in following format:
# plants:
#   plant_001:
#     country_code: XX
#     latitude: 46.023111
#     logger: LoggerType
#     longitude: -0.572528
#     name: PlantName
