import C_DHT

while True:
    data = C_DHT.readSensor(0)
    if data[2] == 1:
        print("Temperature:", "{:.2f}".format(round(data[0], 2)) , " | ", "Humidity:", "{:.2f}".format(round(data[1], 2))  )
