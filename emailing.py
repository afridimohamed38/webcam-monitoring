# def send_email():
#     print("Email was sent!")

import smtplib
import ssl
import os
import imghdr
from email.message import EmailMessage


def send_email(image_path):
    print("send email started")
    username = "afridimohamed38@gmail.com"
    password = os.getenv("APP_PASSWORD")

    receiver = "afridimohamed38@gmail.com"

    to_send_message = EmailMessage()
    to_send_message['Subject'] = "New customer showed up!"
    to_send_message.set_content("Hey we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()

    to_send_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, to_send_message.as_string())
    gmail.quit()
    print("send email ended")


if __name__ == "__main__":
    send_email(image_path="images/67.png")
