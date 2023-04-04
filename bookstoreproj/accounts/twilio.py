from twilio.rest import Client
from django.conf import settings
import random

twilio_account_sid = settings.TWILIO_ACCOUNT_SID
twilio_auth_token = settings.TWILIO_AUTH_TOKEN
twilio_phone_number = settings.TWILIO_PHONE_NUMBER


client = Client(twilio_account_sid, twilio_auth_token)

def send_otp_sms(phone_number):
    
    otp = str(random.randint(1000, 9999))

    message = client.messages.create(
            to=phone_number,
            from_=twilio_phone_number,
            body=f'Your hntjyhbdbgbtfnhtgfbgrfnhtbfbgrfdbgvrfhbgvr OTP is {otp}',
            )

    return message