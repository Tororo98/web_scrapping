import urllib.request
from urllib.request import urlopen
import os.path
import json
import csv

req = urlopen('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1M')

datos = json.loads(req.read())

with open('BTCUSDT.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')

    for fila in datos:
        print(fila)
        writer.writerow(fila)