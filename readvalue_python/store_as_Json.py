//pip3 install jsons
import json
json_temp=json.dumps(temperature)
json_hum=json.dumps(huminity)
txt='Temp:'+json_temp+'C/Humidity:'+json_hum
with open('data.json','w') as obj:
  json.dump(txt.obj)
