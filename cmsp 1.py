class SensorTemperatura:
    def __init__(self, temperatura=0):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, nova_temperatura):
        if -50 <= nova_temperatura <= 150:
            self.__temperatura = nova_temperatura
        else:
            print("Temperatura fora do intervalo permitido.")

# Uso da classe
sensor = SensorTemperatura()
sensor.set_temperatura(25)
print(sensor.get_temperatura())  # Saída: 25
sensor.set_temperatura(200)  # Saída: Temperatura fora do intervalo permitido.
print(sensor.get_temperatura())  # Saída: 25 (a temperatura não foi alterada devido ao valor inválido)

