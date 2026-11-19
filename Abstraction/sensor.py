from abc import ABC, abstractmethod
import random

class Sensor(ABC):

    @abstractmethod
    def get_data(self):
        pass

class TempSensor(Sensor):
    def get_data(self):
      if random.random() <= 0.25:
        self.not_cooperate()
      else:
        print(f"[Temperature Sensor] Reading: {round(random.uniform(0,99),1)}°C")

    def not_cooperate(self):
      print("LOL I HATE U I DONT WANNA DO ANYTHING LELELELELE *dies*")

class pHSensor(Sensor):
    def get_data(self):
      if random.random() <= 0.25:
        self.not_cooperate()
      else:
        ph_lv = round(random.uniform(0,99),1)
        ph_scale = None
        if ph_lv == 7.0:
          ph_scale = "Neutral"
        elif ph_lv < 7.0:
          ph_scale = "Acidic"
        elif ph_lv > 7.0:
          ph_scale = "Basic"
        print(f"[pH Sensor] Reading: {ph_lv} pH ({ph_scale})")

    def not_cooperate(self):
      print("LOL I HATE U I DONT WANNA DO ANYTHING LELELELELE *dies*")

my_sensor = TempSensor()
my_sensor2 = pHSensor()

print("--- Lab Inventory System ---")
my_sensor.get_data()
my_sensor2.get_data()
print("-----------------------------")