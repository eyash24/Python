# lesson: Web Services: Service Oriented Approach, Web Services: APIs
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

# API: Application Program Interface 
import urllib.request, urllib.error, urllib.parse
import json

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = service_url + urllib.parse.urlencode({'address' : address})
    print("Retrieving ", url)
    url_open = urllib.request.urlopen(url)
    data = url_open.read().decode()
    print("Retrieved ",len(data)," characters")
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] !='OK':
        print("=======Failure to retrieve=======")
        print(data)
        continue

    lat = js['result'][0]['geometry']['location']['lat']
    lng = js['result'][0]['geometry']['location']['lng']
    print("Latitude: ",lat)
    print("Longitude: ",lng)

    location = js['result'][0]['formatted_address']
    print(location)

"""
Output:
Enter location: Ann Arbor, MI       
Retrieving  https://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
Retrieved  237  characters
=======Failure to retrieve=======
{
   "error_message" : "You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account",
   "results" : [],
   "status" : "REQUEST_DENIED"
}

Enter location:
"""

