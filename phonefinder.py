import phonenumbers as pn  #Phone info
from phonenumbers import carrier, geocoder, timezone #Phone info
import webbrowser
import time 
while True:
    try:
        phone = pn.parse(input('Enter phone number[ex. +30xxxxxxxxxx] = '))
        phoneL = input('Re-enter the phone number please = ')
        print('\033[34m<<<Check if the phone numbers are match>>>\033[0m')
        time_out = input('\033[32m---|Press Enter to continue|---\033[0m')
        print(phone)
        print('\033[36mValid number\033[0m:',pn.is_valid_number(phone))
        print('\033[36mProvider:\033[0m',carrier.name_for_number(phone,'en'))
        print('\033[36mCountry\033[0m:',geocoder.description_for_number(phone, 'en'))
        print('\033[36mGeo-location\033[0m:',timezone.time_zones_for_number(phone))
        
        bothering_numb =input('Do you think this number is spam/scam ?  y/N ')
        if bothering_numb =='y':
            print('\033[34mLeading you to site..\033[0m')
            print('Site error = no results -just remember')
            time.sleep(2)
            webbrowser.open('https://www.whoseno.com/')
        elif bothering_numb =='n':
            print('')
    except:
        print('\033[31mInvalid phone number\033[0m')
