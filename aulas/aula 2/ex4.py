temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for temp in temperaturas:
    if temp < 37.5:
        status = "Normal"
    elif 37.5 <= temp <= 38.5:
        status = "Febre moderada"
    else:
        status = "Febre alta"
    
    print(f"Temperatura: {temp}°C → {status}")