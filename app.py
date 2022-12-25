from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbcfc25858d83ab1b477529564d4d4114"
# Your Auth Token from twilio.com/console
auth_token  = "0be420042da05354dcea7fe0ba8475a2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+573004557509", 
    from_="+12077076834",
    body="Hello Cralie Feliz NAvidad!")

print(message.sid)