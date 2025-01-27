from requests import get, ConnectionError
from PIL import Image
import numpy as np

params = {"ll": "48.742562,55.752060",
          "spn": "0.008,0.004",
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
    #response2 = get("https://urban-university.ru/guarantee") через раз работает
    #print(response2.headers['x-host'])
    print("Status_code:", response.status_code)
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)
        print('Карта Иннополиса скачана')


with Image.open("map.png") as img:
    img.load()
    print(img.format, img.size)
    crop_img = img.crop((100, 50, 600, 450))
    crop_img.save("map_crop.png")
    print(crop_img.format, crop_img.size)
    tr_img = crop_img.transpose(Image.FLIP_TOP_BOTTOM)
    tr_img.show()


array_one = np.arange(1, 37).reshape(6, 6)
array_two = np.full((6, 6), 55)
print(f'Max value of array_one:{array_one.max()}')
print(f'Sum value of array_two:{array_two.sum()}')
print(array_one + array_two)
