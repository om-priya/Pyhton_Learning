"""
Make Sure to disable 2FA
"""
import smtplib
from email.message import EmailMessage

email_content = "hello"


email = EmailMessage()

email["Subject"] = "Test Email"
email["From"] = "email"
email["To"] = "god@gmail.com"

email.set_content(email_content)


smtp_connector = smtplib.SMTP(host="mail.guerrillamail.com.", port=587)
smtp_connector.starttls()
smtp_connector.login("email", "password")

smtp_connector.send_message(email)
smtp_connector.quit()
