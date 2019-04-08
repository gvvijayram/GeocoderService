import requests

from properties import hereAPIURL, hereAppCode, hereAppID, locationIQAPIURL, \
    locationIQKey, locationIQFormat


# REST Geocoding Service
class GeocodingServiceRest(object):

# Getting Data From HereMaps Geocoding Service
    def getResponseUsingRESTFromHereGeocoding(self, searchText):
        # GET Request To Webservice
        JSONResponse = requests.get(hereAPIURL, params={"app_id":hereAppID, "app_code":hereAppCode, "searchtext":searchText})
        print("Accessing : " + JSONResponse.url)
        print("JSON Output :\n")
        # Printing the Webservice Response
        jsonRes = JSONResponse.json()
        print(jsonRes)
        return jsonRes

# Getting Data From HereMaps LocationIQ Service
    def getResponseUsingRESTFromLocationIQGeocoding(self, searchText):
        # GET Request To Webservice
        JSONResponse = requests.get(locationIQAPIURL, params={"key":locationIQKey, "q":searchText, "format":locationIQFormat})
        print("Accessing : " + JSONResponse.url)
        # Printing the Webservice Response
        jsonRes = JSONResponse.json()
        
        print("JSON Output :\n")
        print(jsonRes)
        return jsonRes
