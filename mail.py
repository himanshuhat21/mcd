import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('himanshubiswasvnbss@gmail.com','himuvnbsss14')


server.sendmail('himanshubiswasvnbss@gmail.com','biswashimanshu984@gmail.com','hey whats upp')


print('MAIL SENT')