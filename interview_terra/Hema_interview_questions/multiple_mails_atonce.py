import smtplib
from email.message import EmailMessage

email_id ='qq6630685@gmail.com'
email_pass='krpe nrri qldy mqxp'
list =["pavanb1997@gmail.com",'pavanb0512@gmail.com','pavan.buchipalli@terralogic.com']
msg = EmailMessage()
msg['subject']='First mail using python'
msg['From']=email_id
msg['To']=list

msg.set_content("Status of the work")


with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(email_id,email_pass)
    smtp.send_message(msg)


