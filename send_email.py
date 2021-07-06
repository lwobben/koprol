import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import config

# Set SMTP server and logins
s = smtplib.SMTP(host='mail.jouwweb.nl', port=587)
s.starttls()
address = config.address
s.login(address, config.password)

# Open csv & loop through
df = pd.read_csv('bestellingen.csv')
for index, row in df.iterrows():
    with open('message.txt', 'r', encoding='utf-8') as template_file:
        
        # Message variables
        name = row['Naam']
        first_name = name.split(" ")[0]
        
        # Load message
        msg = MIMEMultipart()       # create a message
        message = f"{template_file.read()}".format(**locals())

        
        # Message parameters
        msg['From']=address
        msg['To']=row['E-mail']
        msg['Subject']=f"{first_name}, je Rollies zijn klaar!"
        
        # Send
        print(f"Message is being send to {name}")
        msg.attach(MIMEText(message, 'plain'))        
        s.send_message(msg)
    
    del msg