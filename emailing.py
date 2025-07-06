import smtplib,ssl
import os
from email.message import EmailMessage

host="smtp.gmail.com"
port=587
username="subbu.venkat86@gmail.com"
paswword="eoux uydp pwzb pmhp"

receiver_email="srividya.srinivas88@gmail.com"
context = ssl.create_default_context()


def send_email(image_path,Message,thread=None):
    print("Sending email...")
    
    if not os.path.exists(image_path):
        print(f"Image path {image_path} does not exist.")
        return
    
    email_message = EmailMessage()
    email_message['Subject'] = 'Movement Detected'  
    email_message.set_content(Message)
    email_message.add_attachment(open(image_path, 'rb').read(), maintype='image', subtype=os.path.splitext(image_path)[1][1:], filename=os.path.basename(image_path))   

    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls(context=context)
    gmail.login(username, paswword)
    gmail.sendmail(username,receiver_email, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("images/image.png", "Movement detected, see the attached image.")

    # with smtplib.SMTP_SSL(host,port,context=context) as server:
    #     server.login(username,paswword)
    #     server.sendmail(username,receiver_email,Message)
