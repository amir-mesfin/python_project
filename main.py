import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter City Name :", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button = QPushButton("Get Weather", self)
    self.temperature_label = QLabel(self)
    self.emoji_label = QLabel(self)
    self.description_label = QLabel(self)
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Weather App")
    
    vbox = QVBoxLayout()
    
    vbox.addWidget(self.city_label)
    vbox.addWidget(self.city_input)
    vbox.addWidget(self.get_weather_button)
    vbox.addWidget(self.temperature_label)
    vbox.addWidget(self.emoji_label)
    vbox.addWidget(self.description_label)
    
    self.setLayout(vbox)
    
    self.city_label.setAlignment(Qt.AlignCenter)
    self.city_input.setAlignment(Qt.AlignCenter)
    self.temperature_label.setAlignment(Qt.AlignCenter)
    self.emoji_label.setAlignment(Qt.AlignCenter)
    self.description_label.setAlignment(Qt.AlignCenter)
    
    self.city_label.setObjectName("city_label")
    self.city_input.setObjectName("city_input")
    self.get_weather_button.setObjectName("get_weather_button")
    self.temperature_label.setObjectName("temperature_label")
    self.emoji_label.setObjectName("emoji_label")
    self.description_label.setObjectName("description_label")
    
    self.setStyleSheet("""
            QWidget {
                background-color: #e8eaed;
                font-family: Calibri;
            }

            /* Labels */
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #222;
            }

            /* Input box */
            QLineEdit {
                padding: 12px;
                border: 2px solid #999;
                border-radius: 8px;
                background: #ffffff;
                font-size: 18px;
                min-width: 250px;
            }

            /* Button */
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 12px;
                font-size: 18px;
                border-radius: 8px;
                min-width: 200px;
            }

            QPushButton:hover {
                background-color: #0062cc;
            }

            QPushButton:pressed {
                background-color: #004a99;
            }
        """)

# make layout centered with spacing
    vbox.setSpacing(20)
    vbox.setContentsMargins(40, 40, 40, 40)
    self.get_weather_button.clicked.connect(self.get_weather)
  
  def get_weather(self):
    api_key = "d5698f8902350c831f2b1c234be1e5b5"
    city = self.city_input.text()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    print(data)
    
  def display_error(self, message):
    pass  
  def display_weather(self):
    pass
  
if __name__ == "__main__":
   app = QApplication(sys.argv)
   WeatherApp_app = WeatherApp()
   WeatherApp_app.show()
   sys.exit(app.exec_())