import imaplib
import email
#from espeak import espeak 

mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login('vishaal16119@iiitd.ac.in','')
mail.list()
mail.select('INBOX')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print ('Processing ')
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_string(response_part[1])

             print (original['From'])
             print (original['Subject'])
             typ, data = mail.store(num,'+FLAGS','\\Seen')

print (n)
