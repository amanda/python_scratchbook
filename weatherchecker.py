import forecastio
from pyzipcode import ZipCodeDatabase

API_KEY = "blah"

def weatherchecker(zipcode, unit):
	zcdb = ZipCodeDatabase()
	if (len(zipcode) > 5 & zipcode.isdigit()):
		db_zipcode = zcdb[zipcode]
		lat = db_zipcode.latitude
		lng = db_zipcode.longitude
		forecast = forecastio.load_forecast(API_KEY, lat, lng)
		by_hour = forecast.hourly()
		current = forecast.currently()
		if unit == "C":
			temp = str(((current.temperature)-32)/1.8) + " C"
		else:	
			temp = str(current.temperature) + " F"
		print "The current temperature is " + temp
		print by_hour.summary
	else:
		print "Enter a valid U.S. zipcode."

if __name__ == '__main__':
	is_celsius = raw_input("Celsius or farenheit? Enter C or F: ")
	zipcode = raw_input("Enter your zipcode: ")
	weatherchecker(zipcode, is_celsius)
	