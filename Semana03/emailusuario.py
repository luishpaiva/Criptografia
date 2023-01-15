import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email(de: str, para: str, assunto: str, corpo: str):
    server = "smtp.gmail.com"
    port = 587
    username = "luisinhohpaiva@gmail.com"
    password = "njdnbyzjunyycydu"

    mail_from = de
    mail_to = para
    mail_subject = assunto
    mail_body = corpo

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = mail_to
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText(mail_body, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username, password)
    connection.send_message(mensagem)
    connection.quit()
