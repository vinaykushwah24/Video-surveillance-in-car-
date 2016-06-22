import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("vinay.kushwah2014@vit.ac.in", "8109739950")

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("vinay.kushwah2014@vit.ac.in", "vinaykushwah24@gmail.com", msg)
