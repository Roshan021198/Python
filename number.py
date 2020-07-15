import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

#Enter phone number with country code
phone_number = phonenumbers.parse("+917319854538")

#this will print the country name
print(geocoder.description_for_number(phone_number,'en'))

#This will provide the sevice provider name
print(carrier.name_for_number(phone_number,'en'))
