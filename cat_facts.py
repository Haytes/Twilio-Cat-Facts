# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import yaml
import random


with open("cred.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""+cfg['ACCOUNT_SID']
auth_token = ""+cfg['AUTH_TOKEN']
client = Client(account_sid, auth_token)
test_number = cfg['PHONE_NUM']
twilio_number = cfg['TWILIO_NUM']
test= random.choice(list(open('cat_facts.txt')))

message = client.messages.create(
    to = test_number,
    body= test,
    from_= twilio_number,
    media_url="http://thecatapi.com/api/images/get?format=src&type=gif"
)

