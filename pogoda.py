import requests

x = input("в каком городе вывести погоду? ")
pogoda = requests.get(f'https://wttr.in/{x}?format=3')
pc_pogoda = pogoda.content.decode("utf-8")
print(pc_pogoda)
