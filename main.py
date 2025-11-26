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
    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
    # print(data)
    
      if data["cod"] == 200:
        self.display_weather(data)

    except requests.exceptions.HTTPError :
      # print(response.status_code)
      match response.status_code:
        case 400:
            self.display_error("400 - Bad Request: Please check the city name.")
        case 401:
            self.display_error("401 - Unauthorized: Invalid API key.")
        case 403:
            self.display_error("403 - Forbidden: Access denied.")
        case 404:
            self.display_error("404 - Not Found: City not found.")
        case 500:
            self.display_error("500 - Server Error: Try again later.")
        case _:
            self.display_error(f"Unexpected Error: {response.status_code}")
    except requests.exceptions.HTTPError:
        self.display_error("HTTP error:", response.status_code)

    except requests.exceptions.ConnectionError:
        self.display_error("Connection Error — check your internet connection.")

    except requests.exceptions.Timeout:
        self.display_error("Request timed out — server is too slow.")

    except requests.exceptions.TooManyRedirects:
        self.display_error("Too many redirects — invalid URL.")

    except requests.exceptions.RequestException as e:
        self.display_error("Unknown error:", e)
    
    
  def display_error(self, message):
    # print(message)
    self.temperature_label.setText(message)
    self.emoji_label.clear()
    self.description_label.clear()
  def display_weather(self,data):
    # print(data)
    temperature_k = data["main"]["temp"]
    temperature_c = temperature_k - 273.15
    temperature_f = (temperature_k * 9/5) - 459.67
    self.temperature_label.setText(f"{temperature_f:.0f}°F")
    
    weather_description = data["weather"][0]["description"]
    self.description_label.setText(weather_description)
    
    weather_id = data["weather"][0]["id"]
    self.emoji_label.setText(self.get_weather_emoji(weather_id))
  @staticmethod
  def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:         
            return '⛈️'
        elif 300 <= weather_id <= 321:       
            return '🌦️'
        elif 500 <= weather_id <= 531:       
            return '🌧️'
        elif 600 <= weather_id <= 622:       
            return '❄️'
        elif 700 <= weather_id <= 741:       
            return '🌫️'
        elif weather_id == 762:              
            return '🌋'
        elif 751 <= weather_id <= 761:      
            return '🌪️'
        elif weather_id == 781:         
            return '🌪️'
        elif weather_id == 800:              
            return '☀️'
        elif 801 <= weather_id <= 804:      
            return '☁️'
        else:
            return '🌍'   

    
    
if __name__ == "__main__":
   app = QApplication(sys.argv)
   WeatherApp_app = WeatherApp()
   WeatherApp_app.show()
   sys.exit(app.exec_())