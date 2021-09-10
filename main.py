import string
import random
import time
import crayons
from discord_webhook import *

print("{}".format(crayons.red('use this spammer to fuck webhooks and servers')))
print("{}".format(crayons.red('join our discord server if u like it.\n')))

def send():
    webhook = DiscordWebhook(url=webhookurl, content="@everyone https://discord.gg/impop") # Webhook url and message content
    response = webhook.execute()

# SETTINGS
webhookurl = 'Your webhook here!'

changewh = input("Do you want to change the web hook url, say y if you haven't changed it in the file else say N. (y/n) > ")
if changewh == "y":
    webhookurl = input("You have chosen to change the web hook url, paste it here and press enter. > ")

amount = 0
amount = input("How many messages would you like to be sent? ")
print("You have chose to send "+ amount +" messages.")


for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() 
    print("all messages have been sent")
    time.sleep(1.65) # waits 1.65 seconds due to ratelimits.

print('\nmessages have been sent')
time.sleep(5)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
