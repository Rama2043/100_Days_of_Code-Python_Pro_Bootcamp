import smtplib

#MY_EMAIL = <Give your own mail>
#MY_PASSWORD = <Give your password>

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL,password=MY_PASSWORD)
connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Hello from Rama")