import requests
from config import KEY


city = "Lviv"

url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric&lang=ua-uk'.format(city,KEY)

res = requests.get(url)

data = res.json()

# for i in data:
#     print(i,'\t->\t',data[i])

weather = f"Опис: {data['weather'][0]['description'].capitalize()}"

# weather = "Опис: " + data['weather'][0]['description'].capitalize() + "\n"
weather += f"Температура {data['main']['temp']}\n"
weather += f"Вітер: швидкість -> {data['wind']['speed']}\n"
weather += f"Кут (0-359) -> {data['wind']['deg']}*\n"
weather += f"Вологість -> {data['main']['humidity']}%"
print(weather)

# from PIL import Image
# import os
# img = data['weather'][0]['icon']
# image = Image.open(os.path.dirname(__file__) + '/png/' + img + '.png')
# image.show()