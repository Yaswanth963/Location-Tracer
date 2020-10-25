import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
#Mention your phone number with country code
number="+91xxxxxxxxxx"
ch_num=phonenumbers.parse(number,"CH")
print("Location:"+geocoder.description_for_number(ch_num,"en"))
service_number=phonenumbers.parse(number,"RO")
print("Service Provider:"+carrier.name_for_number(service_number,"en"))