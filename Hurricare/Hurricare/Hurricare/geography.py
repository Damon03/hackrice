import googlemaps
from geopy.distance import vincenty
import time,random

gmaps = googlemaps.Client(key='AIzaSyDlwbPWXXcICc959jzORo5vZ9v9ixtAHRk')

def getLocation(address):
    print("++++++++++++++")
    #info = gmaps.geocode(address)

    #print(info)
    #if len(info) == 0:
    #    return None
    #location = info[0]['geometry']['location']
    #return (location['lat'], location['lng'])
    time.sleep(0.5)
    return (random.randint(-90,90),random.randint(-180,180))

def distance(locationA, locationB):
    return vincenty(locationA, locationB).km