import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formatdate


# ----------------------------------------------------------------------------------------------------
# メールを作成
# ----------------------------------------------------------------------------------------------------
def CreateMessage(from_addr, to_addr, subject, body):

	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Date'] = formatdate()

	return msg


# ----------------------------------------------------------------------------------------------------
# メールを送信
# ----------------------------------------------------------------------------------------------------
def SendMail(user_profile, msg):

	smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
	smtpobj.login(user_profile['Adress'], user_profile['Password'])
	smtpobj.sendmail(msg['From'], msg['To'], msg.as_string())
	smtpobj.close()
