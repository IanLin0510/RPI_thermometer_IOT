//pip3 install jsons
import json
//value of temperature is in value.py
json_temp=json.dumps(temperature)
//value of huminity is in value.py
json_hum=json.dumps(huminity)
txt='Temp:'+json_temp+'C/Humidity:'+json_hum
with open('data.json','w') as obj:
  json.dump(txt.obj)
