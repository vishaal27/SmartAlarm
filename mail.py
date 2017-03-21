import imaplib
import email
import time
from espeak import espeak

user="vishaal16119@iiitd.ac.in"
password=""
mail=imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities)=mail.login(user,password)
mail.list()
mail.select("INBOX")
mail_from_store=[]
mail_subject_store=[]

n=0
(retcode, messages)=mail.search(None,'(UNSEEN)')
if(retcode=='OK'):
	for num in messages[0].split():
		n+=1
		result,data=mail.fetch(num,'(RFC822)')
		for r in data:
			if(isinstance(r,tuple)):
				o=email.message_from_bytes(r[1])
				print(o['From'])
				print(o['Subject'])
				mail_from_store.append(o['From'])
				mail_subject_store.append(o['Subject'])
				print()
				result,data=mail.store(num,'+FLAGS','\\Seen')


print(n)
s='Vishaal, You have '+str(n)+' unread mails       Do you want me to read the names of the senders and the subjects of the mails?'
espeak.synth(s)
time.sleep(10)


ch=input()
if(ch=='no'):
	exit()
elif(ch=='yes'):
	for i in range(len(mail_from_store)):
		s1='You have a mail from '+str(mail_from_store[i])+' and the subject is '+str(mail_subject_store[i])
		espeak.synth(s1)
		time.sleep(10)
