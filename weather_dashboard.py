import requests
import matplotlib.pyplot as plt

API_KEY = "4c679af50c1b9ceb4a04e8885b5232fe"
CITY = "Kolhapur"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Pressure:", pressure, "hPa")

labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temperature, humidity, pressure]

plt.figure(figsize=(8,5))
plt.bar(labels, values)
plt.title(f"Weather Data Dashboard - {CITY}")
plt.xlabel("Parameters")
plt.ylabel("Values")
plt.show()

