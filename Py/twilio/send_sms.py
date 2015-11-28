from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
ACCOUNT_SID = "AC1ee9e019a4caea947d0941797b32e141"
AUTH_TOKEN = "ffe7df1f9f7b97e36f1b165e249b5043"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(body="I am testing twilio bro <3",
    to="+19192000708",    # Replace with your phone numbers
    from_="+19195337660") # Replace with your Twilio number

print(message.sid)
