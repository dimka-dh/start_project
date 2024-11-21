import requests
from xml.etree import ElementTree as ET
import numpy
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageDraw, ImageFont

# requests
print('requests')
url = "https://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)

if response.status_code == 200:
    root = ET.fromstring(response.content)

    for currency in root.findall("Valute"):
        char_code = currency.find("CharCode").text
        value = currency.find("Value").text
        if char_code in ["USD", "EUR"]:
            print(f"{char_code}: {value} руб.")
else:
    print(f"Ошибка запроса: {response.status_code}")

# numpy
print('numpy')
array = numpy.arange(1, 11)
squares = numpy.square(array)
mean_value = numpy.mean(array)
print("Исходный массив:", array)
print("Квадраты элементов массива:", squares)
print("Среднее значение массива:", mean_value)

# matplotlib
x = numpy.linspace(0, 2 * numpy.pi, 100)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_sin, label="sin(x)", color="blue", linestyle="-")
plt.plot(x, y_cos, label="cos(x)", color="red", linestyle="--")
plt.title("График функций sin(x) и cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# pillow
print('pillow')

image = Image.open("test.jpg")
print("Размер изображения:", image.size)

resized_image = image.resize((200, 200))
resized_image.save("resized_test.jpg")

blurred_image = image.filter(ImageFilter.GaussianBlur(5))
blurred_image.save("blurred_test.jpg")

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 30)
draw.text((50, 50), "Непонятно как работает этот код!", fill="white", font=font)
image.show()
image.save("text_test.jpg")
