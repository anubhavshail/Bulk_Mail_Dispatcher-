import smtplib, ssl, csv
import re

def sendMail(f, smail, spass, ssub, msg):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = smail
    password = spass
    SUBJECT = ssub  
    TEXT = msg
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    context = ssl.create_default_context()
    
    with open(f) as file:
        valid_email=[]
        invalid_email=[]
        count = 0
        reader = csv.reader(file)
        next(reader) 
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 
        for value in reader:
            if(re.fullmatch(regex, value[0])):
                valid_email.append(value[0].strip())
                count = count + 1
            else:
                invalid_email.append(value[0].strip())    
    

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, valid_email, message)
    return valid_email