from datetime import datetime
from threading import Timer
import threading

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

from twilio.rest import Client
import requests


def sender(args):




    msg=""
    msg = '<head><style>body{background-color:blue;} p{color:yellow; align : center; font-style: italic;font-size: 30px;font-weight: bold;} th{color:blue;}</style></head> <body style="background-color:powderblue;">'

    msg+='hello sir u had set ur schedule in this time  for '+args[0]+"     "+args[1]+'    have a good day'

    msg += '</body></html>'



    gmailaddress = 'mybestpal2018@gmail.com'
    gmailpassword = 'mybestpaladmin2018'
    mailto = args[2]





    try:
        client = None
        message = MIMEMultipart('alternative')
        message['from'] = gmailaddress
        message['to'] = mailto
        message['subject'] = f'admin from my best pal '
        part1 = MIMEText(msg, 'html')
        message.attach(part1)
        client = smtplib.SMTP("smtp.gmail.com", 587)
        client.ehlo()
        client.starttls()
        client.login(gmailaddress, gmailpassword)
        msg = message.as_string()
        client.sendmail(gmailaddress, mailto, msg)

    except smtplib.SMTPAuthenticationError:

        return
    except smtplib.SMTPDataError:

        return
    except smtplib.SMTPConnectError:

        return
    except smtplib.SMTPNotSupportedError:

        return
    except smtplib.SMTPException:

        return



def smssender(args):

    print(args)

    url = "https://www.fast2sms.com/dev/bulk"
    s = args[2]
    msg = "msg from mybest pal admin you scheduled a task this time for  " + args[0] + " describing  " + args[1] + " thank you have a good day"
    payload = "sender_id=FSTSMS&message=" + msg + "&language=english&route=p&numbers=" + s
    headers = {
        'authorization': "GxeVaoMR9Lluuxjw3QQV3AaLkRgYnSmL4ForqqadV43lHSV8ZkLrlAu3fjvC",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }


    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    print("sent")




def sendalert(*args):

    sender(args)

def sendsmsalert(*args):
    smssender(args)




def create_schedule(ye,m,d,hr,mn,se,minse,type,descrption,email,phno):
    x = datetime.today()
    y = x.replace(year=ye,month=m,day=d,hour=hr, minute=mn, second=se, microsecond=minse)
    delta_t = y - x
    secs = delta_t.seconds + 1

    t2 = Timer(secs, sendsmsalert, args=[type, descrption, phno])
    t2.start()

    t = Timer(secs, sendalert,args=[type,descrption,email])
    t.start()



def start_schedule(y,m,d,hr,mn,se,minse,type,description,email,phno):
    t1 = threading.Thread(target=create_schedule, args=(y,m,d,hr,mn,0,0,type,description,email,phno))
    t1.start()
    t1.join()

