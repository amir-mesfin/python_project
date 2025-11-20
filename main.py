import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter City Name :", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button = QPushButton("Get Wether", self)
    self.temperature_label = QLabel("45")
    
    
if __name__ == "__main__":
   app = QApplication(sys.argv)
   WeatherApp_app = WeatherApp()
   WeatherApp_app.show()
   sys.exit(app.exec_())