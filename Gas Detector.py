import smtplib
import time, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print ('Gas has been detected!')
    smtpUser = 'dhirajaswani2727@gmail.com'
    smtpPass = 'dhirajdilipkumaraswani'

    toAdd = 'sanjayjanyani43@gmail.com'
    fromAdd = smtpUser

    subject = 'Alert Gas Leaked'
    header = 'To: ' + toAdd +  '\n' + 'From: ' + fromAdd + '\n' + 'Subject:' + subject
    body = 'ALERT!! Leakage of gas has been detected in your Factory'

    

    s = smtplib.SMTP('smtp.gmail.com',587)

    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(smtpUser,smtpPass)
    s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

    s.quit()

    return

GPIO.add_event_detect(19, GPIO.RISING)
GPIO.add_event_callback(19, action)

try:
    while True:
        print ('Normal Environment')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
