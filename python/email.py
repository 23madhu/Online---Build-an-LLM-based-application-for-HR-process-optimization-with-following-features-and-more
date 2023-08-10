import smtplib

my_email = 'satyavinayak2002@gmail.com'
password = 'zdefpqbdxdqrmcie'

connection = smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs='srihemanthvsh@gmail.com',msg="Hi ra erripuka ! moddaguddu")
connection.close()