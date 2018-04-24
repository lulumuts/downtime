from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC905360593c371acea0ec4417770b3fd5"
# Your Auth Token from twilio.com/console
auth_token  = "d962e83a5a6c92b72a2530e705db61eb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+254727481326",
    from_="+12522622704",
    body="events.message")

print(message.sid)
