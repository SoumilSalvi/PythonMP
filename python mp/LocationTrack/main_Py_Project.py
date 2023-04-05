import phonenumbers
from numbers_Py_Project import number

from phonenumbers import geocoder
from phonenumbers import carrier
 
import folium
 
from opencage.geocoder import OpenCageGeocode
phoneNumber = phonenumbers.parse(number)
Key = " d10f61a812bd450ebb235d88186c33f1" 
yourLocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+yourLocation)
yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+yourServiceProvider)

geocoder = OpenCageGeocode(Key)
query = str(yourLocation)

results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
myMap.save("Location.html")