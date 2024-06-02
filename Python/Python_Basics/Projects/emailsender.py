# from email.message import EmailMessage
# import ssl
# import smtplib

# email_sender = 'documentprofesionally@gmail.com'
# email_receiver = 'pavanpanja395@gmail.com'
# email_password = ''

# subject = "test email trigger using python script"
# body = """This is test email triggering via python script"""

# em = EmailMessage
# em['From'] = email_sender
# em['To'] = email_receiver
# em['subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context

# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string)
########################################################################################

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#your gmail credentials
gmail_user = "documentprofesionally@gmail.com"
gmail_password = ""

#receipient email address
to_email = "pavanpanja395@gmail.com"

#Create the message
subject = "Test email trigger using python script"
body = "test email via python"
message = MIMEMultipart()
message["From"] = gmail_user
message["To"] = to_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Set up the SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #Login to your Gmail acccount
    server.login(gmail_user, gmail_password)
    # Send the email
    server.sendmail(gmail_user, to_email, message.as_string())
print("Email sent successfully!")
