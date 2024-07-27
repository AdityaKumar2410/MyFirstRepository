import pywhatkit as kit

# Specify the recipient's phone number (with country code)
recipient_number = "+919xxxxxxxxx"

# Message to be sent
message = "Hello from Python! 🚀"

# Schedule the message (24-hour format)
# Example: Send the message at 6:30 PM
kit.sendwhatmsg(recipient_number, message, 18, 30)