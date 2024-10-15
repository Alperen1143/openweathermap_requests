import requests


api_key = '893f1b45840b1fa94047acd3e4a16b91'


cities = ['Istanbul', 'Ankara','Londra','Burdur']


for city in cities:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()


    if response.status_code == 200:
        print(f"\nŞehir: {data['name']}")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Durum: {data['weather'][0]['description']}")
    else:
        print(f"\nVeri alınamadı: {city}")
