import send
import utility


def order(subject, body):
	
	user_profile = utility.ReadFileJson('user_profile.json')
	send_profile = utility.ReadFileJson('send_profile.json')
	
	msg = send.CreateMessage(user_profile['Adress'], send_profile['Adress'], subject, body)
	send.SendMail(user_profile, msg)
	
	utility.ReturnHomeScreen()
