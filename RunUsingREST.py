from GeocodingServiceREST import GeocodingServiceRest
geoCodingService = GeocodingServiceRest();
print("Running GeoCoding Service")

# Enter Search Location
searchText = input("Enter the Location You Want to Search For :\n")

#Use Primary service, if not use secondary service
try :
	jsonResp = geoCodingService.getResponseUsingRESTFromHereGeocoding(searchText)
except:
    try :
        print("\n\n*****Error From Primary(HereMaps) GeoCoding Service!*****\n\n")
        jsonResp = geoCodingService.getResponseUsingRESTFromLocationIQGeocoding(searchText)
    except:
        print("\n\n*****Error From Secondary (LocationIQ) GeoCoding Service!*****\n\n")
        print("--Please check the location--\n")
        exit(-1)

# Extract latitude and logitude from json response and print them..
latitude = jsonResp['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
longitude = jsonResp['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
print("Latitude :: " + str(latitude))
print("Longitude :: " + str(longitude))
