import forecastio
from pyzipcode import ZipCodeDatabase

api_key = "0a555c7fc17950bf42d68315e25b1544"
zcdb = ZipCodeDatabase()

isCelsius = raw_input("Celsius or farenheit? Enter C or F: ")
zipcode = raw_input("Enter your zipcode: ")

if (len(zipcode) > 5 & zipcode.isdigit()):
	db_zipcode = zcdb[zipcode]
	lat = db_zipcode.latitude
	lng = db_zipcode.longitude
	forecast = forecastio.load_forecast(api_key, lat, lng)
	
	byHour = forecast.hourly()
	current = forecast.currently()
	if isCelsius == "C":
		temp = str(((current.temperature)-32)/1.8) + " C"
	else:	
		temp = str(current.temperature) + " F"
	print "The current temperature is " + temp
	print byHour.summary

else:
	print "Enter a valid U.S. zipcode."