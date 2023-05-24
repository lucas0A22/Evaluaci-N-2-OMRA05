import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "o96hlGT1YBx1O5ugHOBOmztacjcy7HvJ"

while True:
    orig = input("Ciudad de Origen: ")
    if orig =="q":
        break
    dest = input("Ciudad de destino: ")
    if dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("desde " + orig + " a " + dest)
        print("Duracion: " + json_data["route"]["formattedTime"])
        distance = json_data["route"]["distance"]
        rounded_distance = round(distance, 2)
        print("Kilometros: " + str(rounded_distance))
        print("=============================================")
