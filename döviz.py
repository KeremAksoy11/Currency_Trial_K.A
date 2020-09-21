import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_doviz = input("Bozulan Döviz Türü Nedir: ")
alinan_doviz = input("Alınan Döviz Nedir: ")
miktar = int(input("Ne Kadar {} Bozdurmak İstiyorsunuz: ".format(bozulan_doviz)))

result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)
print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))

print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz],alinan_doviz))