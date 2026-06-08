class Sensor:
    def __init__(self, temperatura_inicial):
        self.__temperatura = 0.0
        self.set_temperatura(temperatura_inicial)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print(f"Erro: Temperatura {temperatura}°C fora do limite físico do sensor (-50 a 150).")

    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "Normal"
        elif 81 <= self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

sensor = Sensor(25.0)

print(f"Temperatura: {sensor.get_temperatura()}°C | Status: {sensor.status()}")

sensor.set_temperatura(95.5)
print(f"Temperatura: {sensor.get_temperatura()}°C | Status: {sensor.status()}")

sensor.set_temperatura(130.0)
print(f"Temperatura: {sensor.get_temperatura()}°C | Status: {sensor.status()}")

sensor.set_temperatura(180.0)