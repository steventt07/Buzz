import smtplib
import yaml
from yaml import Loader
from email.message import EmailMessage

# EMAIL_ADDRESS = 'steven@bubble.llc'
# EMAIL_PASSWORD = 'ygejlkjataaijrqk'

class EmailServer:
	def __init__(self, config_file):
		self.config = self.load_configuration(config_file)
		
	def load_configuration(self, config_file):
		print('Loading email configuration...')
		with open(config_file, 'r') as filehandle:
			config = yaml.load(filehandle.read(), Loader=Loader)
			return config
	
	def send_email(self, verificaiton_code):
		
		msg = EmailMessage()
		msg['Subject'] = 'Bubble Verification Code'
		msg['From'] = self.config['email']
		msg['To'] = self.config['email']
		msg.set_content(verificaiton_code)
		
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(self.config['email'], self.config['password'])

			smtp.send_message(msg)