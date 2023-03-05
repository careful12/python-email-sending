# python email sender

ref: [Code With Tomi - Send Emails With Python [UPDATED]](https://www.youtube.com/watch?v=zxFXnLEmnb4&ab_channel=CodeWithTomi)

---

## Before coding

| Step 1 | Step 2 |
| -------- | -------- |
|<img src=https://i.imgur.com/136Fs6b.png >|<img src=https://i.imgur.com/kHodizq.png>|

|Step 3 |
| -------- |
|<img src=https://i.imgur.com/ROzth3q.png>
**需先完成兩步驟認證**|

|Step 4|
|------|
|![](https://i.imgur.com/AGzVNEJ.png)|

|Step 5|
|------|
|![](https://i.imgur.com/oYaGyeg.png)|

|Step 6|
| ------ |
|![](https://i.imgur.com/7I4bghB.png)
**複製他給的密碼**|


## Start coding

**Step 7 - finish code**

```python
from email.message import EmailMessage
import ssl
import smtplib

# set the sender
# your gmail
email_sender = 'b00303333@gmail.com'
# generate form step 6
email_password = password

# set the receiver
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

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
```

|Step 8|
|------|
|到 [https://temp-mail.org/](https://temp-mail.org/) 測試![](https://i.imgur.com/Lqgx33g.png)|

**Step 9**
- 將複製的email貼到email_receiver
```python
# set the receiver
email_receiver = ''
```

**Step 10 - Execute Your Code**

---


|測試結果|
|------|
|![](https://i.imgur.com/tNFOBud.png)
![](https://i.imgur.com/fAsBjgp.png)|
