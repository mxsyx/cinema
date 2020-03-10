import time
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from laofan import settings

class Email():
	def __init__(self):
		try:
			self.server = smtplib.SMTP_SSL()
		except Exception as e:
			print("\nemail init error -> " + str(e))

	def connect(self):
		try:
			self.server.connect(settings.SMTP_SERVER,settings.SMTP_PORT)
		except Exception as e:
			print("\nemail connect error -> " + str(e))
		try:
			self.server.helo()
			self.server.ehlo()
			self.server.login(settings.FROM_ADDR, settings.SMTP_PASSWORD)
		except Exception as e:
			print("\nemail login error -> " + str(e))

	def send(self,headline,context,filename=""):
		try:
			self.connect()
			msg = MIMEMultipart()
			msg.attach(MIMEText(context, 'plain', 'utf-8'))
			msg['Subject'] = Header(headline, 'utf-8').encode()
			msg['From'] = settings.FROM_ADDR
			msg['To'] = settings.TO_ADDR

			if(filename):	# 附带文件
				with open("/opt/log/" + filename, 'r') as f:
					mime = MIMEBase('text', 'plain', filename=filename.split('/')[-1])
					mime.add_header('Content-Disposition', 'attachment', filename=filename.split('/')[-1])
					mime.add_header('Content-ID', '<0>')
					mime.add_header('X-Attachment-Id', '0')
					mime.set_payload(f.read())	# read attachment information
					encoders.encode_base64(mime)
					msg.attach(mime)

			self.server.sendmail(settings.FROM_ADDR, settings.TO_ADDR, msg.as_string())
			self.server.close()
			print(time.strftime("\n" + "%Y-%m-%d %H:%M:%S", time.localtime()) + "  send email successful . . .")
		except Exception as e:
			print("\nemail send error -> %s" % str(e))