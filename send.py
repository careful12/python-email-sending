from email.message import EmailMessage
import ssl
import smtplib

# set the sender
email_sender = 'b00303333@gmail.com'
# generate form step 6
email_password = password

# set the receiver
# go to https://temp-mail.org/ to generate a temp email to test
email_receiver = ''

# set the subject and content
subject = "Python email test"
body = """
Python email test
"""

# email message oject
em = EmailMessage()
# set headers
em['From'] = email_sender
# or em.add_header("From", email.sender)
em['To'] = email_receiver
em['subject'] = subject
# set content
em.set_content(body)

context = ssl.create_default_context()
'''
An SSL context holds various data longer-lived than single SSL connections, 
such as SSL configuration options, certificate(s) and private key(s). 
It also manages a cache of SSL sessions for server-side sockets, 
in order to speed up repeated connections from the same clients.
'''
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

'''
host - smtp server,  default is local host
port 465 is for ssl
as_string - Return the entire message flattened as a string.
'''
