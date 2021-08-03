import imaplib
email_user = input('Email: ')
email_pass = input('Password: ')

obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login(email_user, email_pass)
# it will select inbox
obj.select('Inbox')
typ ,data = obj.search(None,'UnSeen')
obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')