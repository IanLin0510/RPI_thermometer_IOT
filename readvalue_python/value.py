//在虛擬環境內執行
//pip3 install adafruit_CircuitPython_DHT
import time
import board
import adafruit_dht
from datetime import datetime
//用四腳接到DHT22的訊號端
dht22=adafruit_dht.DHT22(board.D4)
//執行的函式
def value():
  while True:
    now=datetime.now()
    temperature=dht22.temperature
    humidity=dht22.humidity
    a=now.strftime("%Y/%m/%d,%H:%M:%S")
    print(a,temperature,humidity)
    time.sleep(3)
value()
