from simplegmail import Gmail

gmail = Gmail()

# Unread messages in your inbox

# Starred messages
#messages = gmail.get_starred_messages()

def checkEmailUnRead():
    messages = gmail.get_unread_inbox()
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject:" + message.subject)
        print("Message Body: " + message.plain)
    return True
def checkEmailStored():
    messages = gmail.get_starred_messages()
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject:" + message.subject)
        print("Message Body: " + message.plain)
    return True
def senderCheck():
    return 0